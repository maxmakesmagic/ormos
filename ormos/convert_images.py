#!/usr/bin/env python3

import json
import logging
import os
import sys

from ormos.database import orm, db, ImageUrl, ImageUrl2, url_hash

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

    with orm.db_session:
        for index, image in enumerate(orm.select(i for i in ImageUrl)):
            log.info("Process image %d %s", index, image)
            image2 = ImageUrl2(
                hash_input_url=url_hash(image.input_url),
                input_url=image.input_url,
                output_url=image.output_url,
                strategy=image.strategy,
            )
