#!/usr/bin/env python3

import json
import logging
import os
import re
import sys
from typing import Generator

from ormos.database import orm, db, ImageUrl
from ormos.imagecache import ImageCache
import wayback

log = logging.getLogger(__name__)

if __name__ == "__main__":
    streamhandler = logging.StreamHandler(stream=sys.stdout)
    streamhandler.setLevel(logging.DEBUG)
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

    root_logger = logging.getLogger()
    root_logger.addHandler(streamhandler)
    root_logger.addHandler(filehandler)
    root_logger.setLevel(logging.DEBUG)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Bind to the database
    with open("database.json", "rb") as f:
        creds = json.load(f)

    db.bind(**creds)
    db.generate_mapping(create_tables=True)

    session = wayback.WaybackSession(retries=20)
    client = wayback.WaybackClient(session=session)
    cache = ImageCache()

    with orm.db_session:
        author_rex = re.compile(r"(authorpic_[^/]+)$")
        base_urls = [
            "https://media.magic.wizards.com/image_legacy_migration/magic/images/mtgcom/authorpics/",
            "http://media.wizards.com/legacy/magic/images/mtgcom/authorpics/",
            "https://media.magic.wizards.com/styles/auth_small/public/images/person/",
        ]

        authorpics = orm.select(
            i
            for i in ImageUrl
            if i.strategy in ["wayback", "failure"] and "authorpics" in i.input_url
        )  # type: Generator[ImageUrl]

        for pic in authorpics:
            log.info("Processing %s (%s)", pic.input_url, pic.strategy)
            m = author_rex.search(pic.input_url)
            if m:
                authorpic = m.group(1)
                log.info("Searching for: %s", authorpic)
                urls = [f"{u}{authorpic}" for u in base_urls]
                urls.extend([f"{u}{authorpic.lower()}" for u in base_urls])

                for url in urls:
                    log.info("Testing %s", url)
                    new_url = cache.image_url(url, authorpic)
                    if new_url:
                        log.info("[%s] Updating mapping => %s", authorpic, new_url)
                        pic.set(output_url=new_url, strategy="fixauthor")
                        break

        # for failure in failures:
        #     identifier = failure.input_url[-15:]
        #     log.info("[%s] Processing failed URL %s", identifier, failure.input_url)
        #     url = self.wayback_failure(failure.input_url, identifier=identifier)
        #     if url:
        #         # Update the database
        #         log.info("[%s] Updating mapping: => %s", identifier, url)
        #         failure.set(output_url=url, strategy="wayback2")
