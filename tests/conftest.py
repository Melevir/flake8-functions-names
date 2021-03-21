import ast
from typing import List

import deal
import pytest

from flake8_functions_names.custom_types import FuncdefInfo


@deal.pure
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
def fine_funcdef_info(funcdef_factory):
    return funcdef_factory(name='foo')


@pytest.fixture
def funcdef_for_bool_without_bool_result(funcdef_factory):
    return funcdef_factory(name='is_red', return_type='int')


@pytest.fixture
def fine_funcdef_with_property(funcdef_factory):
    return funcdef_factory(name='is_red', decorator='property')


@pytest.fixture
def funcdef_with_property_and_verb(funcdef_factory):
    return funcdef_factory(name='process_color', decorator='property')


@pytest.fixture
def fine_funcdef_save_to(funcdef_factory):
    return funcdef_factory(name='save_user_to_db')


@pytest.fixture
def fine_funcdef_save_without_to(funcdef_factory):
    return funcdef_factory(name='save_user')


@pytest.fixture
def fine_funcdef_load_from(funcdef_factory):
    return funcdef_factory(name='load_user_from_db')


@pytest.fixture
def fine_funcdef_load_without_from(funcdef_factory):
    return funcdef_factory(name='load_user')
