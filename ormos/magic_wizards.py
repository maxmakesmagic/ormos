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

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from ormos.imagecache import db, ImageCache

log = logging.getLogger(__name__)


class MagicWizardsConverterSingle:
    def __init__(self, path: Path, identifier: str, image_cache: Optional[ImageCache] = None):
        self.path = path
        self.identifier = identifier
        self.cache = {}
        self.image_cache = image_cache if image_cache else ImageCache()

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
        self.view_url = wayback_data["record"]["view_url"]

        # Start a metadata dictionary, which can be added to.
        self.metadata = {
            "wayback_url": self.url,
            "wayback_raw_url": self.raw_url,
            "wayback_capture_timestamp": wayback_data["record"]["time"]
        }

        # Calculate the wayback prefix for images
        m = re.match(r'^(https://web.archive.org/web/[^/]+)', wayback_data["record"]["view_url"])
        if m:
            self.image_prefix = f"{m.group(1)}im_"
            log.debug("[%s] Wayback prefix is %s", self.identifier, self.image_prefix)
        else:
            self.image_prefix = None

        # Calculate the archive path
        self.archive_path = self.generate_path(self.url)


    # Converts HTML content into Markdown content
    def process_html(self, path: Path) -> Optional[str]:
        log.info("[%s] Processing HTML path: %s", self.identifier, path)
        with open(path, "rb") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Store off some metadata if it exists.
        for tag in soup.find_all("meta"):
            name = tag.get("name", None)
            if name in ["generator", "description"]:
                self.metadata[name] = tag.get("content", "")

        # Content can be in one of several places.
        #
        # <div id="main-content">
        # <div id="main">
        main_content = soup.find("div", id="main-content")
        if not main_content:
            main_content = soup.find("div", id="main")

        # Check the main content again. If it's not present this is probably not an article.
        if not main_content:
            if soup.find("article"):
                raise Exception("Found an <article> not inside content")

            # Assume not an article. Check later.
            log.error("[%s] Not an article", self.identifier)
            return None

        # Remove content that isn't necessary
        #
        # Remove breadcrumb links
        for bc in main_content.find_all(id="breadcrumb"):
            bc.decompose()

        # Remove author links (Bio, Archive)
        for p_class in ["links"]:
            for p in main_content.find_all("p", class_=p_class):
                p.decompose()
        for s_class in ["links"]:
            for s in main_content.find_all("span", class_=s_class):
                s.decompose()

        # Remove in-body styles and scripts
        for tagtype in ["style", "script"]:
            for tag in main_content.find_all(tagtype):
                tag.decompose()

        # Remove sharing links and the article footer
        # Also remove sample hands
        for div_class in ["sharing", "article-footer", "data-sample-hand-cards", "toggle-samplehand"]:
            for ds in main_content.find_all("div", class_=div_class):
                ds.decompose()

        # Convert iframes to hyperlinks
        for iframe in main_content.find_all("iframe"):
            if "src" in iframe.attrs:
                new_a = soup.new_tag("a")
                new_a.attrs["href"] = iframe.attrs["src"]
                new_a.string = iframe.attrs["src"]
                iframe.replace_with(new_a)

        # Verify that any images exist; and if they don't, then
        # try and replace them with a Wayback URL.
        for img in main_content.find_all("img"):
            if "src" in img.attrs:
                new_src = self.image_cache.verified_image(img.attrs["src"], self.identifier, self.image_prefix)
                img.attrs["src"] = new_src
            else:
                # Image is weird. One example seen: <img style="magic">
                img.decompose()

        # Convert the remainder into Markdown
        mc = MarkdownConverter().convert_soup(main_content)

        # log.debug("Markdown content: %s", mc)
        return mc


    # Generates a path for this content in the archive
    def generate_path(self, url: str) -> Path:
        parts = urlparse(url)
        log.debug("[%s] URL parts: %s", self.identifier, parts)

        # URL-unquote the path, and remove any slashes from the
        # front or end.
        noleading = unquote(parts.path.strip("/"))

        # At this point we can try and extract the path from the URL.
        m = re.match(r'^(.*?)([^/]+-(\d{4})-(\d{2})-(\d{2})(:?-\d)?)$', noleading)
        if m:
            path = Path("archive",
                        m.group(1),
                        m.group(3),
                        m.group(4),
                        f"{m.group(2)}.md")

            self.metadata["publish_date"] = f"{m.group(3)}-{m.group(4)}-{m.group(5)}"
        else:
            path = Path("archive", f"{noleading}.md")

        log.debug("[%s] Generated path: %s", self.identifier, path)
        parent = path.parent
        os.makedirs(parent, exist_ok=True)
        return path

    def process(self):
        # Check to see if the path already exists
        if self.archive_path.exists():
            log.warning("[%s] Path already exists: %s", self.identifier, self.archive_path)

        # Process the HTML into Markdown
        markdown = self.process_html(self.html_path)
        if markdown:
            # Write out the Markdown.
            with open(self.archive_path, "w", encoding="utf-8") as f:
                f.write("\n---\n")
                # Write the link to the Wayback page
                f.write(f"[Link to Wayback Machine]({self.view_url})\n\n")

                # Add the metadata as Markdown metadata at the start of the file
                for key, value in self.metadata.items():
                    escvalue = value.replace('"','`')
                    f.write(f"[_metadata_:{key}]:- \"{escvalue}\"\n")
                f.write("---\n")
                f.write(markdown)


class MagicWizardsConverterMany:
    SEARCH_TERM_BASE = "magic_wizards_com"

    def __init__(self, path: Path, search_term: Optional[str] = None):
        self.search_term = search_term if search_term else self.SEARCH_TERM_BASE
        self.path = path
        self.cache_path = Path(f"{self.search_term}.json")
        self.image_cache = ImageCache()

    def get_dirs(self) -> List[Path]:
        if not self.cache_path.exists():
            directories = []  # type: List[Path]
            for (index, listing) in enumerate(self.path.iterdir()):
                if self.search_term in listing.name:
                    to_process = self.path / listing
                    log.debug("[%d] Adding listing %s", index, to_process)
                    directories.append(to_process)
            with open(self.cache_path, "w", encoding="utf-8") as f:
                json.dump([d.as_posix() for d in directories], f)
        else:
            with open(self.cache_path, "rb") as f:
                directory_paths = json.load(f)
                directories = [Path(d) for d in directory_paths]

        return directories

    def process(self):
        log.info("Starting search")
        directories_to_process = self.get_dirs()
        total = len(directories_to_process)
        log.info("Processing %d entries", total)

        for (index, directory) in enumerate(directories_to_process):
            log.debug("[%d/%d] Processing %s", index+1, total, directory)
            # Just pick a directory out of the subfolder for now
            for content_dir in directory.iterdir():
                content_full = directory / content_dir
                if content_full.is_dir():
                    # At least one content directory! Process it.
                    log.info("[%d/%d] Processing %s", index+1, total, content_full)
                    single = MagicWizardsConverterSingle(content_full, f"{index+1}/{total}", image_cache=self.image_cache)
                    single.process()
                    break

if __name__ == "__main__":
    streamhandler = logging.StreamHandler(stream=sys.stdout)
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s"))
    filehandler = logging.FileHandler(filename="magic_wizards.log", mode="w")
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5.5s %(message)s"))

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

    parser = argparse.ArgumentParser()
    parser.add_argument("--content", type=lambda p: Path(p).absolute(), help="Directory with all previously scraped content")
    parser.add_argument("--single", type=lambda p: Path(p).absolute(), help="Path to directory containing HTML+JSON files")
    parser.add_argument("--searchterm", help="override default search term")

    args = parser.parse_args()

    if args.content and not args.content.exists():
        raise Exception("Content folder does not exist!")

    if args.single and not args.single.exists():
        raise Exception("Single content folder does not exist!")

    if args.content:
        converter = MagicWizardsConverterMany(args.content, search_term=args.searchterm)
        converter.process()
    elif args.single:
        converter = MagicWizardsConverterSingle(args.single, "1/1")
        converter.process()
