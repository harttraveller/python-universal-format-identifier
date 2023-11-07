from urllib.request import urlretrieve
from pufi.env import CACHE, LOC_CAT, LOC_EXT, WEB_CAT, WEB_EXT


CACHE.mkdir(exist_ok=True)
if not LOC_CAT.exists():
    urlretrieve(WEB_CAT, LOC_CAT)
