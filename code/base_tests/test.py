import time
import pytest
from base_tests.base import BaseCase


class TestOne(BaseCase):


    def test_title(self):
        assert "Рекламная платформа" in self.driver.title


    def test_login(self, creds):
        time.sleep(1)
        self.login_page.login(creds)
        time.sleep(2)


    def test_biling(self, dashboard):
        dashboard.open_billing()
        time.sleep(3)

    def test_profile_change(self, dashboard):
        dashboard.open_profile()
        time.sleep(2)

        elem = self.base_page.find(dashboard.locators.FIO)
        elem.clear()
        elem.send_keys("Омулев Фёдр Рисович")

        elem = self.base_page.find(dashboard.locators.INN)
        elem.clear()
        elem.send_keys("12345678901")

        elem = self.base_page.find(dashboard.locators.PHONE)
        elem.clear()
        elem.send_keys("+74957256358")

        self.base_page.click(dashboard.locators.BUTTON_SAVE)

