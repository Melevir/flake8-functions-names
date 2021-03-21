import pytest

from flake8_functions_names.validators import (
    validate_returns_bool_if_names_said_so,
    validate_has_property_and_no_verbs, validate_save_to, validate_load_from,
    validate_returns_bool_and_name_shows_it, validate_names_says_its_pure_and_its_pure,
    validate_no_blacklisted_words_in_name, validate_name_not_endswith_first_argument_name,
)


def test_validate_returns_bool_if_names_said_so_raises_no_error_for_ok_function(fine_funcdef_info):
    assert not validate_returns_bool_if_names_said_so(fine_funcdef_info)


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


def test_validate_load_from_raises_error_for_load_without_from(
    fine_funcdef_load_without_from,
):
    actual_result = validate_load_from(fine_funcdef_load_without_from)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE004')


@pytest.mark.parametrize(
    'function_name',
    [
        'is_user_banned',
        'has_active_account',
        'have_enough_gold',
        'can_access_page',
        'check_if_user_is_active',
    ],
)
def test_validate_returns_bool_and_name_shows_it_raises_no_error_for_ok_function(
    function_name,
    funcdef_factory,
):
    funcdef = funcdef_factory(name=function_name, return_type='bool')
    assert not validate_returns_bool_and_name_shows_it(funcdef)


@pytest.mark.xfail
@pytest.mark.parametrize(
    'function_name',
    [
        'user_banned',
        'active_account',
        'enough_gold',
        'access',
        'if_user_is_active',
    ],
)
def test_validate_returns_bool_and_name_shows_it_raises_error_for_nonbool_names(
    function_name,
    funcdef_factory,
):
    funcdef = funcdef_factory(name=function_name, return_type='bool')
    actual_result = validate_returns_bool_and_name_shows_it(funcdef)
    assert len(actual_result) == 1
    assert actual_result[0].startswith('FNE005')


@pytest.mark.xfail
@pytest.mark.parametrize(
    'function_name, decorator, has_error',
    [
        ('print_settings', None, False),
        ('calculate_data', None, True),
        ('calculate_data', 'deal.pure', False),
        ('clean_form_data', None, True),
        ('clean_form_data', 'pure', False),
    ],
)
def test_validate_names_says_its_pure_and_its_pure_works_for_different_functions(  # noqa: CFQ003
    function_name, decorator, has_error,
    funcdef_factory,
):
    funcdef = funcdef_factory(name=function_name, return_type='bool', decorator=decorator)
    actual_result = validate_names_says_its_pure_and_its_pure(funcdef)
    if has_error:
        assert len(actual_result) == 1
        assert actual_result[0].startswith('FNE006')
    else:
        assert not actual_result


@pytest.mark.xfail
@pytest.mark.parametrize(
    'function_name, has_error',
    [
        ('fetch_data', False),
        ('process_data', False),
        ('fetch_and_process_data', True),
    ],
)
def test_validate_no_blacklisted_words_in_name_works_for_different_functions(
    function_name, has_error,
    funcdef_factory,
):
    funcdef = funcdef_factory(name=function_name)
    actual_result = validate_no_blacklisted_words_in_name(funcdef)
    if has_error:
        assert len(actual_result) == 1
        assert actual_result[0].startswith('FNE006')
    else:
        assert not actual_result


@pytest.mark.xfail
@pytest.mark.parametrize(
    'function_name, arguments, has_error',
    [
        ('is_active_for_user', [], False),
        ('is_active_for_user', ['user'], True),
        ('is_active_for', ['user'], False),
    ],
)
def test_validate_name_not_endswith_first_argument_name_works_for_different_functions(
    function_name, arguments, has_error,
    funcdef_factory,
):
    funcdef = funcdef_factory(name=function_name, arguments=arguments)
    actual_result = validate_name_not_endswith_first_argument_name(funcdef)
    if has_error:
        assert len(actual_result) == 1
        assert actual_result[0].startswith('FNE006')
    else:
        assert not actual_result
