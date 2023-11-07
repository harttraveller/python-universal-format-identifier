from pathlib import Path
from loguru import logger
from typing import Optional, Union
from pydantic import BaseModel, field_validator
from pufi.env import cats, exts


class DataFormat(BaseModel):
    name: str

    # @field_validator("name")
    # def __validate_name(cls, name: str) -> str:
    #     if name not in FORMATS:
    #         raise ValueError("unknown file format")
    #     return name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class ResolutionResult(BaseModel):
    success: bool
    dformat: DataFormat


class Resolver:
    def __init__(self):
        pass


# def resolve_via_loc(loc: Union[str, Path], val: bool) -> ResolutionResult:
#     if "." in loc:
#         extension = loc.split(".")[-1].lower()
#         if extension in FORMATS:
#             return ResolutionResult(success=True, dformat=DataFormat(name=extension))
#         else:
#             return ResolutionResult(success=False, dformat="unknown")
#     else:
#         raise NotImplementedError(
#             "Could not resolve from file extension, would need to read in file "
#             "to resolve from binary, but this feature is currently unimplemented."
#         )


def resolve_via_uri(uri: str) -> ResolutionResult:
    # check if actually uri
    pass


def resolve_via_raw(raw: str) -> ResolutionResult:
    pass


def resolve_via_bin(bin: bytes) -> ResolutionResult:
    pass


def resolve(
    raw: Optional[str] = None,
    bin: Optional[bytes] = None,
    loc: Optional[Union[str, Path]] = None,
    uri: Optional[str] = None,
    val: bool = False,
) -> DataFormat:
    if val:
        raise NotImplementedError(
            "Reading in the resource to check it is not yet supported, "
            "you should read it in and pass the text or binary data to this function."
        )
    # check if appropriate params have been passed in
    if all([raw is None, bin is None, loc is None, uri is None]):
        raise ValueError("You must pass an argument to at least one of the parameters.")
    # assess if the path or uri
    # todo: if val, run all, compare results
    # if loc is not None:
    #     loc_resolution_attempt = resolve_via_loc(loc=loc, val=val)
    #     if loc_resolution_attempt.success:
    #         # todo: if val, doublecheck by reading in
    #         return loc_resolution_attempt.dformat
    if uri is not None:
        uri_resolution_attempt = resolve_via_uri(uri=uri)
        if uri_resolution_attempt.success:
            # todo: if val, doublecheck by retrieving from web
            return uri_resolution_attempt.dformat
    if raw is not None:
        raw_resolution_attempt = resolve_via_raw(raw=raw)
        if raw_resolution_attempt.success:
            return raw_resolution_attempt.dformat
    if bin is not None:
        bin_resolution_attempt = resolve_via_bin(bin=bin)
        if bin_resolution_attempt.success:
            return bin_resolution_attempt.dformat
    # todo: check to make sure there are no dataformats called 'unknown'
    return "unknown"
