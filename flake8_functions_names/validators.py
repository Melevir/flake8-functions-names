from typing import List

from flake8_functions_names.custom_types import FuncdefInfo
from flake8_functions_names.utils.imports import is_module_installed
from flake8_functions_names.words import VERBS, PURE_VERBS, BLACKLISTED_WORDS_IN_FUNCTIONS_NAMES


def validate_returns_bool_if_names_said_so(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.is_name_looks_like_question and funcdef.return_type != 'bool':
        return [
            f'FNE001 Name of the function says, that is should '
            f'return bool, but it returns {funcdef.return_type}',
        ]
    return []


def validate_has_property_and_no_verbs(funcdef: FuncdefInfo) -> List[str]:  # noqa: FNE007
    if funcdef.has_property_decorator and any(w in VERBS for w in funcdef.name_words):
        verbs = [w for w in funcdef.name_words if w in VERBS]
        return [
            f'FNE002 The method has a @property decorator, '
            f"but has a verb in it's name ({', '.join(verbs)})",
        ]
    return []


def validate_save_to(funcdef: FuncdefInfo) -> List[str]:
    if 'save' in funcdef.name_words and 'to' not in funcdef.name_words:
        return [
            'FNE003 Name of the function uses "save", but not uses "to"',
        ]
    return []


def validate_load_from(funcdef: FuncdefInfo) -> List[str]:
    if 'load' in funcdef.name_words and 'from' not in funcdef.name_words:
        return [
            'FNE004 ame of the function uses "load", but not uses "from"',
        ]
    return []


def validate_returns_bool_and_name_shows_it(funcdef: FuncdefInfo) -> List[str]:  # noqa: FNE007
    if (
        funcdef.return_type == 'bool'
        and not funcdef.is_name_looks_like_question
        and not funcdef.is_buildin_dundner_method_that_returns_bool
    ):
        return [
            "FNE005 Return type of the function is bool, but the name doesn't show it",
        ]
    return []


def validate_names_says_its_pure_and_its_pure(  # noqa: CFQ003, FNE007
    funcdef: FuncdefInfo,
) -> List[str]:
    if (
        is_module_installed('deal')
        and not funcdef.has_deal_pure_decorator
        and any(w in PURE_VERBS for w in funcdef.name_words)
    ):
        return [
            'FNE006 Name of function says, that it works with data, '
            'so it should be pure, but it has no @deal.pure()',
        ]
    return []


def validate_no_blacklisted_words_in_name(funcdef: FuncdefInfo) -> List[str]:
    blacklisted_words = [w for w in funcdef.name_words if w in BLACKLISTED_WORDS_IN_FUNCTIONS_NAMES]
    if blacklisted_words:
        return [
            f'FNE007 "{blacklisted_words[0]}" is not recommended in functions names',
        ]
    return []


def validate_name_not_endswith_first_argument_name(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.arguments_names and funcdef.name.endswith(f'_{funcdef.arguments_names[0]}'):
        return [
            "FNE008 Name of functions ends with it's first argument name",
        ]
    return []
