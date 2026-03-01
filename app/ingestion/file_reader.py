
import os
from typing import List

from app.ingestion import validators
import logging

logger = logging.getLogger(__name__)

def read_file(file_path: str) -> List[validators.FileMetadata]:
    files_result: List[validators.FileMetadata] = []
    for root, dirs, files in os.walk(file_path):

        for file in files:
            full_path = os.path.join(root, file)
            try:
                with open(full_path, encoding="utf-8") as f:
                    content = f.read()

                files_result.append(
                    validators.FileMetadata(
                        file_path=full_path,
                        content=content
                    )
                )

            except Exception as e:
                logger.error("unable to read file {}", full_path)

    return files_result