from base import BaseCase
from ui.pages.settings_page import SettingsPage


class TestSettingsPage(BaseCase):
    VALID_PHONE = "+79155218177"
    INVALID_PHONE = "89155218177"
    INVALID_EMAIL = "rrrrrr"
    INVALID_INN = "pppp"
    SMALL_INN = "4444"
    VALID_INN = "444444444444"
    FIO = "Гавирин Матвей Генадьевич"

    def test_invalid_phone(self, settings_page: SettingsPage):
        settings_page.fill_phone(self.INVALID_PHONE)
        settings_page.click_save()
        assert settings_page.is_invalid_phone_visible()

    def test_extra_email(self, settings_page: SettingsPage):
        settings_page.click_add_email()
        assert settings_page.is_extra_email_field_visible()

    def test_invalid_email(self, settings_page: SettingsPage):
        settings_page.click_add_email()
        settings_page.fill_email(self.INVALID_EMAIL)
        settings_page.click_save()
        assert settings_page.is_invalid_email_visible()

    def test_must_have_field(self, settings_page: SettingsPage):
        settings_page.fill_phone(self.VALID_PHONE)
        settings_page.click_save()
        assert settings_page.is_must_have_field_visible()

    def test_invalid_inn(self, settings_page: SettingsPage):
        settings_page.fill_inn(self.INVALID_INN)
        settings_page.click_save()
        assert settings_page.is_invalid_inn_visible()

    def test_small_inn(self, settings_page: SettingsPage):
        settings_page.fill_inn(self.SMALL_INN)
        settings_page.click_save()
        assert settings_page.is_small_inn_visible()