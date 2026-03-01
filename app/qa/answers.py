from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from app.qa.validators import SearchResult
from app.registry import instances


SYSTEM_PROMPT = """You are an expert Java code assistant.
You have been given relevant code snippets from a codebase.
Answer the question based ONLY on the provided code snippets.
If the answer is not found in the code, say "I could not find relevant code for this question."
Be concise and precise in your answer."""

def doAnswer(question: str, search_results: list[SearchResult]) -> AIMessage:
    contexts = []
    snippet_id = 0
    for search_result in search_results:
        print(f"question: {question}, result: {search_result}")
        snippet_id = snippet_id + 1
        context = (
            f"--- Snippet {snippet_id} ---\n"
            f"Class: {search_result.class_name}\n"
            f"Method: {search_result.method_name}\n"
            f"File: {search_result.file_path}\n"
            f"Code:\n"
            f"{search_result.content}\n"
        )
        contexts.append(context)

    context_msg = "\n".join(contexts)
    messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Code snippets:\n{context_msg}\n\nQuestion: {question}")
    ]

    return instances.get_llm_model().invoke(messages)
