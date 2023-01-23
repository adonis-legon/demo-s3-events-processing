import pytest

from src.tests.util import load_test_event


@pytest.fixture(name="put_event")
def put_event():
    return load_test_event('.', 'put')


@pytest.fixture(name="delete_event")
def delete_event():
    return load_test_event('.', 'delete')


@pytest.fixture(name="transition_event")
def transition_event():
    return load_test_event('.', 'transition')


@pytest.fixture(name="expiration_event")
def expiration_event():
    return load_test_event('.', 'expiration')
