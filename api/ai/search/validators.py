from pydantic import BaseModel


class SearchQueryParams(BaseModel):
    question: str
    top_k: int = 5

class SearchResponse(BaseModel):
    question: str
    answer: str | list[str | dict]
