import json
from pathlib import Path
from loguru import logger as log
from urllib.request import urlretrieve as download

# * default cache location
PUFI_CACHE = Path.home() / ".pufi"

# * local cached category/extension data
CATEGORIES_LOCAL = PUFI_CACHE / "categories.json"
EXTENSIONS_LOCAL = PUFI_CACHE / "extensions.json"

# * category/extension data source
CATEGORIES_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/categories.json"
)
EXTENSIONS_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/extensions.json"
)

# ensure that package resource files are available
# todo: add logging messages
if not PUFI_CACHE.exists():
    log.warning(f"A {str(PUFI_CACHE)} directory is needed to cache package data in")
    PUFI_CACHE.mkdir()
    log.info(f"Created {str(PUFI_CACHE)} cache directory")
if not CATEGORIES_LOCAL.exists():
    log.warning(f"Could not find {str(CATEGORIES_LOCAL)} file")
    try:
        download(CATEGORIES_URL, CATEGORIES_LOCAL)
        log.info(f"Downloaded {str(CATEGORIES_LOCAL)} from {CATEGORIES_URL}")
    except:
        pass
if not EXTENSIONS_LOCAL.exists():
    download(EXTENSIONS_URL, EXTENSIONS_LOCAL)

with open(CATEGORIES_LOCAL) as categories_file:
    CATEGORIES = cats = json.loads(categories_file.read())
categories_file.close()

with open(EXTENSIONS_LOCAL) as extensions_file:
    EXTENSIONS = exts = json.loads(extensions_file.read())
extensions_file.close()
