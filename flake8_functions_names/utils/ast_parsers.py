from __future__ import annotations

import ast
from typing import Union, Optional


def extract_decorator_str_respresentation(
    decorator_node: Union[ast.Name, ast.Attribute, ast.Call],
) -> Optional[str]:
    if isinstance(decorator_node, ast.Name):
        return decorator_node.id
    elif isinstance(decorator_node, ast.Attribute) and isinstance(decorator_node.value, ast.Name):
        return f'{decorator_node.value.id}.{decorator_node.attr}'
    elif isinstance(decorator_node, ast.Call):
        return extract_decorator_str_respresentation(decorator_node.func)
    return None
