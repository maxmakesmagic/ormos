"""Check that a slow R2 request does not hold up the next group of work."""

from concurrent.futures import ThreadPoolExecutor
from threading import Event

from ormos.deploy import _parallel


def test_parallel_replenishes_before_the_previous_window_finishes() -> None:
    """Start a ninth request while the second is pending and yield in order."""
    records = range(9)
    release_second = Event()
    started_ninth = Event()

    def process(record: int) -> int:
        if record == 1:
            release_second.wait()
        elif record == 8:
            started_ninth.set()
        return record

    def consume() -> list[int]:
        return list(_parallel(process, records, workers=2))

    with ThreadPoolExecutor(max_workers=1) as consumer:
        results = consumer.submit(consume)
        try:
            assert started_ninth.wait(timeout=5)
        finally:
            release_second.set()
        assert results.result(timeout=5) == list(records)
