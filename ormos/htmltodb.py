#!/usr/bin/env python3

import argparse
from datetime import datetime
import hashlib
import json
import logging
import os
from pathlib import Path
import sys
from typing import List

# Import database items
from .database import orm, Scraped, db

log = logging.getLogger(__name__)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def url_hash(url: str) -> str:
    m = hashlib.sha256()
    m.update(url.encode("utf-8"))
    return m.hexdigest()


class DbConverterMany:
    def __init__(self, paths: List[str]):
        self.paths = paths

    def get_list(self):
        if not os.path.exists("htmldb.json"):
            to_process = []
            counter = 0

            for path in self.paths:
                log.critical("Processing %s", path)
                for root, _dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".json"):
                            full_json = Path(root, file)
                            full_html = full_json.with_suffix(".html")
                            if full_json.exists() and full_html.exists():
                                to_process.append((full_json, full_html))
                                counter += 1
                                if counter % 1000 == 0:
                                    log.info("Queued %d articles", counter)

            with open("htmldb.json", "w", encoding="utf-8") as f:
                to_dump = [(str(x), str(y)) for x, y in to_process]
                json.dump(to_dump, f)
        else:
            with open("htmldb.json", "rb") as f:
                to_undump = json.load(f)
                to_process = [(Path(x), Path(y)) for x, y in to_undump]
        return to_process

    def process(self):
        log.info("Starting search")

        to_process = self.get_list()
        total = len(to_process)
        chunk_size = 1000

        # Get the existing URLs.
        # hashes = set()
        # with orm.db_session:
        #     for row in orm.select(c for c in Scraped):
        #         hashes.add(row.hash_raw_url)

        for chunk_id, chunk in enumerate(chunks(to_process, chunk_size)):
            log.info("Processing chunk: %s", f"{chunk_id+1}/{total/chunk_size}")
            with orm.db_session:
                for index, (full_json, full_html) in enumerate(chunk):
                    ident = f"{chunk_id+1}/{total/chunk_size}:{index+1}/{chunk_size}"

                    log.debug(
                        "[%s] Processing html %s json %s", ident, full_html, full_json
                    )

                    with open(full_json, "rb") as f:
                        data = json.load(f)
                        record = data["record"]

                    # Have we already ingested this?
                    raw_url = record["raw_url"]
                    hash_raw_url = url_hash(raw_url)

                    r = Scraped.get(hash_raw_url=hash_raw_url)
                    if r:
                        log.debug("[%s] Scraped already exists: %s", ident, r)
                        # # Let's archive the content.
                        # new_html_path = full_html.with_suffix(".htmldone")
                        # new_json_path = full_json.with_suffix(".jsondone")
                        # new_dir = os.path.dirname(new_html_path)
                        # os.makedirs(new_dir, exist_ok=True)

                        # log.debug("[%s] Moving HTML and JSON to %s", ident, new_dir)
                        # shutil.move(full_html, new_html_path)
                        # shutil.move(full_json, new_json_path)
                        # log.info("[%s] Moved HTML and JSON to %s", ident, new_dir)
                        continue

                    url = record["url"]
                    mime_type = record["mime_type"]
                    status_code = record["status_code"]
                    timestamp = datetime.strptime(record["time"], "%Y-%m-%d %H:%M:%S%z")
                    view_url = record["view_url"]

                    with open(full_html, "rb") as f:
                        html_content = f.read()

                    scraped = Scraped(
                        raw_url=raw_url,
                        hash_raw_url=hash_raw_url,
                        url=url,
                        mime_type=mime_type,
                        status_code=status_code,
                        time=timestamp,
                        view_url=view_url,
                        html_content=html_content,
                    )
                    log.info("[%s] Created scraped: %s", ident, scraped)


if __name__ == "__main__":
    streamhandler = logging.StreamHandler(stream=sys.stdout)
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )
    filehandler = logging.FileHandler(
        filename=f"{os.path.basename(__file__)}.log", mode="w"
    )
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )
    errorhandler = logging.FileHandler(
        filename=f"{os.path.basename(__file__)}_errors.log", mode="w"
    )
    errorhandler.setLevel(logging.ERROR)
    errorhandler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s")
    )
    root_logger = logging.getLogger()
    root_logger.addHandler(streamhandler)
    root_logger.addHandler(filehandler)
    root_logger.addHandler(errorhandler)
    root_logger.setLevel(logging.DEBUG)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Bind to the database
    with open("database.json", "rb") as f:
        creds = json.load(f)
    db.bind(**creds)
    db.generate_mapping(create_tables=True)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--content",
        action="append",
        help="Directory with all previously scraped content",
    )

    args = parser.parse_args()

    if args.content:
        converter = DbConverterMany(args.content)
        converter.process()
