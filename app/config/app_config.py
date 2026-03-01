from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", env_file_encoding="utf-8")

    embedding_provider: str = "ollama"
    embedding_model: str = "qwen3-embedding:0.6b"
    gemini_api_key: str = ""
    ollama_base_url: str = "http://localhost:11434"
    chroma_db_path: str = "./chroma_db"
    repo_name: str = "ingester"
    include_class_embedding: bool = False

    delete_chroma_db: bool = True

    top_k: int = 5

    llm_model: str = "qwen2.5:1.5b" # "qwen2.5:7b" #

    docs_output_dir: str = "./docs"
