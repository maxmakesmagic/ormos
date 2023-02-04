#!/usr/bin/env python3

import argparse
import json
import logging
import os
from pathlib import Path
import re
import sys

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

log = logging.getLogger(__name__)

# Converts HTML content into Markdown content
def process_html(path: Path) -> str:
    log.info("Processing HTML path: %s", path)
    with open(path, "rb") as f:
        soup = BeautifulSoup(f, "html.parser")

    # The article content starts in <div id="main-content">
    main_content = soup.find(id="main-content")

    # Remove content that isn't necessary
    #
    # Remove breadcrumb links
    for bc in main_content.find_all(id="breadcrumb"):
        bc.decompose()

    # Remove author links (Bio, Archive)
    for p_class in ["links"]:
        for p in main_content.find_all("p", class_=p_class):
            p.decompose()

    # Remove sharing links and the article footer
    for div_class in ["sharing", "article-footer"]:
        for ds in main_content.find_all("div", class_=div_class):
            ds.decompose()

    # Convert iframes to hyperlinks
    for iframe in main_content.find_all("iframe"):
        new_a = soup.new_tag("a")
        new_a.attrs["href"] = iframe.attrs["src"]
        new_a.string = iframe.attrs["src"]

        iframe.replace_with(new_a)

    # Convert the remainder into Markdown
    mc = MarkdownConverter().convert_soup(main_content)

    log.debug("Markdown content: %s", mc)
    return mc


# Generates a path for this content in the archive
def generate_path(url: str) -> Path:
    m = re.match(r'^http[s]?://magic.wizards.com/en/articles/archive/(.*)$', url)
    if m:
        url_path = f"{m.group(1)}.md"
        path = Path("archive", url_path)
        log.debug("Generated path: %s", path)
        parent = path.parent
        os.makedirs(parent, exist_ok=True)
        return path

    raise Exception(f"Cannot generate path from URL {url}")

def process_single(path: Path):
    log.info("Processing path: %s", path)

    # Within this path there should be two files:
    # - an HTML file containing the content
    # - and a JSON file containing Wayback metadata
    html_files = [f for f in path.iterdir() if f.suffix == ".html"]
    json_files = [f for f in path.iterdir() if f.suffix == ".json"]
    log.debug("Paths: html %s json %s", html_files, json_files)

    if not html_files or not json_files:
        raise Exception("Expected both HTML and JSON")

    html_path = html_files[0]
    json_path = json_files[0]

    # Read in the JSON file.
    with open(json_path, "rb") as f:
        wayback_data = json.load(f)
    url = wayback_data["record"]["url"]
    raw_url = wayback_data["record"]["raw_url"]

    # Process the HTML into Markdown
    markdown = process_html(html_path)

    # Add the wayback data as Markdown metadata at the start of the file
    metadata = f'''
---
[_metadata_:wayback_url]:- "{url}"
[_metadata_:wayback_raw_url]:- "{raw_url}"
---
'''

    # Calculate the archive path
    path = generate_path(url)

    # Write out the Markdown.
    with open(path, "w", encoding="utf-8") as f:
        f.write(metadata)
        f.write(markdown)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stdout, format="%(asctime)s %(message)s", level=logging.DEBUG
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--content", type=lambda p: Path(p).absolute(), help="Directory with all previously scraped content")
    parser.add_argument("--single", type=lambda p: Path(p).absolute(), help="Path to directory containing HTML+JSON files")

    args = parser.parse_args()

    if args.content and not args.content.exists():
        raise Exception("Content folder does not exist!")

    if args.single and not args.single.exists():
        raise Exception("Single content folder does not exist!")

    if args.single:
        process_single(args.single)
