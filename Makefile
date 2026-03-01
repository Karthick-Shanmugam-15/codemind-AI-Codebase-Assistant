
install-models:
	curl -fsSL https://ollama.com/install.sh | sh
	ollama pull qwen2.5:1.5b
	ollama pull nomic-embed-text

install:
	poetry install


run:
	poetry run python -m app.main

run-api:
	poetry run uvicorn api.app:app --reload