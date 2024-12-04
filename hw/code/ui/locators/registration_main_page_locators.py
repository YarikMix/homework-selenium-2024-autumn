from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class RegistrationMainPageLocators(BasePageLocators):
    @staticmethod
    def TEXT(text):
        return By.XPATH, f"//*[text()='{text}']"

    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")

    MAIN_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'registration_panelTitle')]")

    MAIN_PAGE_SUBTITLE = (
        By.XPATH,
        "//*[contains(@class, 'registration_panelSubTitle')]",
    )

    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    IMPORT_MYTARGET_CABINET_BUTTON = (By.ID, "click-exportMTButton")

    IMPORT_MYTARGET_CABINET_BUTTON_HINT = (
        By.XPATH,
        "//*[contains(@id, 'click-exportMTButton')]/descendant::*[contains(@class, 'Hint_hintTrigger')]",
    )

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[text()='{language}']",
        )

    SELECTED_LANGUAGE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4",
    )
