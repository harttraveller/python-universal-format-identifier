from pathlib import Path


HOME = Path.home()
CACHE = HOME / ".pufi"

LOC_CAT = CACHE / "categories.json"
LOC_EXT = CACHE / "extensions.json"
URL_CAT = "https://github.com/dyne/file-extension-list/raw/master/pub/categories.json"
URL_EXT = "https://github.com/dyne/file-extension-list/raw/master/pub/extensions.json"
