from urllib.request import urlretrieve
from pufi.variable import (
    CACHE,
    CATEGORIES_LOCAL,
    CATEGORIES_URL,
    EXTENSIONS_LOCAL,
    EXTENSIONS_URL,
)


# ensure that package resource files are available
if not CACHE.exists():
    CACHE.mkdir()
if not CATEGORIES_LOCAL.exists():
    urlretrieve(CATEGORIES_URL, CATEGORIES_LOCAL)
if not EXTENSIONS_LOCAL.exists():
    urlretrieve(EXTENSIONS_URL, EXTENSIONS_LOCAL)

from pufi.core import resolve
