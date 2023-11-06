from pathlib import Path
from typing import Optional, Union

from pufi.env import DataFormat


def resolve(
    text: Optional[str] = None,
    bin: Optional[bytes] = None,
    path: Optional[Union[str, Path]] = None,
    uri: Optional[str] = None,
    check: bool = False,
) -> DataFormat:
    if check:
        raise NotImplementedError(
            "Reading in the resource to check it is not yet supported, "
            "you should read it in and pass the text or binary data to this function."
        )
    # check if appropriate params have been passed in
    if all([text is None, bin is None, path is None, uri is None]):
        raise ValueError("You must pass an argument to at least one of the parameters.")
    # assess if the path or uri
