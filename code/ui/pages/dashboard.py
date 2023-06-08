import time

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import CommonNavigationLocators


class Dashboard(BasePage):
    locators = CommonNavigationLocators

    def open_billing(self):
        self.click(self.locators.BILLING)

    def open_profile(self):
        self.click(self.locators.PROFILE)
        time.sleep(1)
        self.click(self.locators.PROFILE_CONTACTS)





