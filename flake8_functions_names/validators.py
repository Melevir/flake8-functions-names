from typing import List

from flake8_functions_names.custom_types import FuncdefInfo
from flake8_functions_names.utils.imports import is_module_installed
from flake8_functions_names.words import VERBS, PURE_VERBS, BLACKLISTED_WORDS_IN_FUNCTIONS_NAMES


def validate_returns_bool_if_names_said_so(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.is_name_looks_like_question and funcdef.return_type != 'bool':
        return [
            f'FNE001 Function name says that it should return a bool, '
            f'but it returns {funcdef.return_type}',
        ]
    return []


def validate_has_property_and_no_verbs(funcdef: FuncdefInfo) -> List[str]:  # noqa: FNE007
    if funcdef.has_property_decorator and any(w in VERBS for w in funcdef.name_words):
        verbs = [w for w in funcdef.name_words if w in VERBS]
        return [
            f'FNE002 Method has a @property decorator but has a verb '
            f"in its name ({', '.join(verbs)})",
        ]
    return []


def validate_save_to(funcdef: FuncdefInfo) -> List[str]:
    if 'save' in funcdef.name_words and 'to' not in funcdef.name_words:
        return [
            'FNE003 Function name uses "save", but doesn\'t use "to"',
        ]
    return []


def validate_load_from(funcdef: FuncdefInfo) -> List[str]:
    if 'load' in funcdef.name_words and 'from' not in funcdef.name_words:
        return [
            'FNE004 Function name uses "load", but doesn\'t use "from"',
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
            'FNE006 Function name says that it works with data '
            'so it should be pure, but it has no @deal.pure()',
        ]
    return []


def validate_no_blacklisted_words_in_name(funcdef: FuncdefInfo) -> List[str]:
    blacklisted_words = [w for w in funcdef.name_words if w in BLACKLISTED_WORDS_IN_FUNCTIONS_NAMES]
    if blacklisted_words:
        return [
            f'FNE007 "{blacklisted_words[0]}" is not recommended in function names',
        ]
    return []


def validate_name_not_endswith_first_argument_name(funcdef: FuncdefInfo) -> List[str]:
    if funcdef.arguments_names and funcdef.name.endswith(f'_{funcdef.arguments_names[0]}'):
        return [
            'FNE008 Function name ends with its first argument name',
        ]
    return []
