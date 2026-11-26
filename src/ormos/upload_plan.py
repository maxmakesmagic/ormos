"""Compare a built site with a verified deployment inventory."""

import argparse
import json
import logging
import os
import re
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from hashlib import sha256
from mimetypes import MimeTypes
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TextIO

from .paths import read_json_lines, route, site_file

CONTENT_TYPES = {
    ".css": "text/css",
    ".csv": "text/csv",
    ".htm": "text/html",
    ".html": "text/html",
    ".js": "text/javascript",
    ".json": "application/json",
    ".jsonl": "application/x-ndjson",
    ".swf": "application/x-shockwave-flash",
    ".txt": "text/plain",
    ".vtt": "text/vtt",
    ".wasm": "application/wasm",
    ".xml": "application/xml",
}
MIME_TYPES = MimeTypes()
SHA256 = re.compile(r"[a-f0-9]{64}")
UNSAFE_KEY = re.compile(r"[\\\x00-\x1f\x7f]")
logger = logging.getLogger(__name__)


def _cache_control(content_type: str) -> str:
    cache = "public, max-age=300"
    if content_type.partition(";")[0] == "text/html":
        cache += ", no-transform"
    return cache


def _object_key(key: object) -> str:
    if (
        not isinstance(key, str)
        or UNSAFE_KEY.search(key)
        or any(part in {"", ".", ".."} for part in key.split("/"))
    ):
        raise ValueError(f"Invalid object key: {key!r}")
    return key


@dataclass(frozen=True, slots=True)
class SiteObject:
    """The bytes and serving metadata of one site object."""

    key: str
    size: int
    sha256: str
    content_type: str
    cache_control: str
    redirect: str | None

    @classmethod
    def from_row(cls, row: dict[str, object]) -> "SiteObject":
        """Read an object from a deployment inventory row."""
        key = _object_key(row.get("key"))
        size = row.get("size")
        digest = row.get("sha256")
        content_type = row.get("content_type")
        redirect = row.get("redirect")
        if (
            type(size) is not int
            or size < 0
            or not isinstance(digest, str)
            or not SHA256.fullmatch(digest)
            or not isinstance(content_type, str)
            or not content_type.strip()
            or (redirect is not None and not isinstance(redirect, str))
        ):
            raise ValueError(f"Invalid site object metadata: {key}")
        cache = row.get("cache_control", _cache_control(content_type))
        if not isinstance(cache, str):
            raise ValueError(f"Invalid cache control for site object: {key}")  # noqa: TRY004
        return cls(key, size, digest, content_type, cache, redirect)

    @classmethod
    def from_file(cls, root: Path, key: str, redirect: str | None) -> "SiteObject":
        """Hash the built object and record its publication metadata."""
        path = root / _object_key(key)
        digest = sha256()
        with path.open("rb") as stream:
            while block := stream.read(1024 * 1024):
                digest.update(block)
            size = stream.tell()
        if key == "robots.txt":
            content_type = "text/plain; charset=utf-8"
        else:
            content_type = (
                CONTENT_TYPES.get(path.suffix.lower())
                or MIME_TYPES.guess_type(path.name)[0]
                or "application/octet-stream"
            )
        return cls(
            key,
            size,
            digest.hexdigest(),
            content_type,
            _cache_control(content_type),
            redirect,
        )

    def write(self, stream: TextIO, *, change: str | None = None) -> None:
        """Write the object as one JSON record."""
        row: dict[str, str | int] = {
            "key": self.key,
            "size": self.size,
            "sha256": self.sha256,
            "content_type": self.content_type,
            "cache_control": self.cache_control,
        }
        if self.redirect is not None:
            row["redirect"] = self.redirect
        if change is not None:
            row["change"] = change
        stream.write(json.dumps(row, ensure_ascii=False) + "\n")


def _raise_walk_error(error: OSError) -> None:
    raise error


def _inventory_objects(path: Path) -> Iterator[SiteObject]:
    for row in read_json_lines(path):
        try:
            yield SiteObject.from_row(row)
        except ValueError as error:
            raise ValueError(f"{path}: {error}") from error


def _read_baseline(path: Path) -> dict[str, SiteObject]:
    records: dict[str, SiteObject] = {}
    for record in _inventory_objects(path):
        if record.key in records:
            raise ValueError(f"Duplicate object key in {path}: {record.key}")
        records[record.key] = record
    return records


def _candidate_objects(path: Path) -> Iterator[SiteObject]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Expected a regular inventory file: {path}")
    previous = ""
    for record in _inventory_objects(path):
        if record.key <= previous:
            raise ValueError(
                f"Candidate inventory keys must be unique and sorted: {path}"
            )
        previous = record.key
        yield record
    if not previous:
        raise ValueError(f"The candidate inventory is empty: {path}")


def _site_root(site: Path, output: Path) -> Path:
    root = site.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"Expected a site directory: {root}")
    if output.resolve().is_relative_to(root):
        raise ValueError("Output must be outside the built site")
    return root


@dataclass(frozen=True, slots=True)
class _SiteInventory:
    root: Path

    def _keys(self) -> list[str]:
        root = self.root
        keys = []
        for directory, folders, files in os.walk(root, onerror=_raise_walk_error):
            folder = Path(directory)
            for name in folders:
                if (folder / name).is_symlink():
                    raise ValueError(f"Unexpected site symlink: {folder / name}")
            for name in files:
                path = folder / name
                if path.is_symlink() or not path.is_file():
                    raise ValueError(f"Expected a regular site file: {path}")
                keys.append(path.relative_to(root).as_posix())
        if not keys:
            raise ValueError(f"No files in site directory: {root}")
        return sorted(keys)

    def _redirects(self) -> dict[str, str]:
        root = self.root
        path = root / "redirects.jsonl"
        redirects: dict[str, str] = {}
        if path.is_file():
            for row in read_json_lines(path):
                source, target = row.get("path"), row.get("target")
                if not isinstance(source, str) or not isinstance(target, str):
                    raise ValueError(  # noqa: TRY004
                        f"Invalid redirect entry in {path}: {row}"
                    )
                key = site_file(root, source).relative_to(root).as_posix()
                target = route(target)
                if key in redirects or not (root / key).is_file():
                    raise ValueError(f"Missing or duplicate redirect object: {key}")
                if not site_file(root, target).is_file():
                    raise ValueError(f"Missing redirect destination: {target}")
                redirects[key] = target
        return redirects

    def _objects(self) -> Iterator[SiteObject]:
        keys = self._keys()
        redirects = self._redirects()
        logger.info("Inventorying %s site files", f"{len(keys):,}")
        for key in keys:
            yield SiteObject.from_file(self.root, key, redirects.get(key))

    def _write(self, output: Path) -> None:
        if output.exists() or output.is_symlink():
            raise FileExistsError(f"Inventory file already exists: {output}")
        output.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix=f".{output.name}-", dir=output.parent) as stage:
            candidate = Path(stage) / "inventory.ndjson"
            with candidate.open("w", encoding="utf-8") as stream:
                for record in self._objects():
                    record.write(stream)
            output.hardlink_to(candidate)


def _write_plan(
    output: Path, previous: dict[str, SiteObject], candidate: Iterable[SiteObject]
) -> None:
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"Plan directory already exists: {output}")
    logger.info("Comparing with %s deployed objects", f"{len(previous):,}")
    counts: Counter[str] = Counter()
    output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=f".{output.name}-", dir=output.parent) as stage:
        directory = Path(stage)
        with (
            (directory / "inventory.ndjson").open("w", encoding="utf-8") as all_files,
            (directory / "upload.ndjson").open("w", encoding="utf-8") as upload,
            (directory / "removed.ndjson").open("w", encoding="utf-8") as removed,
        ):
            for record in candidate:
                old = previous.pop(record.key, None)
                record.write(all_files)
                if old == record:
                    counts["unchanged"] += 1
                else:
                    change = "added" if old is None else "changed"
                    counts[change] += 1
                    record.write(upload, change=change)
            for key in sorted(previous):
                previous[key].write(removed)
        if output.exists() or output.is_symlink():
            raise FileExistsError(f"Plan directory already exists: {output}")
        directory.rename(output)

    logger.info(
        "%s added, %s changed, %s removed, %s unchanged",
        f"{counts['added']:,}",
        f"{counts['changed']:,}",
        f"{len(previous):,}",
        f"{counts['unchanged']:,}",
    )


@dataclass(frozen=True, slots=True)
class UploadPlan:
    """Compare a built site with the recorded state of an earlier deployment."""

    site: Path
    baseline: Path
    overlays: tuple[Path, ...]
    output: Path

    def write(self) -> None:
        """Write a new inventory and lists of uploads and removals."""
        root = _site_root(self.site, self.output)
        previous = _read_baseline(self.baseline)
        for path in self.overlays:
            previous.update(_read_baseline(path))
        _write_plan(self.output, previous, _SiteInventory(root)._objects())


@dataclass(frozen=True, slots=True)
class InventoryPlan:
    """Compare inventory records without opening or executing candidate files."""

    candidate: Path
    baseline: Path
    output: Path

    def write(self) -> None:
        """Write a comparison against the verified deployment inventory."""
        _write_plan(
            self.output,
            _read_baseline(self.baseline),
            _candidate_objects(self.candidate),
        )


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )


def inventory_main() -> None:
    """Read arguments and write an inventory for a built site."""
    parser = argparse.ArgumentParser(description="Inventory a built Ormos site.")
    parser.add_argument("--site", type=Path, required=True, help="Built site directory")
    parser.add_argument("--output", type=Path, required=True, help="New inventory file")
    args = parser.parse_args()
    _configure_logging()
    try:
        root = _site_root(args.site, args.output)
        _SiteInventory(root)._write(args.output)
    except (OSError, ValueError) as error:
        parser.error(str(error))


def main() -> None:
    """Read arguments and write an upload plan for the built site."""
    parser = argparse.ArgumentParser(description="Plan uploads for a built Ormos site.")
    parser.add_argument("--site", type=Path, required=True, help="Built site directory")
    parser.add_argument(
        "--baseline", type=Path, required=True, help="Verified deployment inventory"
    )
    parser.add_argument(
        "--overlay",
        type=Path,
        action="append",
        default=[],
        help="Verified object updates",
    )
    parser.add_argument("--output", type=Path, required=True, help="New plan directory")
    args = parser.parse_args()
    _configure_logging()
    plan = UploadPlan(args.site, args.baseline, tuple(args.overlay), args.output)
    try:
        plan.write()
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
