from __future__ import annotations

from pydantic import BaseModel

from app import ingestion
from app.utils.id_generator import generate_id


class FileMetadata(BaseModel):
    file_path: str
    content: str

    def get_content_bytes(self: FileMetadata) -> bytes:
        return self.content.encode("utf-8")

class ParsedUnit(BaseModel):
    file_path: str
    type: str        # "class", "method", "interface", "constructor"
    name: str
    class_name: str
    content: str
    start_line: int
    end_line: int
    method_parameters: str = ""

    @property
    def id(self) -> str:
        return generate_id(
            self.file_path,
            self.class_name,
            self.name,
            self.type,
            self.method_parameters
        )