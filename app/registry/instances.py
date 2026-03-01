from functools import lru_cache
import chromadb
from chromadb import ClientAPI
from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings, ChatOllama

from app.config.app_config import AppConfig


@lru_cache(maxsize=1)
def get_app_config() -> AppConfig:
    return AppConfig()


@lru_cache(maxsize=1)
def get_chroma_client() -> ClientAPI:
    return chromadb.PersistentClient(path=get_app_config().chroma_db_path)


@lru_cache(maxsize=1)
def get_embedder() -> Embeddings:
    app_config: AppConfig = get_app_config()
    return OllamaEmbeddings(
        model=app_config.embedding_model,
        base_url=app_config.ollama_base_url
    )


@lru_cache(maxsize=1)
def get_llm_model() -> ChatOllama:
    app_config: AppConfig = get_app_config()
    return ChatOllama(
        model=app_config.llm_model,
        base_url=app_config.ollama_base_url,
    )
