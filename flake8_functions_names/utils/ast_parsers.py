import ast
from typing import Union

from flake8_functions_names.custom_types import FuncdefInfo


def parse_funcdef(funcdef: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> FuncdefInfo:
    pass
