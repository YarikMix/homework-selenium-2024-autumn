from .base_page import BasePage
from ui.locators.settings_locators import SettingsLocators


class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = SettingsLocators()

    def fill_phone(self, phone):
        self.fill(self.locators.PHONE_LOCATOR, phone)

    def is_save_btn_visible(self):
        return self.is_visible(self.locators.SAVE_BTN_LOCATOR)

    def is_cancel_btn_visible(self):
        return self.is_visible(self.locators.CANCEL_BTN_LOCATOR)

    def is_must_have_field_visible(self):
        return self.is_visible(self.locators.MUST_HAVE_FIELD)

    def click_save(self):
        self.scroll_click(self.locators.SAVE_BTN_LOCATOR)

    def click_cancel(self):
        self.scroll_click(self.locators.CANCEL_BTN_LOCATOR)

    def is_invalid_phone_visible(self):
        return self.is_visible(self.locators.INVALID_PHONE_LOCATOR)

    def click_add_email(self):
        self.click(self.locators.ADD_EMAIL_LOCATOR)

    def is_extra_email_field_visible(self):
        return self.is_visible(self.locators.EXTRA_EMAIL_LOCATOR)

    def fill_email(self, email):
        self.fill(self.locators.EXTRA_EMAIL_LOCATOR, email)

    def is_invalid_email_visible(self):
        return self.is_visible(self.locators.INVALID_EMAIL_LOCATOR)

    def fill_inn(self, inn):
        self.fill(self.locators.INN_INPUT_LOCATOR, inn)

    def is_invalid_inn_visible(self):
        return self.is_visible(self.locators.INVALID_INN_LOCATOR)

    def is_small_inn_visible(self):
        return self.is_visible(self.locators.SMALL_INN_LOCATOR)

    def fill_fio(self, fio):
        self.fill(self.locators.FIO_INPUT_LOCATOR, fio)
