


from fastapi import APIRouter, Depends

from api.ai.search.validators import SearchQueryParams, SearchResponse
from app.qa import retriever, answers

router = APIRouter(
    prefix="/api/ai/search",
    tags=["Search"]
)

@router.get("/", response_model=SearchResponse)
def search(query_params: SearchQueryParams = Depends()):
    results = retriever.search(query_params.question)
    response = answers.doAnswer(query_params.question, results)

    return SearchResponse(question=query_params.question, answer=response.content)