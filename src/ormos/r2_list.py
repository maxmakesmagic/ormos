"""Read object metadata in batches from the Cloudflare R2 REST API."""

import json
from collections.abc import Generator
from contextlib import closing
from dataclasses import dataclass, field
from http.client import HTTPException, HTTPResponse, HTTPSConnection
from time import sleep
from typing import TypedDict
from urllib.parse import quote, urlencode

_ATTEMPTS = 4
_MAX_RETRY_DELAY = 15
_REQUEST_TIMEOUT = 20


class R2ListingError(Exception):
    """Report a listing failure without exposing credentials or response bodies."""


class R2ListedObject(TypedDict, total=False):
    """Represent the subset of S3 HEAD metadata present in a listing."""

    ETag: str
    ContentLength: int
    ContentType: str
    CacheControl: str
    Metadata: dict[str, str]


def _read_page(response: HTTPResponse) -> tuple[list[object], str | None]:
    try:
        data = json.loads(response.read())
    except ValueError:
        raise R2ListingError("R2 object listing returned invalid JSON") from None
    if not isinstance(data, dict) or data.get("success") is not True:
        raise R2ListingError("R2 object listing reported an API error")
    objects = data.get("result")
    info = data.get("result_info")
    if not isinstance(objects, list) or not isinstance(info, dict):
        raise R2ListingError("R2 object listing is missing results or pagination data")
    truncated = info.get("is_truncated")
    if truncated is False:
        return objects, None
    cursor = info.get("cursor")
    if (
        truncated is not True
        or not isinstance(cursor, str)
        or not cursor
        or not objects
    ):
        raise R2ListingError("R2 object listing returned invalid pagination data")
    return objects, cursor


def _read_object(row: object) -> tuple[str, R2ListedObject]:
    if not isinstance(row, dict):
        raise R2ListingError("R2 object listing returned an invalid object")
    key = row.get("key")
    size = row.get("size")
    etag = row.get("etag")
    if (
        not isinstance(key, str)
        or not key
        or type(size) is not int
        or size < 0
        or not isinstance(etag, str)
        or not etag
        or '"' in etag
    ):
        raise R2ListingError("R2 object listing returned invalid object identity")

    record: R2ListedObject = {"ContentLength": size, "ETag": f'"{etag}"'}
    http = row.get("http_metadata", {})
    custom = row.get("custom_metadata", {})
    if not isinstance(http, dict) or not isinstance(custom, dict):
        raise R2ListingError("R2 object listing returned invalid object metadata")
    content_type = http.get("contentType")
    cache_control = http.get("cacheControl")
    if isinstance(content_type, str):
        record["ContentType"] = content_type
    if isinstance(cache_control, str):
        record["CacheControl"] = cache_control
    if any(not isinstance(value, str) for value in custom.values()):
        raise R2ListingError("R2 object listing returned invalid custom metadata")
    record["Metadata"] = {name.lower(): value for name, value in custom.items()}
    return key, record


@dataclass(frozen=True, slots=True)
class R2ObjectListing:
    """List a bucket over one reusable HTTPS connection."""

    account: str
    bucket: str
    token: str = field(repr=False)

    def _page(
        self, connection: HTTPSConnection, path: str
    ) -> tuple[list[object], str | None]:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }
        for attempt in range(_ATTEMPTS):
            delay = 2**attempt
            try:
                connection.request("GET", path, headers=headers)
                with connection.getresponse() as response:
                    if response.status == 200:
                        return _read_page(response)
                    failure = f"R2 object listing returned HTTP {response.status}"
                    if response.status not in (408, 429) and response.status < 500:
                        raise R2ListingError(failure)
                    retry_after = response.getheader("Retry-After")
                    if retry_after is not None and retry_after.isdecimal():
                        delay = max(delay, int(retry_after))
            except (OSError, HTTPException):
                failure = "R2 object listing failed to reach Cloudflare"
            except ValueError:
                raise R2ListingError(
                    "R2 object listing could not send a request"
                ) from None
            connection.close()
            if attempt == _ATTEMPTS - 1 or delay > _MAX_RETRY_DELAY:
                raise R2ListingError(failure)
            sleep(delay)
        raise AssertionError("R2 object listing exhausted its retry loop")

    def objects(self) -> Generator[tuple[str, R2ListedObject], None, None]:
        """Yield key and metadata for every object in the bucket."""
        account = quote(self.account, safe="")
        bucket = quote(self.bucket, safe="")
        path = f"/client/v4/accounts/{account}/r2/buckets/{bucket}/objects"
        params = {"per_page": "1000"}
        previous_key = ""
        cursors: set[str] = set()
        with closing(
            HTTPSConnection("api.cloudflare.com", timeout=_REQUEST_TIMEOUT)
        ) as connection:
            while True:
                rows, cursor = self._page(connection, f"{path}?{urlencode(params)}")
                if cursor is not None and cursor in cursors:
                    raise R2ListingError(
                        "R2 object listing repeated a pagination cursor"
                    )
                for row in rows:
                    key, record = _read_object(row)
                    if key <= previous_key:
                        raise R2ListingError(
                            "R2 object listing returned unordered keys"
                        )
                    previous_key = key
                    yield key, record
                if cursor is None:
                    return
                cursors.add(cursor)
                params["cursor"] = cursor
