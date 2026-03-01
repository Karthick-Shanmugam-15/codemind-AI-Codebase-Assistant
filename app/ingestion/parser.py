from app.config.app_config import AppConfig
from app.ingestion.validators import FileMetadata, ParsedUnit
from tree_sitter import Language, Parser, Tree, Node
import tree_sitter_java

JAVA_LANGUAGE: Language = Language(tree_sitter_java.language())
parser: Parser = Parser(JAVA_LANGUAGE)

def parse_files(app_config: AppConfig, file_metadata: list[FileMetadata]) -> list[ParsedUnit]:
    result: list[ParsedUnit] = []
    for file in file_metadata:
        _parse_content(app_config, result, file)

    return result


def _parse_content(app_config: AppConfig, result: list[ParsedUnit], file_metadata: FileMetadata) -> None:
    content_bytes: bytes = file_metadata.get_content_bytes()
    tree: Tree = parser.parse(content_bytes)
    root_node: Node = tree.root_node

    lines = file_metadata.content.split("\n")

    for node in root_node.children:
        if node.type == "class_declaration":
            class_name = _get_class_name(node)
            if app_config.include_class_embedding :
                start_line = node.start_point.row
                end_line = node.end_point.row
                node_content = "\n".join(lines[start_line:end_line + 1])

                result.append(ParsedUnit(
                    file_path=file_metadata.file_path,
                    type=node.type,
                    name=class_name,
                    class_name=class_name,
                    content=node_content,
                    start_line=start_line,
                    end_line=end_line,
                    method_parameters=""
                ))
            for child in node.children:
                if child.type == "class_body":
                    for body in child.children:
                        if body.type in ("method_declaration", "constructor_declaration"):
                            method_name = _get_class_name(body)
                            parameter = _get_parameters(body)
                            start_line = body.start_point.row
                            end_line = body.end_point.row
                            node_content = "\n".join(lines[start_line:end_line + 1])

                            result.append(ParsedUnit(
                            file_path=file_metadata.file_path,
                            type=body.type,
                            name=method_name,
                            method_parameters=parameter,
                            class_name=class_name,
                            content=node_content,
                            start_line=start_line,
                            end_line=end_line,
                            ))






def _get_class_name(node: Node) -> str:
    for child in node.children:
        if child.type == "identifier":
            return child.text.decode("utf-8")
    return ""

def _get_parameters(node: Node) -> str:
    for child in node.children:
        if child.type == "formal_parameters":
            return child.text.decode("utf-8")
    return ""


