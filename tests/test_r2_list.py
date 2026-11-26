"""Test object metadata listings and fallback errors."""

import json
from unittest.mock import MagicMock

import pytest

from ormos import r2_list


def _response(status, data=None, retry_after=None):
    response = MagicMock()
    response.__enter__.return_value = response
    response.status = status
    response.getheader.return_value = retry_after
    response.read.return_value = json.dumps(data).encode()
    return response


def _listing(monkeypatch, *responses):
    connection = MagicMock()
    connection.getresponse.side_effect = responses
    monkeypatch.setattr(r2_list, "HTTPSConnection", lambda *args, **kwargs: connection)
    return connection, r2_list.R2ObjectListing("account", "bucket", "private-token")


def _page(key, *, truncated, cursor=None):
    return _response(
        200,
        {
            "success": True,
            "result": [
                {
                    "key": key,
                    "size": 125,
                    "etag": "e7a8",
                    "http_metadata": {
                        "contentType": "text/html",
                        "cacheControl": "max-age=60",
                    },
                    "custom_metadata": {
                        "SHA256": "digest",
                        "redirectlocation": "/destination",
                    },
                }
            ],
            "result_info": {"is_truncated": truncated, "cursor": cursor},
        },
    )


def test_lists_and_normalizes_metadata(monkeypatch):
    """Request every page and match the field names used by S3 HEAD."""
    connection, listing = _listing(
        monkeypatch,
        _page("a", truncated=True, cursor="x+/="),
        _page("b", truncated=False),
    )

    metadata = {
        "ETag": '"e7a8"',
        "ContentLength": 125,
        "ContentType": "text/html",
        "CacheControl": "max-age=60",
        "Metadata": {"sha256": "digest", "redirectlocation": "/destination"},
    }
    assert list(listing.objects()) == [("a", metadata), ("b", metadata)]
    first, second = connection.request.call_args_list
    assert first.args == (
        "GET",
        "/client/v4/accounts/account/r2/buckets/bucket/objects?per_page=1000",
    )
    assert first.kwargs["headers"]["Authorization"] == "Bearer private-token"
    assert second.args[1].endswith("&cursor=x%2B%2F%3D")
    assert "private-token" not in repr(listing)
    connection.close.assert_called_once()


def test_retries_rate_limit_and_network_failure(monkeypatch):
    """Use Retry-After and reconnect before another attempt."""
    delay = MagicMock()
    monkeypatch.setattr(r2_list, "sleep", delay)
    connection, listing = _listing(
        monkeypatch,
        _response(429, retry_after="4"),
        ConnectionError("private-token"),
        _page("a", truncated=False),
    )

    assert len(list(listing.objects())) == 1
    assert [call.args[0] for call in delay.call_args_list] == [4, 2]
    assert connection.request.call_count == 3
    assert connection.close.call_count == 3


@pytest.mark.parametrize("status,retry_after", [(403, None), (429, "300")])
def test_fails_without_retrying_permission_or_long_rate_limit(
    monkeypatch, status, retry_after
):
    """Return a sanitized error so the caller can fall back to S3."""
    connection, listing = _listing(
        monkeypatch, _response(status, {"detail": "private-token"}, retry_after)
    )

    with pytest.raises(r2_list.R2ListingError, match=f"HTTP {status}$"):
        list(listing.objects())
    connection.request.assert_called_once()


@pytest.mark.parametrize(
    "second_cursor,error",
    [(None, "invalid pagination"), ("same-cursor", "repeated a pagination cursor")],
)
def test_rejects_incomplete_pagination(monkeypatch, second_cursor, error):
    """Fail closed when Cloudflare cannot identify the next page."""
    _, listing = _listing(
        monkeypatch,
        _page("a", truncated=True, cursor="same-cursor"),
        _page("b", truncated=True, cursor=second_cursor),
    )

    with pytest.raises(r2_list.R2ListingError, match=error):
        list(listing.objects())
