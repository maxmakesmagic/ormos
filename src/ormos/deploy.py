"""Plan and apply incremental archive deployments to R2."""

import argparse
import logging
import os
import re
from base64 import b64encode
from collections.abc import Callable, Iterable, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from dataclasses import dataclass
from hashlib import md5, sha256
from heapq import merge
from itertools import islice
from operator import attrgetter
from pathlib import Path
from shutil import copyfileobj
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any, TypeVar
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile

import boto3
from botocore.config import Config
from botocore.exceptions import BotoCoreError, ClientError

from .paths import read_json_lines
from .upload_plan import InventoryPlan, SiteObject, UploadPlan

if TYPE_CHECKING:
    from mypy_boto3_s3.client import S3Client
    from mypy_boto3_s3.type_defs import HeadObjectOutputTypeDef, PutObjectRequestTypeDef

STATE_KEY = "deployment.zip"
INVENTORY = "inventory.ndjson"
UPLOAD = "upload.ndjson"
REMOVED = "removed.ndjson"
WORKERS = 16
DELETE_BATCH_SIZE = 1_000
logger = logging.getLogger(__name__)
Result = TypeVar("Result")


def _objects(path: Path) -> Iterator[SiteObject]:
    previous = ""
    for row in read_json_lines(path):
        record = SiteObject.from_row(row)
        if record.key <= previous:
            raise ValueError(f"Inventory keys must be unique and sorted: {path}")
        previous = record.key
        yield record


def _write_inventory(path: Path, *groups: Iterable[SiteObject]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for record in merge(*groups, key=attrgetter("key")):
            record.write(stream)


def _parallel(
    action: Callable[[SiteObject], Result], records: Iterable[SiteObject]
) -> Iterator[Result]:
    source = iter(records)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        while batch := list(islice(source, WORKERS * 4)):
            yield from pool.map(action, batch)


def _matches(
    remote: "HeadObjectOutputTypeDef | None", record: SiteObject | None
) -> bool:
    if remote is None or record is None:
        return remote is None and record is None
    metadata = remote.get("Metadata", {})
    return (
        remote.get("ContentLength") == record.size
        and remote.get("ContentType") == record.content_type
        and remote.get("CacheControl") == record.cache_control
        and metadata.get("sha256") == record.sha256
        and metadata.get("redirectlocation") == record.redirect
    )


@dataclass(frozen=True, slots=True)
class DeploymentState:
    """A local snapshot of the committed inventory and pending changes."""

    etag: str
    inventory: Path
    pending_uploads: Path | None = None
    pending_removals: Path | None = None

    @property
    def has_pending(self) -> bool:
        """Return whether a deployment journal needs reconciliation."""
        return self.pending_uploads is not None or self.pending_removals is not None

    def dry_baseline(self) -> Path:
        """Return the inventory from the last completed deployment."""
        if self.has_pending:
            logger.warning(
                "Dry plan uses the last completed inventory while a deployment is pending"
            )
        return self.inventory


@dataclass(frozen=True, slots=True)
class R2Deployment:
    """Read deployment state and publish verified changes to the archive."""

    client: "S3Client"
    state_bucket: str
    site_bucket: str

    def _get_state(self, directory: Path) -> DeploymentState:
        try:
            response = self.client.get_object(Bucket=self.state_bucket, Key=STATE_KEY)
        except self.client.exceptions.NoSuchKey as error:
            raise ValueError(
                f"Seed {self.state_bucket}/{STATE_KEY} with the verified deployment inventory"
            ) from error
        archive_path = directory / STATE_KEY
        with closing(response["Body"]) as body, archive_path.open("wb") as archive:
            copyfileobj(body, archive, 1024 * 1024)
        with ZipFile(archive_path) as archive:
            names = archive.namelist()
            if (
                INVENTORY not in names
                or len(names) != len(set(names))
                or set(names) - {INVENTORY, UPLOAD, REMOVED}
            ):
                raise ValueError(
                    f"Expected {INVENTORY} and optional {UPLOAD} and {REMOVED} in {STATE_KEY}"
                )
            for name in names:
                with (
                    archive.open(name) as member,
                    (directory / name).open("wb") as target,
                ):
                    copyfileobj(member, target, 1024 * 1024)
        inventory = directory / INVENTORY
        if next(_objects(inventory), None) is None:
            raise ValueError("The deployment inventory is empty")
        return DeploymentState(
            response["ETag"],
            inventory,
            pending_uploads=directory / UPLOAD if UPLOAD in names else None,
            pending_removals=directory / REMOVED if REMOVED in names else None,
        )

    def _head(self, key: str) -> "HeadObjectOutputTypeDef | None":
        try:
            return self.client.head_object(Bucket=self.site_bucket, Key=key)
        except ClientError as error:
            if error.response["ResponseMetadata"]["HTTPStatusCode"] == 404:
                return None
            raise

    def _put_file(
        self,
        path: Path,
        request: "PutObjectRequestTypeDef",
        record: SiteObject | None = None,
    ) -> str:
        # A single conditional PUT protects the object identified by the prior ETag.
        transport = md5(usedforsecurity=False)
        digest = sha256()
        with path.open("rb") as payload:
            while chunk := payload.read(1024 * 1024):
                transport.update(chunk)
                digest.update(chunk)
            size = payload.tell()
            if record is not None and (
                record.size != size or record.sha256 != digest.hexdigest()
            ):
                raise ValueError(f"Built file changed after planning: {record.key}")
            payload.seek(0)
            request["Body"] = payload
            request["ContentLength"] = size
            request["ContentMD5"] = b64encode(transport.digest()).decode("ascii")
            response = self.client.put_object(**request)
        return response["ETag"]

    def _put_state(
        self,
        etag: str,
        inventory: Path,
        *,
        pending_uploads: Path | None = None,
        pending_removals: Path | None = None,
    ) -> str:
        with TemporaryDirectory(prefix="ormos-state-") as directory:
            archive_path = Path(directory) / STATE_KEY
            with ZipFile(archive_path, "w", ZIP_DEFLATED) as archive:
                archive.write(inventory, INVENTORY)
                if pending_uploads is not None:
                    archive.write(pending_uploads, UPLOAD)
                if pending_removals is not None:
                    archive.write(pending_removals, REMOVED)
            return self._put_file(
                archive_path,
                {
                    "Bucket": self.state_bucket,
                    "Key": STATE_KEY,
                    "ContentType": "application/zip",
                    "CacheControl": "no-store",
                    "IfMatch": etag,
                },
            )

    def _reconcile(self, state: DeploymentState) -> Path:
        if not state.has_pending:
            return state.inventory
        uploads = (
            {record.key: record for record in _objects(state.pending_uploads)}
            if state.pending_uploads is not None
            else {}
        )
        removals = (
            {record.key: record for record in _objects(state.pending_removals)}
            if state.pending_removals is not None
            else {}
        )
        if uploads.keys() & removals.keys():
            raise ValueError("Deployment journal lists a key for upload and removal")
        affected = uploads.keys() | removals.keys()
        previous = {
            record.key: record
            for record in _objects(state.inventory)
            if record.key in affected
        }
        if any(previous.get(key) != record for key, record in removals.items()):
            raise ValueError("Deployment journal removals differ from the inventory")

        def live_update(record: SiteObject) -> SiteObject | None:
            remote = self._head(record.key)
            if _matches(remote, record):
                return record
            if _matches(remote, previous.get(record.key)):
                return None
            raise ValueError(
                f"Live object differs from the deployment journal: {record.key}"
            )

        applied = {
            record.key: record
            for record in _parallel(live_update, uploads.values())
            if record is not None
        }
        removed = {
            key
            for key, present in zip(
                removals, _parallel(self._needs_removal, removals.values()), strict=True
            )
            if not present
        }
        logger.info(
            "Recovered %s uploads and %s removals",
            f"{len(applied):,}",
            f"{len(removed):,}",
        )
        inventory = state.inventory.with_name("reconciled.ndjson")
        _write_inventory(
            inventory,
            (
                record
                for record in _objects(state.inventory)
                if record.key not in applied and record.key not in removed
            ),
            applied.values(),
        )
        return inventory

    def _upload(self, root: Path, record: SiteObject, old: SiteObject | None) -> bool:
        remote = self._head(record.key)
        if _matches(remote, record):
            return False
        if not _matches(remote, old):
            raise ValueError(
                f"Live object differs from the deployment inventory: {record.key}"
            )
        metadata = {"sha256": record.sha256}
        if record.redirect is not None:
            metadata["redirectlocation"] = record.redirect
        request: PutObjectRequestTypeDef = {
            "Bucket": self.site_bucket,
            "Key": record.key,
            "ContentType": record.content_type,
            "CacheControl": record.cache_control,
            "Metadata": metadata,
        }
        if remote is None:
            request["IfNoneMatch"] = "*"
        else:
            request["IfMatch"] = remote["ETag"]
        etag = self._put_file(root / record.key, request, record)
        verified = self._head(record.key)
        if (
            verified is None
            or verified["ETag"] != etag
            or not _matches(verified, record)
        ):
            raise ValueError(f"R2 did not return the expected upload: {record.key}")
        return True

    def _needs_removal(self, record: SiteObject) -> bool:
        remote = self._head(record.key)
        if remote is None:
            return False
        if not _matches(remote, record):
            raise ValueError(
                f"Live object differs from the deployment inventory: {record.key}"
            )
        return True

    def _verify_removal(self, key: str) -> None:
        if self._head(key) is not None:
            raise ValueError(f"R2 still has the object after deletion: {key}")

    def _remove(self, records: Iterator[SiteObject]) -> None:
        # R2 deletes are unconditional. The production workflow serializes writes.
        removed = 0
        checked = 0
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            while batch := list(islice(records, DELETE_BATCH_SIZE)):
                keys = [
                    record.key
                    for record, present in zip(
                        batch, pool.map(self._needs_removal, batch), strict=True
                    )
                    if present
                ]
                if keys:
                    response = self.client.delete_objects(
                        Bucket=self.site_bucket,
                        Delete={
                            "Objects": [{"Key": key} for key in keys],
                            "Quiet": True,
                        },
                    )
                    if errors := response.get("Errors"):
                        first = errors[0]
                        raise ValueError(
                            f"R2 failed to delete {len(errors):,} objects. "
                            f"{first.get('Key')} returned {first.get('Code')}"
                        )
                    for _ in pool.map(self._verify_removal, keys):
                        pass
                    removed += len(keys)
                checked += len(batch)
                if checked % 10_000 == 0:
                    logger.info("Verified %s planned removals", f"{checked:,}")
        logger.info("Deleted %s files", f"{removed:,}")

    def _apply(
        self, state: DeploymentState, baseline: Path, site: Path, plan: Path
    ) -> None:
        upload = plan / UPLOAD
        removals = plan / REMOVED
        has_uploads = upload.stat().st_size > 0
        has_removals = removals.stat().st_size > 0
        if not (has_uploads or has_removals or state.has_pending):
            logger.info("No deployment changes needed")
            return
        etag = state.etag
        if has_uploads or has_removals:
            etag = self._put_state(
                etag,
                baseline,
                pending_uploads=upload if has_uploads else None,
                pending_removals=removals if has_removals else None,
            )
        if has_uploads:
            keys = {record.key for record in _objects(upload)}
            previous = {
                record.key: record
                for record in _objects(baseline)
                if record.key in keys
            }

            def publish(record: SiteObject) -> bool:
                return self._upload(site, record, previous.get(record.key))

            uploaded = 0
            for completed, written in enumerate(
                _parallel(publish, _objects(upload)), 1
            ):
                uploaded += written
                if completed % 10_000 == 0:
                    logger.info("Verified %s planned uploads", f"{completed:,}")
            logger.info("Uploaded %s files", f"{uploaded:,}")

        if has_removals:
            self._remove(_objects(removals))
        self._put_state(etag, plan / INVENTORY)
        logger.info("Published the verified deployment inventory")

    def run(self, site: Path, output: Path, *, apply: bool) -> None:
        """Create an upload plan and apply it only when requested."""
        with TemporaryDirectory(prefix="ormos-deployment-") as temp:
            state = self._get_state(Path(temp))
            baseline = self._reconcile(state) if apply else state.dry_baseline()
            UploadPlan(site, baseline, (), output).write()
            if apply:
                self._apply(state, baseline, site.resolve(strict=True), output)

    def plan_inventory(self, candidate: Path, output: Path) -> None:
        """Compare an inventory without reading site files or writing to R2."""
        with TemporaryDirectory(prefix="ormos-deployment-") as temp:
            state = self._get_state(Path(temp))
            InventoryPlan(candidate, state.dry_baseline(), output).write()


def _delete_batch_checksum(params: dict[str, Any], **_kwargs: object) -> None:
    """Use the classic S3 Content-MD5 header for R2 bulk deletes."""
    # Botocore assigns a flexible CRC32 checksum even in when_required mode.
    params["context"].pop("checksum", None)
    digest = md5(params["body"], usedforsecurity=False).digest()
    params["headers"]["Content-MD5"] = b64encode(digest).decode("ascii")


def _deployment() -> R2Deployment:
    account = os.environ.get("ORMOS_R2_ACCOUNT_ID", "")
    state = os.environ.get("ORMOS_R2_STATE_BUCKET", "")
    site = os.environ.get("ORMOS_R2_SITE_BUCKET") or "ormos-site"
    if not re.fullmatch(r"[a-f0-9]{32}", account):
        raise ValueError("Set ORMOS_R2_ACCOUNT_ID to the Cloudflare account ID")
    if not state or state == site:
        raise ValueError(
            "Set ORMOS_R2_STATE_BUCKET to the private deployment state bucket"
        )
    if not os.environ.get("AWS_ACCESS_KEY_ID") or not os.environ.get(
        "AWS_SECRET_ACCESS_KEY"
    ):
        raise ValueError(
            "Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to the R2 credentials"
        )
    client = boto3.client(
        "s3",
        endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
        region_name="auto",
        config=Config(
            s3={"addressing_style": "path"},
            retries={"mode": "standard", "total_max_attempts": 5},
            connect_timeout=10,
            read_timeout=60,
            max_pool_connections=WORKERS,
            request_checksum_calculation="when_required",
            response_checksum_validation="when_required",
        ),
    )
    client.meta.events.register("before-call.s3.DeleteObjects", _delete_batch_checksum)
    return R2Deployment(client, state, site)


def main() -> int:
    """Read the command arguments and plan or apply an archive deployment."""
    parser = argparse.ArgumentParser(description="Deploy a built Ormos site to R2.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--site", type=Path, help="Built site directory")
    source.add_argument(
        "--inventory", type=Path, help="Candidate inventory for a dry plan"
    )
    parser.add_argument("--output", type=Path, required=True, help="New plan directory")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply and verify planned uploads and removals",
    )
    args = parser.parse_args()
    if args.apply and args.inventory is not None:
        parser.error("--apply requires a built site directory")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    try:
        deployment = _deployment()
        if args.inventory is not None:
            deployment.plan_inventory(args.inventory, args.output)
        else:
            deployment.run(args.site, args.output, apply=args.apply)
    except (BadZipFile, BotoCoreError, ClientError, OSError, ValueError) as error:
        logger.error("%s", error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
