"""Validate public routes and map them to static files."""

import json
import re
import unicodedata
from collections.abc import Iterator
from pathlib import Path

SAFE_COMPONENT = re.compile(r"[A-Za-z0-9_~-][A-Za-z0-9._~-]*\Z")
LEGACY_ASCII = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._~- "
)


def route(value: str) -> str:
    """Accept a site-rooted route and remove a single directory suffix."""
    if not isinstance(value, str) or not value.startswith("/"):
        raise ValueError(f"Expected a root-relative route, got {value!r}")
    normalized = value.removesuffix("/") or "/"
    if normalized != "/" and not all(
        SAFE_COMPONENT.fullmatch(component) for component in normalized[1:].split("/")
    ):
        raise ValueError(f"Unsafe route {value!r}")
    return normalized


def component(value: str) -> str:
    """Return one safe route component or raise an error."""
    if not isinstance(value, str) or not SAFE_COMPONENT.fullmatch(value):
        raise ValueError(f"Unsafe path component {value!r}")
    return value


def legacy_component(value: str) -> bool:
    """Accept safe characters from decoded historical URLs."""
    if SAFE_COMPONENT.fullmatch(value):
        return True
    if not value or value.startswith("."):
        return False
    folded = unicodedata.normalize("NFKC", value)
    if folded in {".", ".."} or any(char in folded for char in "/\\%"):
        return False
    return all(
        char in LEGACY_ASCII
        if char.isascii()
        else (category := unicodedata.category(char))[0] in "LMNPS" or category == "Zs"
        for char in value
    )


def legacy_redirect_route(value: str) -> str:
    """Accept a decoded historical route only below the old archive directory."""
    if isinstance(value, str) and value.startswith("/archive/"):
        normalized = value.removesuffix("/")
        if normalized.startswith("/archive/") and all(
            legacy_component(part)
            for part in normalized.removeprefix("/archive/").split("/")
        ):
            return normalized
    raise ValueError(f"Unsafe legacy archive route {value!r}")


def site_file(root: Path, path: str) -> Path:
    """Map a route to its HTML file below the site root."""
    normalized = (
        legacy_redirect_route(path)
        if isinstance(path, str) and path.startswith("/archive/")
        else route(path)
    )
    relative = normalized.lstrip("/")
    candidate = root / relative
    if relative.endswith((".html", ".htm")):
        return candidate
    return candidate / "index.html"


def write_new(path: Path, value: str) -> None:
    """Write a UTF-8 file and fail if the file already exists."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as out:
        out.write(value)


def read_json_lines(path: Path) -> Iterator[dict]:
    """Read one JSON object per nonempty line."""
    with path.open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            if line.strip():
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError(f"Expected a JSON object at {path}:{number}")
                yield row
