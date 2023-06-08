import pytest
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--login', default='for-robot@mail.ru')
    parser.addoption('--pwd', default='tpq9AMTtyrtmQ3F_')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    login = request.config.getoption('--login')
    pwd = request.config.getoption('--pwd')
    return {'url': url, 'login': login, 'pwd': pwd}


@pytest.fixture(scope='session')
def creds(config) -> tuple[str, str]:
    return config['login'], config['pwd']
