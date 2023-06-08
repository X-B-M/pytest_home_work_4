from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')
    GO_LOGIN = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')


class LoginPageLocators(BasePageLocators):
    LOGIN = (By.XPATH, '//input[contains(@name,"email")]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    # BUTTON_ENTER = (By.XPATH, '//div[text()="Войти"]')
    BUTTON_ENTER = (By.XPATH, '//div[text()="Войти" and @class="authForm-module-button-1u2DYF"]')


class CommonNavigationLocators:
    DASHBOARD = (By.LINK_TEXT, '/dashboard')
    # BILLING = (By.LINK_TEXT, 'https://target.my.com/billing#deposit')
    BILLING = (By.XPATH, '//li/a[@href="/billing"]')
    PROFILE = (By.XPATH, '//a[@href="/profile"]')
    PROFILE_CONTACTS = (By.XPATH, '//a[@href="/profile/contacts"]')

    FIO = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input')
    INN = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[3]/div[1]/div/div/input")
    PHONE = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input")
    BUTTON_SAVE = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button/div")
