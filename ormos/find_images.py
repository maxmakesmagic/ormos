#!/usr/bin/env python3

import argparse
import json
import logging
import os
from pathlib import Path
import re
import sys
from typing import List, Optional
from urllib.parse import urlparse, unquote

from ormos.imagecache import db, ImageCache


from pony import orm
import requests
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
    cache.wayback_failures()
