from app.embeddings.validators import EmbeddingResult
from app.ingestion.validators import ParsedUnit
import logging

from app.registry import instances

logger = logging.getLogger(__name__)


def embed_parsed_units(parsed_files: list[ParsedUnit]) -> list[EmbeddingResult]:
    embedding_model = instances.get_embedder()

    embedding_result = []
    for parsed_file in parsed_files:
        embedding_text = f"Class: {parsed_file.class_name}\nMethod: {parsed_file.name}\n{parsed_file.content}"
        vector = embedding_model.embed_query(embedding_text)
        embedding_result.append(
            EmbeddingResult(
                id=parsed_file.id,
                vector=vector,
                class_name=parsed_file.class_name,
                metadata=parsed_file.model_dump(by_alias=True),
            )
        )

    return embedding_result