from pydantic import BaseModel


class SearchResult(BaseModel):
    id: str
    distance: float
    class_name: str
    method_name: str
    file_path: str
    content: str
    type: str