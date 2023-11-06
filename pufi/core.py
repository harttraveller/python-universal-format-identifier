from pathlib import Path
from typing import Optional, Union


def resolve(
    text: Optional[str] = None,
    bin: Optional[bytes] = None,
    path: Optional[Union[str, Path]] = None,
    uri: Optional[str] = None,
    check: bool = False,
):
    if check:
        raise NotImplementedError(
            "Reading in the resource to check it is not yet supported, "
            "you should read it in and pass the text or binary data to this function."
        )
