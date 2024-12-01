from ui.pages.overview_page import OverviewPage
from ui.locators.main_page import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.registration_page import RegistrationPage


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = MainPageLocators()

    def login(self, username, password):
        self.click(self.locators.NAVBAR_LOGIN_BTN_LOCATOR)
        self.click(self.locators.OAUTH_MAIL_BTN_LOCATOR)

        username_input = self.find(self.locators.USERNAME_INPUT_LOCATOR)
        username_input.send_keys(username)

        self.click(self.locators.NEXT_BTN_LOCATOR)
        self.click(self.locators.AUTH_PROBLEMS_BTN_LOCATOR)
        self.click(self.locators.AUTH_BY_PASSWORD_BTN_LOCATOR)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BTN_LOCATOR)

        return OverviewPage(self.driver)

    def login_no_cabinet(self, username, password):
        self.click(self.locators.NAVBAR_LOGIN_BTN_LOCATOR)
        self.click(self.locators.OAUTH_MAIL_BTN_LOCATOR)

        username_input = self.find(self.locators.USERNAME_INPUT_LOCATOR)
        username_input.send_keys(username)

        self.click(self.locators.NEXT_BTN_LOCATOR)
        self.click(self.locators.AUTH_PROBLEMS_BTN_LOCATOR)
        self.click(self.locators.AUTH_BY_PASSWORD_BTN_LOCATOR)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BTN_LOCATOR)

        return RegistrationPage(self.driver)