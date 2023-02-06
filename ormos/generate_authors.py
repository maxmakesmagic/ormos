#!/usr/bin/python3

import logging
import os
from pathlib import Path
import re
import sys


log = logging.getLogger(__name__)


AUTHOR_REX = re.compile(r'\[\_metadata\_\:author\]\:\- "([^"]+)"')
TITLE_REX = re.compile(r'\[\_metadata\_\:title\]\:\- "([^"]+)"')
DATE_REX = re.compile(r'\[\_metadata\_\:publish_date\]\:\- "([^"]+)"')


def process_path(path: Path, author_dict):
    with open(path, "r", encoding="utf-8") as f:
        prelude = f.read(4096)
        m = AUTHOR_REX.search(prelude)
        if not m:
            log.error("[%s] No author found", path)
            log.debug("Prelude: %s", prelude)
            return

        author = m.group(1).strip()

        m = TITLE_REX.search(prelude)
        if m:
            title = m.group(1)
        else:
            title = str(path)

        m = DATE_REX.search(prelude)
        if m:
            date = m.group(1)
        else:
            date = "Unknown"

        if author not in author_dict:
            author_dict[author] = {}

        # Create a slash-path for the content
        slashpath = f"/{path}"

        if slashpath not in author_dict[author]:
            author_dict[author][slashpath] = {}

        author_dict[author][slashpath]["title"] = title
        author_dict[author][slashpath]["date"] = date

        log.debug("Adding mapping: %s => %s", author, author_dict[author][slashpath])


def main():
    author_dict = {}
    author_dir = "by-author"

    # Find all the markdown files in archive/, and generate author pages in authors/
    for root, _dirs, files in os.walk("archive"):
        for file in files:
            if file.endswith(".md"):
                path = Path(root, file)
                process_path(path, author_dict)

    os.makedirs(author_dir, exist_ok=True)

    for author, articles in author_dict.items():
        path = Path(author_dir, f"{author}.md")
        with open(path, "w", encoding="utf-8") as f:
            # Let's write a simple Markdown file.
            f.write(f"# Articles by {author}\n\n")
            for date, title, slashpath in sorted(
                [
                    (d["date"], d["title"], slashpath)
                    for slashpath, d in articles.items()
                ]
            ):
                f.write(f"* [{title}]({slashpath}) - {date}\n")


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

    root_logger = logging.getLogger()
    root_logger.addHandler(streamhandler)
    root_logger.addHandler(filehandler)
    root_logger.setLevel(logging.DEBUG)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    main()
