"""Exercise archive removals against an in-memory R2 client."""

import json
from base64 import b64encode
from hashlib import md5
from io import BytesIO, StringIO
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast
from zipfile import ZipFile

import pytest
from botocore.awsrequest import AWSPreparedRequest
from botocore.exceptions import ClientError

from ormos.deploy import (
    INVENTORY,
    REMOVED,
    STATE_KEY,
    UPLOAD,
    R2Deployment,
    _deployment,
)
from ormos.paths import read_json_lines
from ormos.upload_plan import SiteObject

if TYPE_CHECKING:
    from mypy_boto3_s3 import S3Client

STATE_BUCKET = "test-state"
SITE_BUCKET = "test-site"
KEEP = "index.html"
RESTORE = "restore.html"
STALE = "stale.html"


def _archive_objects(payload: bytes) -> dict[str, list[str]]:
    with ZipFile(BytesIO(payload)) as archive:
        return {
            name: [json.loads(line)["key"] for line in archive.read(name).splitlines()]
            for name in archive.namelist()
        }


class _FakeR2:
    def __init__(self, records: list[SiteObject]) -> None:
        rows = StringIO()
        for record in records:
            record.write(rows)
        payload = BytesIO()
        with ZipFile(payload, "w") as archive:
            archive.writestr(INVENTORY, rows.getvalue())
        self.state = payload.getvalue()
        self.etag = '"state-0"'
        self.objects = {
            record.key: {
                "ETag": f'"{record.sha256}"',
                "ContentLength": record.size,
                "ContentType": record.content_type,
                "CacheControl": record.cache_control,
                "Metadata": {"sha256": record.sha256},
            }
            for record in records
        }
        self.saved_states: list[dict[str, list[str]]] = []
        self.deleted: list[str] = []
        self.uploaded: list[str] = []
        self.fail_deleting: str | None = None

    def get_object(self, *, Bucket: str, Key: str) -> dict[str, object]:
        """Return the saved deployment state."""
        assert (Bucket, Key) == (STATE_BUCKET, STATE_KEY)
        return {"ETag": self.etag, "Body": BytesIO(self.state)}

    def head_object(self, *, Bucket: str, Key: str) -> dict[str, object]:
        """Report the current metadata or an object miss."""
        assert Bucket == SITE_BUCKET
        if Key not in self.objects:
            raise ClientError(
                {
                    "Error": {"Code": "NotFound", "Message": "Object does not exist"},
                    "ResponseMetadata": {
                        "HTTPStatusCode": 404,
                        "RequestId": "",
                        "HostId": "",
                        "HTTPHeaders": {},
                        "RetryAttempts": 0,
                    },
                },
                "HeadObject",
            )
        return self.objects[Key]

    def put_object(self, **request: Any) -> dict[str, str]:
        """Save a new state archive or restore one absent site file."""
        payload = request["Body"].read()
        assert request["ContentLength"] == len(payload)
        key = request["Key"]
        if request["Bucket"] == STATE_BUCKET:
            assert key == STATE_KEY
            assert request["IfMatch"] == self.etag
            self.state = payload
            self.saved_states.append(_archive_objects(payload))
            self.etag = f'"state-{len(self.saved_states)}"'
            return {"ETag": self.etag}
        assert request["Bucket"] == SITE_BUCKET
        assert request["IfNoneMatch"] == "*"
        assert key not in self.objects
        etag = '"restored"'
        self.objects[key] = {
            "ETag": etag,
            "ContentLength": len(payload),
            "ContentType": request["ContentType"],
            "CacheControl": request["CacheControl"],
            "Metadata": request["Metadata"],
        }
        self.uploaded.append(key)
        return {"ETag": etag}

    def delete_objects(
        self, *, Bucket: str, Delete: dict[str, Any], **_: object
    ) -> dict[str, list[dict[str, str]]]:
        """Delete objects and report per-key errors for a failed item."""
        assert Bucket == SITE_BUCKET
        assert Delete["Quiet"]
        assert {item["Key"] for item in Delete["Objects"]} <= set(
            self.saved_states[-1][REMOVED]
        )
        errors = []
        for item in Delete["Objects"]:
            key = item["Key"]
            if key == self.fail_deleting:
                errors.append({"Key": key, "Code": "InternalError"})
                continue
            self.objects.pop(key)
            self.deleted.append(key)
        return {"Errors": errors} if errors else {}

    def run(self, site: Path, output: Path, *, apply: bool) -> None:
        """Run the normal deployment entry point with this client."""
        deployment = R2Deployment(cast("S3Client", self), STATE_BUCKET, SITE_BUCKET)
        deployment.run(site, output, apply=apply)


@pytest.fixture
def archive(tmp_path: Path) -> tuple[_FakeR2, Path]:
    """Seed a site and a previous inventory with two additional files."""
    previous = tmp_path / "previous"
    previous.mkdir()
    records = []
    for key in (KEEP, RESTORE, STALE):
        (previous / key).write_text(key, encoding="utf-8")
        records.append(SiteObject.from_file(previous, key, None))
    site = tmp_path / "site"
    site.mkdir()
    (site / KEEP).write_text(KEEP, encoding="utf-8")
    return _FakeR2(records), site


def test_dry_plan_reports_removals_without_mutating_r2(
    tmp_path: Path, archive: tuple[_FakeR2, Path]
) -> None:
    """Record removed files in the plan and keep the deployment untouched."""
    client, site = archive
    output = tmp_path / "plan"
    client.run(site, output, apply=False)

    assert [row["key"] for row in read_json_lines(output / REMOVED)] == [RESTORE, STALE]
    assert set(client.objects) == {KEEP, RESTORE, STALE}
    assert not (client.saved_states or client.deleted or client.uploaded)


def test_apply_commits_a_deletion_only_deployment(
    tmp_path: Path, archive: tuple[_FakeR2, Path]
) -> None:
    """Journal removed files before deleting them and commit the new inventory."""
    client, site = archive
    unmanaged = "outside-inventory.html"
    client.objects[unmanaged] = client.objects[KEEP].copy()
    client.run(site, tmp_path / "plan", apply=True)

    assert client.saved_states[0][REMOVED] == [RESTORE, STALE]
    assert client.saved_states[-1] == {INVENTORY: [KEEP]}
    assert set(client.objects) == {KEEP, unmanaged}
    assert client.deleted == [RESTORE, STALE]
    assert not client.uploaded


def test_apply_preserves_an_object_that_differs_from_the_inventory(
    tmp_path: Path, archive: tuple[_FakeR2, Path]
) -> None:
    """Stop before deleting a batch when a live object changed outside a deploy."""
    client, site = archive
    client.objects[STALE]["Metadata"] = {"sha256": "different"}

    with pytest.raises(ValueError, match=f"deployment inventory: {STALE}"):
        client.run(site, tmp_path / "plan", apply=True)

    assert not client.deleted
    assert _archive_objects(client.state)[REMOVED] == [RESTORE, STALE]


def test_apply_recovers_a_partial_delete_before_restoring_a_file(
    tmp_path: Path, archive: tuple[_FakeR2, Path]
) -> None:
    """Reconcile missing keys so a later build can publish them again."""
    client, site = archive
    client.fail_deleting = STALE
    with pytest.raises(ValueError, match="InternalError"):
        client.run(site, tmp_path / "failed-plan", apply=True)

    assert _archive_objects(client.state)[REMOVED] == [RESTORE, STALE]
    assert set(client.objects) == {KEEP, STALE}
    client.fail_deleting = None
    (site / RESTORE).write_text(RESTORE, encoding="utf-8")
    output = tmp_path / "retry-plan"
    client.run(site, output, apply=True)

    assert [row["key"] for row in read_json_lines(output / UPLOAD)] == [RESTORE]
    assert client.uploaded == [RESTORE]
    assert client.deleted == [RESTORE, STALE]
    assert _archive_objects(client.state) == {INVENTORY: [KEEP, RESTORE]}


def test_r2_delete_request_uses_content_md5(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sign the marshalled delete batch with the checksum R2 accepts."""
    monkeypatch.setenv("ORMOS_R2_ACCOUNT_ID", "0" * 32)
    monkeypatch.setenv("ORMOS_R2_STATE_BUCKET", STATE_BUCKET)
    monkeypatch.setenv("ORMOS_R2_SITE_BUCKET", SITE_BUCKET)
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "test-key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "test-secret")
    client = _deployment().client
    requests: list[AWSPreparedRequest] = []

    def capture(request: AWSPreparedRequest, **_kwargs: object) -> None:
        requests.append(request)
        raise RuntimeError("Captured request before sending")

    client.meta.events.register("before-send.s3.DeleteObjects", capture)
    with pytest.raises(RuntimeError, match="Captured request before sending"):
        client.delete_objects(
            Bucket=SITE_BUCKET, Delete={"Objects": [{"Key": STALE}], "Quiet": True}
        )

    (request,) = requests
    assert isinstance(request.body, bytes)
    assert request.headers["Content-MD5"] == b64encode(
        md5(request.body, usedforsecurity=False).digest()
    )
    assert "x-amz-checksum-crc32" not in request.headers
