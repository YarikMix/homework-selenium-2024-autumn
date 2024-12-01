from .base_page import BasePage
from  ui.locators.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = RegistrationLocators()