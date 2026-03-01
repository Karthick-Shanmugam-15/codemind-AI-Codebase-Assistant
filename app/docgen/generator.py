from collections import defaultdict

from langchain_core.messages import SystemMessage, HumanMessage

from app.ingestion import ParsedUnit
from app.registry import instances

SYSTEM_PROMPT = """You are a Java documentation expert.
Generate README style documentation for the following class.
Output in markdown format with these sections:
1. Overview — what this class does
2. Usage — how to use it with example
3. Methods — for each method document:
   - Description
   - Parameters
   - Returns
   - Example"""

def generate_docs(parsed_units: list[ParsedUnit]) -> dict[str, str]:
    group_by_class_name = defaultdict(list)
    for unit in parsed_units:
        group_by_class_name[unit.class_name].append(unit)

    llm = instances.get_llm_model()
    docs = {}
    for class_name, units in group_by_class_name.items():
        code_sections = []
        for unit in units:
            code_sections.append(
                f"### {unit.type}: {unit.name}{unit.method_parameters}\n"
                f"{unit.content}\n"
            )
        code_combined = "\n".join(code_sections)
        prompt = f"Class: {class_name}\n\nCode:\n{code_combined}"

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]

        response = llm.invoke(messages)
        docs[class_name] = response.content

    return docs
