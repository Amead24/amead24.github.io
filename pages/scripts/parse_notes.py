import json
import logging
import os
import sys
from pathlib import Path
from typing import List

import bs4
from bs4 import BeautifulSoup as bs
from fire import Fire

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

INPUT_DIR: Path = Path("obsidian/book_reviews/")
OUTPUT_KEYS: List[str] = ["title", "subtitle", "thumbnail", "content"]
OUTPUT_PATH: Path = "pages/public/book_reviews.json"


def clean(tag: bs4.element.Tag) -> str:
    return tag.text.strip()


def parse(fn: str, markdown: str, keys: List[str] = None) -> dict:
    try:
        data = {key: clean(getattr(markdown, key)) for key in keys}
        logger.info(f"Successfully parsed: {fn}")
        return data

    except:
        logger.info(f"Malformed template: {fn}")


def convert(
    file_name: str = None,
    dir_name: str = INPUT_DIR,
    output_path: str = OUTPUT_PATH,
    keys: List[str] = None,
) -> None:
    """conversion of book review template into json file for GH pages

    python parse_notes.py -f example.md -o example.json
    """
    if file_name is not None:
        files = [file_name]

    else:
        dir_name = Path(dir_name) if dir_name else INPUT_DIR
        files = [dir_name / f for f in os.listdir(dir_name) if f.endswith(".md")]

    keys = OUTPUT_KEYS if keys is None else keys
    logger.info(f"Parsing files...")
    json_dicts = [parse(f, bs(open(f, "r"), "html.parser"), keys) for f in files]
    json.dump([jd for jd in json_dicts if jd is not None], open(output_path, "w"))
    logger.info(f"Done - Writing output to: {output_path}")


if __name__ == "__main__":
    Fire(convert)
