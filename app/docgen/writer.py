import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def write_docs(docs: dict[str, str], output_dir: str = "./docs") -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for class_name, content in docs.items():
        file_path = Path(output_dir) / f"{class_name}.md"
        file_path.write_text(content, encoding="utf-8")
        logger.info(f"Written: {file_path}")