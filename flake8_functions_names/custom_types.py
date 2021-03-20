import ast
from typing import NamedTuple, Union, List, Optional


class FuncdefInfo(NamedTuple):
    raw_funcdef: Union[ast.FunctionDef, ast.AsyncFunctionDef]

    @property
    def name(self) -> str:
        return self.raw_funcdef.name

    @property
    def name_words(self) -> List[str]:
        return self.name.split('_')

    @property
    def has_property_decorator(self) -> bool:
        return False

    @property
    def has_deal_pure_decorator(self) -> bool:
        return False

    @property
    def arguments_names(self) -> List[str]:
        return []

    @property
    def return_type(self) -> Optional[str]:
        if self.raw_funcdef.returns is None:
            return None
        return [e.id for e in ast.walk(self.raw_funcdef.returns) if isinstance(e, ast.Name)][0]

    @property
    def is_name_looks_like_question(self) -> bool:
        return (
            self.name_words[0] in {'is', 'have', 'has', 'can'}
            or self.name_words[:2] == ['check', 'if']
        )
