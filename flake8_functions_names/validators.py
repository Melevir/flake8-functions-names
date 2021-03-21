from typing import List

from flake8_functions_names.custom_types import FuncdefInfo
from flake8_functions_names.verbs import VERBS


def validate_returns_bool_if_names_said_so(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.is_name_looks_like_question and funcdef.return_type != 'bool':
        return [
            f'FNE001 Name of the function says, that is should '
            f'return bool, but it returns {funcdef.return_type}',
        ]
    return []


def validate_has_property_and_no_verbs(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.has_property_decorator and any(w in VERBS for w in funcdef.name_words):
        verbs = [w for w in funcdef.name_words if w in VERBS]
        return [
            f'FNE002 The method has a @property decorator, '
            f"but has verb in it's name ({', '.join(verbs)})",
        ]
    return []


def validate_save_to(funcdef: FuncdefInfo) -> List[str]:
    return []


def validate_load_from(funcdef: FuncdefInfo) -> List[str]:
    return []


def validate_returns_bool_and_name_shows_it(funcdef: FuncdefInfo) -> List[str]:
    return []


def validate_names_says_its_pure_and_its_pure(funcdef: FuncdefInfo) -> List[str]:
    return []


def validate_no_blacklisted_words_in_name(funcdef: FuncdefInfo) -> List[str]:
    return []


def validate_name_not_endswith_first_argument_name(funcdef: FuncdefInfo) -> List[str]:
    return []
