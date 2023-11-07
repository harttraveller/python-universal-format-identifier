from pathlib import Path
from urllib.request import urlretrieve


CACHE = Path.home() / ".pufi"

CATEGORIES_LOCAL = CACHE / "categories.json"
EXTENSIONS_LOCAL = CACHE / "extensions.json"
CATEGORIES_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/categories.json"
)
EXTENSIONS_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/extensions.json"
)

# ensure that package resource files are available
if not CACHE.exists():
    CACHE.mkdir()
if not CATEGORIES_LOCAL.exists():
    urlretrieve(CATEGORIES_URL, CATEGORIES_LOCAL)
if not EXTENSIONS_LOCAL.exists():
    urlretrieve(EXTENSIONS_URL, EXTENSIONS_LOCAL)
