import time

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from ui.pages.dashboard import Dashboard


class LoginPage(BasePage):
    locators = LoginPageLocators()
    def login(self, creds:tuple[str, str]):
        self.click(self.locators.GO_LOGIN)
        time.sleep(1)
        login = self.find(self.locators.LOGIN)
        login.clear()
        login.send_keys(creds[0])
        login = self.find(self.locators.PASSWORD)
        login.clear()
        login.send_keys(creds[1])
        time.sleep(1)
        self.click(self.locators.BUTTON_ENTER)
        time.sleep(1)
        #self.driver.find_element(*self.locators.BUTTON_ENTER).click()
        return Dashboard(self.driver)
