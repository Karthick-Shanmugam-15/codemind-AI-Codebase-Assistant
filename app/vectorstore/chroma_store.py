from typing import Any

from chromadb import Collection

from app.config.app_config import AppConfig
from app.embeddings.validators import EmbeddingResult
from app.registry import instances


def get_collection(repo_name: str) -> Collection:
    return instances.get_chroma_client().get_or_create_collection(name=repo_name)

def store_embeddings(app_config: AppConfig, embedding_results: list[EmbeddingResult]) -> None:
    collection = get_collection(app_config.repo_name)

    ids: list[str] = []
    embeddings: list[list[float]] = []
    metadatas: list[dict[str, Any]] = []

    for result in embedding_results:
        ids.append(result.id)
        embeddings.append(result.vector)
        metadatas.append(result.metadata)

    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas
    )