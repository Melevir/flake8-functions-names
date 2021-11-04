import ast
from typing import NamedTuple, Union, List, Optional

from flake8_functions_names.utils.ast_parsers import extract_decorator_str_respresentation
from flake8_functions_names.words import DUNDER_BUILDINS_THAT_RETURNS_BOOL


class FuncdefInfo(NamedTuple):
    raw_funcdef: Union[ast.FunctionDef, ast.AsyncFunctionDef]

    @property
    def name(self) -> str:
        return self.raw_funcdef.name.lower()

    @property
    def name_words(self) -> List[str]:
        return self.name.strip('_').split('_')

    @property
    def has_property_decorator(self) -> bool:
        return 'property' in self.decorators_names

    @property
    def has_overrides_decorator(self) -> bool:
        return (
            'overrides' in self.decorators_names
            or 'overrides.overrides' in self.decorators_names
        )

    @property
    def has_deal_pure_decorator(self) -> bool:  # noqa: CFQ003
        return 'pure' in self.decorators_names or 'deal.pure' in self.decorators_names

    @property
    def arguments_names(self) -> List[str]:
        return [a.arg for a in ast.walk(self.raw_funcdef.args) if isinstance(a, ast.arg)]

    @property
    def return_type(self) -> Optional[str]:
        if self.raw_funcdef.returns is None:
            return None
        return_types = [e.id for e in ast.walk(self.raw_funcdef.returns) if isinstance(e, ast.Name)]
        return return_types[0] if return_types else None

    @property
    def is_name_looks_like_question(self) -> bool:
        return (
            self.name_words[0] in {'is', 'are', 'have', 'has', 'can'}
            or self.name_words[:2] == ['check', 'if']
        )

    @property
    def is_buildin_dundner_method_that_returns_bool(self) -> bool:
        return self.name.strip('_') in DUNDER_BUILDINS_THAT_RETURNS_BOOL

    @property
    def decorators_names(self) -> List[str]:
        decorators = [
            extract_decorator_str_respresentation(d)
            for d in self.raw_funcdef.decorator_list
        ]
        return list(filter(None, decorators))
