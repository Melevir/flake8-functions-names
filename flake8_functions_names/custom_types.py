import ast
from typing import NamedTuple, Union, List


class FuncdefInfo(NamedTuple):
    raw_funcdef: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    name: str
    name_words: List[str]
    has_property_decorator: bool
    has_deal_pure_decorator: bool
    arguments_names: List[str]
