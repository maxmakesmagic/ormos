#!/usr/bin/env python3

import argparse
import json
import logging
import os
from pathlib import Path
import re
import sys
from typing import Optional

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
import requests

log = logging.getLogger(__name__)


class MagicWizardsConverterSingle:
    def __init__(self, path: Path):
        self.path = path

        # Within this path there should be two files:
        # - an HTML file containing the content
        # - and a JSON file containing Wayback metadata
        html_files = [f for f in self.path.iterdir() if f.suffix == ".html"]
        json_files = [f for f in self.path.iterdir() if f.suffix == ".json"]
        log.debug("Paths: html %s json %s", html_files, json_files)

        if not html_files or not json_files:
            raise Exception("Expected both HTML and JSON")

        self.html_path = html_files[0]
        self.json_path = json_files[0]

        # Read in the JSON file.
        with open(self.json_path, "rb") as f:
            wayback_data = json.load(f)
        self.url = wayback_data["record"]["url"]
        self.raw_url = wayback_data["record"]["raw_url"]

        # Calculate the wayback prefix for images
        m = re.match(r'^(https://web.archive.org/web/[^/]+)', wayback_data["record"]["view_url"])
        if m:
            self.image_prefix = f"{m.group(1)}im_"
            log.debug("Wayback prefix is %s", self.image_prefix)
        else:
            self.image_prefix = None

    def image_url(self, img_src: str) -> Optional[str]:
        try:
            r = requests.head(img_src, allow_redirects=True, timeout=20)
            if r.status_code == 200:
                return r.url
        except:
            log.debug("Failed to find URL")

        return None

    def verified_image(self, img_src: str) -> str:
        # Best effort to get a working image.
        log.debug("Checking image: %s", img_src)
        checked_img_src = self.image_url(img_src)
        if checked_img_src:
            log.debug("Using image %s", checked_img_src)
            return checked_img_src

        # Image doesn't exist. Try checking the Wayback image.
        wayback_url = f"{self.image_prefix}/{img_src}"
        log.debug("Not found; checking wayback image: %s", wayback_url)
        if self.image_prefix:
            wayback_img = self.image_url(wayback_url)
            if wayback_img:
                log.debug("Using wayback image %s", wayback_img)
                return wayback_img

        # If in doubt, just return the original source.
        log.debug("Not found; using original %s", img_src)
        return img_src

    # Converts HTML content into Markdown content
    def process_html(self, path: Path) -> str:
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

        # Verify that any images exist; and if they don't, then
        # try and replace them with a Wayback URL.
        for img in main_content.find_all("img"):
            new_src = self.verified_image(img.attrs["src"])
            img.attrs["src"] = new_src

        # Convert the remainder into Markdown
        mc = MarkdownConverter().convert_soup(main_content)

        # log.debug("Markdown content: %s", mc)
        return mc


    # Generates a path for this content in the archive
    def generate_path(self, url: str) -> Path:
        m = re.match(r'^http[s]?://magic.wizards.com/en/articles/archive/(.*)$', url)
        if m:
            url_path = f"{m.group(1)}.md"
            path = Path("archive", url_path)
            log.debug("Generated path: %s", path)
            parent = path.parent
            os.makedirs(parent, exist_ok=True)
            return path

        raise Exception(f"Cannot generate path from URL {url}")

    def process(self):
        # Process the HTML into Markdown
        markdown = self.process_html(self.html_path)

        # Add the wayback data as Markdown metadata at the start of the file
        metadata = f'''
---
[_metadata_:wayback_url]:- "{self.url}"
[_metadata_:wayback_raw_url]:- "{self.raw_url}"
---
'''

        # Calculate the archive path
        path = self.generate_path(self.url)

        # Write out the Markdown.
        with open(path, "w", encoding="utf-8") as f:
            f.write(metadata)
            f.write(markdown)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stdout, format="%(asctime)s %(message)s", level=logging.DEBUG
    )
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    parser = argparse.ArgumentParser()
    parser.add_argument("--content", type=lambda p: Path(p).absolute(), help="Directory with all previously scraped content")
    parser.add_argument("--single", type=lambda p: Path(p).absolute(), help="Path to directory containing HTML+JSON files")

    args = parser.parse_args()

    if args.content and not args.content.exists():
        raise Exception("Content folder does not exist!")

    if args.single and not args.single.exists():
        raise Exception("Single content folder does not exist!")


    if args.single:
        converter = MagicWizardsConverterSingle(args.single)
        converter.process()
