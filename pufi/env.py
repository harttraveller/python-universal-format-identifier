from pydantic import BaseModel, field_validator

FORMATS = {
    "txt",
}

FORMATS_TODO = {
    "html",
    "json",
    "csv",
    "xml",
    "yaml",
    "rss",
    "atom",
    "js",
    "rdf",
    "tsv",
    "text",
    "plain",
    "md",
    "ini",
    "toml",
    "vcf",
    "ics",
    "xhtml",
    "svg",
    "jsonld",
    "protobuf",
    "edi",
    "srt",
    "vtt",
}


class DataFormat(BaseModel):
    name: str

    @field_validator("name")
    def __validate_name(cls, name: str) -> str:
        if name not in FORMATS:
            raise ValueError("unknown file format")
        return name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
