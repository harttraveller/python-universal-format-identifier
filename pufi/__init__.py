from urllib.request import urlretrieve
from pufi.env import (
    CACHE,
    CATEGORIES_LOCAL,
    CATEGORIES_URL,
    EXTENSIONS_LOCAL,
    EXTENSIONS_URL,
)

if not CACHE.exists():
    CACHE.mkdir()
if not CATEGORIES_LOCAL.exists():
    urlretrieve(CATEGORIES_URL, CATEGORIES_LOCAL)
if not EXTENSIONS_LOCAL.exists():
    urlretrieve(EXTENSIONS_URL, EXTENSIONS_LOCAL)
