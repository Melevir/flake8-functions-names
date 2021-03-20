import ast
from typing import List

import pytest

from flake8_functions_names.custom_types import FuncdefInfo


def _generate_funcdef_info(funcdef: str) -> FuncdefInfo:
    return FuncdefInfo(ast.parse(funcdef + ':\n    pass').body[0])


@pytest.fixture
def funcdef_factory():
    def factory(
        name: str,
        return_type: str = None,
        decorator: str = None,
        arguments: List[str] = None,
    ) -> FuncdefInfo:
        arguments_str = ', '.join(arguments) if arguments else ''
        funcdef_str = f'def {name}({arguments_str})'
        if return_type:
            funcdef_str = f'{funcdef_str} -> {return_type}'
        if decorator:
            funcdef_str = f'@{decorator}\n{funcdef_str}'
        return _generate_funcdef_info(funcdef_str)
    return factory


@pytest.fixture
def fine_funcdef_info():
    return _generate_funcdef_info('def foo()')


@pytest.fixture
def funcdef_for_bool_without_bool_result(fine_funcdef_info):
    return _generate_funcdef_info('def is_red(color) -> int')


@pytest.fixture
def fine_funcdef_with_property():
    return _generate_funcdef_info('@property\ndef is_red(color) -> int')


@pytest.fixture
def funcdef_with_property_and_verb():
    return _generate_funcdef_info('@property\ndef process_color(color) -> int')


@pytest.fixture
def fine_funcdef_save_to():
    return _generate_funcdef_info('def save_user_to_db(user)')


@pytest.fixture
def fine_funcdef_save_without_to():
    return _generate_funcdef_info('def save_user(user)')


@pytest.fixture
def fine_funcdef_load_from():
    return _generate_funcdef_info('def load_user_from_db(user)')


@pytest.fixture
def fine_funcdef_load_without_from():
    return _generate_funcdef_info('def load_user(user)')
