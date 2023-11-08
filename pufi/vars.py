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
EXTENSIONS_LOCAL = PUFI_CACHE / "extensions.txt"

EXTENSIONS_URL = "https://github.com/harttraveller/python-universal-format-identifier/raw/main/file/extensions.txt"


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
def cache_file(path: Union[str, Path], url: str) -> None:
    path = Path(path)
    if not path.exists():
        log.warning(f"Could not find {str(path)} file")
        require_internet(reason=f"downloading {url}")
        try:
            download(url, path)
            log.info(f"Downloaded {url} to {str(path)}")
        except URLError:
            raise Exception("Could not download required package resource files.")


# * ensure extensions data cached and download if not
cache_file(path=EXTENSIONS_LOCAL, url=EXTENSIONS_URL)

# * load extensions data
with open(EXTENSIONS_LOCAL) as extensions_file:
    EXTENSIONS = exts = set(
        [i.strip() for i in extensions_file.read().split("\n") if i.strip() != ""]
    )
extensions_file.close()
