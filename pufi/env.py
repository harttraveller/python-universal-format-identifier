import json
from pathlib import Path
from urllib.request import urlretrieve


PUFI_CACHE = Path.home() / ".pufi"

CATEGORIES_LOCAL = PUFI_CACHE / "categories.json"
EXTENSIONS_LOCAL = PUFI_CACHE / "extensions.json"
CATEGORIES_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/categories.json"
)
EXTENSIONS_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/extensions.json"
)

# ensure that package resource files are available
if not PUFI_CACHE.exists():
    PUFI_CACHE.mkdir()
if not CATEGORIES_LOCAL.exists():
    urlretrieve(CATEGORIES_URL, CATEGORIES_LOCAL)
if not EXTENSIONS_LOCAL.exists():
    urlretrieve(EXTENSIONS_URL, EXTENSIONS_LOCAL)
