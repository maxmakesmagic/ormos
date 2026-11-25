"""Read one NDJSON file from a pull request artifact."""

import argparse
from pathlib import Path
from shutil import copyfileobj
from zipfile import ZipFile

CANDIDATE_FILENAME = "candidate.ndjson"
MAX_INVENTORY_BYTES = 1024**3


def main() -> None:
    """Copy the expected inventory to a fixed local path."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("download", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    files = list(args.download.iterdir())
    if len(files) != 1 or not files[0].is_file() or files[0].is_symlink():
        parser.error("Expected one candidate inventory archive")

    with ZipFile(files[0]) as artifact:
        if artifact.namelist() != [CANDIDATE_FILENAME]:
            parser.error("Expected only candidate.ndjson in the archive")
        member = artifact.getinfo(CANDIDATE_FILENAME)
        if member.file_size > MAX_INVENTORY_BYTES:
            parser.error("The candidate inventory exceeds 1 GiB")
        with artifact.open(member) as source, args.output.open("xb") as output:
            copyfileobj(source, output)


if __name__ == "__main__":
    main()
