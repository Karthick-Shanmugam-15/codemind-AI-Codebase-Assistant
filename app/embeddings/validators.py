from typing import Any

from pydantic import BaseModel


class EmbeddingResult(BaseModel):
    id: str
    vector: list[float]
    class_name: str
    metadata: dict[str, Any]
