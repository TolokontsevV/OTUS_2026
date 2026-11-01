import pytest


@pytest.fixture(scope='session', autouse=False)
def check_circle():
    print('\n Start check circle')

    yield

    print('\n End check circle')
