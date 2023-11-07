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
CATEGORIES_URL_BACKUP = "https://github.com/harttraveller/python-universal-format-identifier/raw/main/file/categories.json"
EXTENSIONS_URL_BACKUP = "https://github.com/harttraveller/python-universal-format-identifier/raw/main/file/extensions.json"


# ! DYNAMIC


# * ensure that cache dir exists and create if not
if not PUFI_CACHE.exists():
    log.warning(f"A {str(PUFI_CACHE)} directory is needed to cache package data in")
    PUFI_CACHE.mkdir()
    log.info(f"Created {str(PUFI_CACHE)} cache directory")

# * ensure categories data cached and download if not
if not CATEGORIES_LOCAL.exists():
    log.warning(f"Could not find {str(CATEGORIES_LOCAL)} file")
    try:
        download(CATEGORIES_URL, CATEGORIES_LOCAL)
        log.info(f"Downloaded {CATEGORIES_URL} to {str(CATEGORIES_LOCAL)}")
    except Exception as exc:
        # todo: raise exception if no network connectivity
        raise exc

# * ensure extensions data cached and download if not
if not EXTENSIONS_LOCAL.exists():
    log.warning(f"Could not find {str(EXTENSIONS_LOCAL)} file")
    try:
        download(EXTENSIONS_URL, EXTENSIONS_LOCAL)
        log.info(f"Downloaded {EXTENSIONS_URL} to {str(EXTENSIONS_LOCAL)}")
    except Exception as exc:
        # todo: raise exception if no network connectivity
        raise exc

# * load categories data
with open(CATEGORIES_LOCAL) as categories_file:
    CATEGORIES = cats = json.loads(categories_file.read())
categories_file.close()

# * load extensions data
with open(EXTENSIONS_LOCAL) as extensions_file:
    EXTENSIONS = exts = json.loads(extensions_file.read())
extensions_file.close()
