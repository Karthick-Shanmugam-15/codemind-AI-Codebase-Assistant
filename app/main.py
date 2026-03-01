from pathlib import Path
import shutil

from app import ingestion
from app.config.app_config import AppConfig
from app.docgen import generator, writer
from app.qa import retriever, answers
from app.registry import instances
from app.embeddings import embedder
from app.registry.instances import get_app_config, get_embedder
from app.vectorstore import chroma_store
import logging

FILE_PATH = "/Users/karthickshanmugam/opscruise/ws1/ingester-service/oc-ingester-service/src/main/java/com/opscruise/stages"


def main():
    setup_logging()

    app_config: AppConfig = instances.get_app_config()

    remove_chrome_db(app_config)

    files: list[ingestion.FileMetadata] = ingestion.read_file(file_path=FILE_PATH)
    parsed_files: list[ingestion.ParsedUnit] = ingestion.parse_files(app_config, files)

    print(f"Total files: {len(files)}")
    print(f"Total parsed units: {len(parsed_files)}")

    embeddings = embedder.embed_parsed_units(parsed_files)
    chroma_store.store_embeddings(app_config, embeddings)

    print(f"Done! Stored {len(embeddings)} units in ChromaDB")

    # generate_documentation(app_config, parsed_files)
    #
    #
    ask("how does GCPConfigNormalizer class do ?")



def generate_documentation(app_config: AppConfig, parsed_files: list[ingestion.ParsedUnit]):
    docs = generator.generate_docs(parsed_files)
    writer.write_docs(docs, app_config.docs_output_dir)
    print(f"Generated docs for {len(docs)} classes")


def ask(question: str) -> None:
    results = retriever.search(question)
    response = answers.doAnswer(question, results)

    print(f"\nQuestion: {question}")
    print(f"\nAnswer: {response.content}")


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def remove_chrome_db(app_config: AppConfig) -> None:
    if not app_config.delete_chroma_db:
        return

    logging.info("Removing chrome db")
    db_path = Path(app_config.chroma_db_path)
    if db_path.exists():
        shutil.rmtree(db_path)

if __name__ == '__main__':
    main()