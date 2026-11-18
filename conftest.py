import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default=None,
        help="URL ресурса"
    )

    parser.addoption(
        "--status",
        default=None,
        help="Ответ ресурса"
    )

@pytest.fixture(scope="session")
def url(pytestconfig):
    return pytestconfig.getoption("--url")

@pytest.fixture(scope="session")
def status(pytestconfig):
    return pytestconfig.getoption("--status")
