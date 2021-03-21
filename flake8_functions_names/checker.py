import ast
from typing import Generator, Tuple

from flake8_functions_names import __version__ as version
from flake8_functions_names.custom_types import FuncdefInfo
from flake8_functions_names.validators import (
    validate_returns_bool_if_names_said_so,
    validate_has_property_and_no_verbs, validate_save_to, validate_load_from,
    validate_returns_bool_and_name_shows_it, validate_names_says_its_pure_and_its_pure,
    validate_no_blacklisted_words_in_name, validate_name_not_endswith_first_argument_name,
)


class FunctionsNamesChecker:
    name = 'flake8-functions-names'
    version = version

    validators = [
        validate_returns_bool_if_names_said_so,
        validate_has_property_and_no_verbs,
        validate_save_to,
        validate_load_from,
        validate_returns_bool_and_name_shows_it,
        validate_names_says_its_pure_and_its_pure,
        validate_no_blacklisted_words_in_name,
        validate_name_not_endswith_first_argument_name,
    ]

    def __init__(self, tree, filename: str):
        self.filename = filename
        self.tree = tree

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        funcdefs = (
            n for n in ast.walk(self.tree)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
        for funcdef in funcdefs:
            funcdef_details = FuncdefInfo(raw_funcdef=funcdef)
            for validator in self.validators:
                errors = validator(funcdef_details)
                for error in errors:
                    yield funcdef.lineno, funcdef.col_offset, error, type(self)
