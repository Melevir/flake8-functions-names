import ast
from typing import NamedTuple, Union, List


class FuncdefInfo(NamedTuple):
    raw_funcdef: Union[ast.FunctionDef, ast.AsyncFunctionDef]

    @property
    def name(self) -> str:
        return ''

    @property
    def name_words(self) -> List[str]:
        return []

    @property
    def has_property_decorator(self) -> bool:
        return False

    @property
    def has_deal_pure_decorator(self) -> bool:
        return False

    @property
    def arguments_names(self) -> List[str]:
        return []
