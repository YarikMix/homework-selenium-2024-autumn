from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators import login_locators

class Credentials:
    def __init__(self, login, password):
        self.login = login
        self.password = password
class LoginPage(BasePage):
    locators = login_locators.LoginPageLocators()

    def login(self, credentials: Credentials):
        self.click(super().locators.NAV_BUTTON_CABINET_LOCATOR)

        self.click(self.locators.BUTTON_MAILRU_AUTH_LOCATOR)

        self.write_input(self.locators.INPUT_EMAIL_LOCATOR, credentials.login)

        self.click(self.locators.BUTTON_NEXT_LOCATOR)

        self.write_input(self.locators.INPUT_PASSWORD_LOCATOR, credentials.password)

        self.click(self.locators.BUTTON_SUBMIT_LOCATOR)

        self.mainPage = MainPage(self.driver)

        return self.mainPage

    def register(self, credentials: Credentials):
        self.click(super().locators.NAV_BUTTON_CABINET_LOCATOR)

        self.click(self.locators.BUTTON_MAILRU_AUTH_LOCATOR)

        self.write_input(self.locators.INPUT_EMAIL_LOCATOR, credentials.login)

        self.click(self.locators.BUTTON_NEXT_LOCATOR)

        self.write_input(self.locators.INPUT_PASSWORD_LOCATOR, credentials.password)

        self.click(self.locators.BUTTON_SUBMIT_LOCATOR)

        return self.preRegistrationPage