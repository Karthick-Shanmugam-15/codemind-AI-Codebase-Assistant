from langchain_core.embeddings import Embeddings

from app.config.app_config import AppConfig
from app.qa.validators import SearchResult
from app.registry import instances
from app.registry.instances import get_app_config
from app.vectorstore.chroma_store import get_collection


def search(user_question: str):
    embedding_model: Embeddings = instances.get_embedder()

    question_vector: list[float] = embedding_model.embed_query(user_question)

    app_config: AppConfig = get_app_config()

    results = get_collection(app_config.repo_name).query(
        query_embeddings=[question_vector],
        n_results=get_app_config().top_k
    )

    search_results = []
    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]
        search_results.append(SearchResult(
            id=results["ids"][0][i],
            distance=results["distances"][0][i],
            class_name=metadata.get("class_name", ""),
            method_name=metadata.get("name", ""),
            file_path=metadata.get("file_path", ""),
            content=metadata.get("content", ""),
            type=metadata.get("type", ""),
        ))

    return search_results

