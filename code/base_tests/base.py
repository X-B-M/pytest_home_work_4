import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
