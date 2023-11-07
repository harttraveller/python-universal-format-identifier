from urllib.request import urlretrieve
from pufi.env import (
    CACHE,
    CATEGORIES_LOCAL,
    CATEGORIES_URL,
    EXTENSIONS_LOCAL,
    EXTENSIONS_URL,
)


CACHE.mkdir(exist_ok=True)
if not CATEGORIES_LOCAL.exists():
    urlretrieve(CATEGORIES_URL, CATEGORIES_LOCAL)
