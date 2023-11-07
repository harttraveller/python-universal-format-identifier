from pydantic import BaseModel, field_validator

# from pufi.env import FORMATS


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
