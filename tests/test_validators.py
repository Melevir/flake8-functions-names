import pytest

from flake8_functions_names.validators import (
    validate_returns_bool_if_names_said_so,
    validate_has_property_and_no_verbs, validate_save_to, validate_load_from,
)


def test_validate_returns_bool_if_names_said_so_raises_no_error_for_ok_function(fine_funcdef_info):
    assert not validate_returns_bool_if_names_said_so(fine_funcdef_info)


@pytest.mark.xfail
def test_validate_returns_bool_if_names_said_so_raises_error_for_nonbool_result_type(
    funcdef_for_bool_without_bool_result,
):
    actual_result = validate_returns_bool_if_names_said_so(funcdef_for_bool_without_bool_result)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE001')


def test_validate_has_property_and_no_verbs_raises_no_error_for_ok_function(
    fine_funcdef_info,
    fine_funcdef_with_property,
):
    assert not validate_has_property_and_no_verbs(fine_funcdef_info)
    assert not validate_has_property_and_no_verbs(fine_funcdef_with_property)


@pytest.mark.xfail
def test_validate_has_property_and_no_verbs_raises_error_for_propery_with_verb(
    funcdef_with_property_and_verb,
):
    actual_result = validate_has_property_and_no_verbs(funcdef_with_property_and_verb)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE002')


def test_validate_save_to_raises_no_error_for_ok_function(
    fine_funcdef_info,
    fine_funcdef_save_to,
):
    assert not validate_save_to(fine_funcdef_info)
    assert not validate_save_to(fine_funcdef_save_to)


@pytest.mark.xfail
def test_validate_save_to_raises_error_for_save_without_to(
    fine_funcdef_save_without_to,
):
    actual_result = validate_save_to(fine_funcdef_save_without_to)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE003')


def test_validate_load_from_raises_no_error_for_ok_function(
    fine_funcdef_info,
    fine_funcdef_load_from,
):
    assert not validate_load_from(fine_funcdef_info)
    assert not validate_load_from(fine_funcdef_load_from)


@pytest.mark.xfail
def test_validate_load_from_raises_error_for_load_without_from(
    fine_funcdef_load_without_from,
):
    actual_result = validate_load_from(fine_funcdef_load_without_from)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE004')
