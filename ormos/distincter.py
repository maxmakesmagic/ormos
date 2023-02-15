#!/usr/bin/env python3

import argparse
from datetime import datetime
import hashlib
import json
import logging
import os
from pathlib import Path
import sys
from typing import Generator, List

# Import database items
from ormos.database import orm, Scraped, DistinctPage, db, url_hash

log = logging.getLogger(__name__)


class MakeDistinct:
    def __init__(self):
        pass

    def process(self):
        log.info("Starting search")

        with orm.db_session:
            orm.sql_debug(True)
            items = orm.select(s for s in Scraped)
            total = items.count()
            orm.sql_debug(False)

            for index, scraped in enumerate(items):  # type: Generator[Scraped]
                ident = f"{index+1}/{total}"

                log.debug("[%s] Processing Scraped %s", ident, scraped)

                # Have we already ingested this?
                hashed_url = url_hash(scraped.url)

                r = DistinctPage.get(hash_url=hashed_url)
                if r:
                    log.debug("[%s] Distinct already exists: %s", ident, r)
                    continue

                distinctpage = DistinctPage(
                    hash_url=hashed_url, url=scraped.url, scraped=scraped
                )

                log.info("[%s] Created Distinct: %s", ident, distinctpage)


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

    converter = MakeDistinct()
    converter.process()
