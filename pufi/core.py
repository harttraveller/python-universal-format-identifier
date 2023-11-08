from pathlib import Path
from typing import Optional, Union
from pydantic import BaseModel, field_validator
from pufi.vars import exts


class DataFormat(BaseModel):
    extension: str

    def __str__(self) -> str:
        return self.extension

    def __repr__(self) -> str:
        return self.extension


class ResolutionResult(BaseModel):
    success: bool
    dformat: DataFormat


class Resolver:
    def __init__(self):
        pass


def resolve_loc(loc: Union[str, Path]) -> ResolutionResult:
    loc = str(loc)
    if "." in loc:
        extension = loc.split(".")[-1].lower()
        if extension in exts:
            return ResolutionResult(success=True, dformat=DataFormat(extension=extension))
        else:
            return ResolutionResult(
                success=False, dformat=DataFormat(extension="unknown")
            )


def resolve_binary(binary: bytes):
    pass


def resolve_text(text: str):
    pass


def resolve_raw(raw: Union[str, bytes]) -> ResolutionResult:
    pass


def resolve(
    raw: Optional[Union[str, bytes]] = None,
    loc: Optional[Union[str, Path]] = None,
) -> DataFormat:
    """
    raw: text
    loc: path (str/Path) or uri/url to resource
    """
    # check if appropriate params have been passed in
    if all([raw is None, loc is None]):
        raise ValueError("You must pass an argument to at least one of the parameters.")
    # assess if the path or uri
    # todo: if val, run all, compare results
    if loc is not None:
        loc_resolution_attempt = resolve_loc(loc=loc)
        if loc_resolution_attempt.success:
            # todo: if val, doublecheck by reading in
            return loc_resolution_attempt.dformat
    if raw is not None:
        raw_resolution_attempt = resolve_raw(raw=raw)
        if raw_resolution_attempt.success:
            return raw_resolution_attempt.dformat
    # todo: check to make sure there are no dataformats called 'unknown'
    return "unknown"
