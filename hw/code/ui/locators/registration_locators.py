from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class RegistrationLocators(BasePageLocators):
    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']",
        )

    SELECTED_LANGUAGE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4",
    )

    COUNTRY_DROPDOWN = (By.XPATH, "//*[@data-testid='country']")

    @staticmethod
    def COUNTRY_DROPDOWN_ITEM(country_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{country_name}']",
        )

    CURRENCY_DROPDOWN = (By.XPATH, "//*[@data-testid='currency']")

    @staticmethod
    def CURRENCY_DROPDOWN_ITEM(currency_item):
        return By.XPATH, f"//*[@title='{currency_item}']"

    EMAIL_INPUT = (By.NAME, "email")
    INN_INPUT = (By.NAME, "inn")

    EMAIL_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::h5[text()='Email*']]",
    )

    INN_ERROR = (By.XPATH, "//*[@role='alert' and preceding-sibling::h5[text()='ИНН']]")

    OFFER_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::div[contains(@class, 'registration_offerDesc__')]]",
    )

    SUBMIT_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")

    OFFER_CHECKBOX = (By.NAME, "offer")

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiRadio__title')]//span[text()='{account_type}']",
        )
