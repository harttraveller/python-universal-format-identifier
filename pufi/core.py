from pathlib import Path
from typing import Optional, Union
from pydantic import BaseModel, field_validator
from pufi.vars import cats, exts, extset


class DataFormat(BaseModel):
    extension: str

    @field_validator("extension")
    def __validate_name(cls, extension: str) -> str:
        if extension not in extset:
            raise ValueError("unknown file format")
        return extension

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


def resolve_via_path(path: Union[str, Path], val: bool) -> ResolutionResult:
    if "." in path:
        extension = path.split(".")[-1].lower()
        if extension in extset:
            return ResolutionResult(success=True, dformat=DataFormat(name=extension))
        else:
            return ResolutionResult(success=False, dformat="unknown")
    else:
        raise NotImplementedError(
            "Could not resolve from file extension, would need to read in file "
            "to resolve from binary, but this feature is currently unimplemented."
        )


def resolve_via_uri(uri: str) -> ResolutionResult:
    # check if actually uri
    pass


def resolve_via_text(text: str) -> ResolutionResult:
    pass


def resolve_via_bin(bin: bytes) -> ResolutionResult:
    pass


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
    # todo: if val, run all, compare results
    if path is not None:
        loc_resolution_attempt = resolve_via_path(path=path, val=check)
        if loc_resolution_attempt.success:
            # todo: if val, doublecheck by reading in
            return loc_resolution_attempt.dformat
    if uri is not None:
        uri_resolution_attempt = resolve_via_uri(uri=uri)
        if uri_resolution_attempt.success:
            # todo: if val, doublecheck by retrieving from web
            return uri_resolution_attempt.dformat
    if text is not None:
        raw_resolution_attempt = resolve_via_text(text=text)
        if raw_resolution_attempt.success:
            return raw_resolution_attempt.dformat
    if bin is not None:
        bin_resolution_attempt = resolve_via_bin(bin=bin)
        if bin_resolution_attempt.success:
            return bin_resolution_attempt.dformat
    # todo: check to make sure there are no dataformats called 'unknown'
    return "unknown"
