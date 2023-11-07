import json
from pathlib import Path
from loguru import logger as log
from typing import Union
from urllib.error import URLError
from urllib import request
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


# todo: move to sep micropkg
class InternetUnavailableError(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return f"Internet connection required for {self.reason}"


def require_internet(reason: str, check: str = "https://www.google.com"):
    try:
        _ = request.urlopen(check)
    except URLError:
        raise InternetUnavailableError(reason=reason)


# ! DYNAMIC

# * ensure that cache dir exists and create if not
if not PUFI_CACHE.exists():
    log.warning(f"A {str(PUFI_CACHE)} directory is needed to cache package data in")
    PUFI_CACHE.mkdir()
    log.info(f"Created {str(PUFI_CACHE)} cache directory")


# todo: move to sep micropkg
def cache_file(path: Union[str, Path], source: str, backup: str) -> None:
    path = Path(path)
    if not path.exists():
        log.warning(f"Could not find {str(path)} file")
        require_internet(reason=f"downloading {source}")
        try:
            download(source, path)
            log.info(f"Downloaded {source} to {str(path)}")
        except URLError:
            log.error(f"Attempt to retrieve {source} failed, trying {backup}")
            try:
                download(backup, path)
                log.info(f"Downloaded {backup} to {str(path)}")
            except:
                raise Exception("Could not download required package resource files.")


# * ensure categories data cached and download if not
cache_file(path=CATEGORIES_LOCAL, source=CATEGORIES_URL, backup=CATEGORIES_URL_BACKUP)


# * ensure extensions data cached and download if not
cache_file(path=EXTENSIONS_LOCAL, source=EXTENSIONS_URL, backup=EXTENSIONS_URL_BACKUP)

# * load categories data
with open(CATEGORIES_LOCAL) as categories_file:
    CATEGORIES = cats = json.loads(categories_file.read())
categories_file.close()

# * load extensions data
with open(EXTENSIONS_LOCAL) as extensions_file:
    EXTENSIONS = exts = json.loads(extensions_file.read())
extensions_file.close()
