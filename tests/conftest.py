import ast

import pytest

from flake8_functions_names.custom_types import FuncdefInfo


@pytest.fixture
def fine_funcdef_info():
    return FuncdefInfo(
        raw_funcdef=ast.FunctionDef('foo', [], None),
        name='foo',
        name_words=['foo'],
        has_property_decorator=False,
        has_deal_pure_decorator=False,
        arguments_names=[],
    )
