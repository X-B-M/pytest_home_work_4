import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.dashboard import Dashboard
from ui.pages.login_page import LoginPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def dashboard(login_page) -> Dashboard:
    return login_page.login(('for_robot@mail.ru', 'tpq9AMTtyrtmQ3F'))


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()
