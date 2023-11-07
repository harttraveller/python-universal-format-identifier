from pathlib import Path


HOME = Path.home()
CACHE = HOME / ".pufi"

CATEGORIES_LOCAL = CACHE / "categories.json"
EXTENSIONS_LOCAL = CACHE / "extensions.json"
CATEGORIES_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/categories.json"
)
EXTENSIONS_URL = (
    "https://github.com/dyne/file-extension-list/raw/master/pub/extensions.json"
)
