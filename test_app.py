# coding=utf-8
"""Deployable Flask webpage feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@pytest.fixture
def my_app():
    from app import app
    return app.test_client().get('/')


@pytest.fixture()
def get_app():
    import app
    return app


@scenario('app.feature', 'Requesting basic response from the Flask app')
def test_requesting_basic_response_from_the_flask_app():
    """Requesting basic response from the Flask app."""


@when('the flask app is requested')
def the_flask_app_is_requested(my_app):
    """the flask app is requested."""
    assert len(my_app.data) > 0


@then('the response status code is 200')
def the_response_status_code_is_200(my_app):
    """the response status code is 200."""
    assert my_app.status_code == 200


@then('the response content has data')
def the_response_content_has_data(my_app):
    """the response content has data."""
    assert b'Welcome' in my_app.data


@scenario('app.feature', 'Ensure that the count is changing')
def test_ensure_that_the_count_is_changing():
    """Ensure that the count is changing."""


@when("the flask app is imported")
def the_flask_app_is_imported(get_app):
    """the flask app is imported"""
    assert get_app.file_name == 'count.txt'


@then('count is incremented by a value of one')
def count_is_incremented_by_a_value_of_one(get_app):
    """count is incremented by a value of one."""
    old_count = get_app.get_count()
    new_count = get_app.update_count()
    assert old_count < new_count


@then('the current count is read')
def the_current_count_is_read(get_app):
    """the current count is read."""
    assert get_app.get_count() >= 0
