from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CommercePageLocators(BasePageLocators):
    CREATE_BUTTON = (
        By.XPATH,
        "//*[@data-testid='create-catalog']",
    )

    SIDEBAR = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_')]")

    NEW_CATALOG_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-2') and text()='Новый каталог']",
    )

    NAME_INPUT = (By.XPATH, "//*[@data-testid='catalogName-input']")

    @staticmethod
    def TABS_NAME(tabs):
        return (
            By.XPATH,
            f"//*[@data-testid='catalog-source_type-select']//*[text()='{tabs}']",
        )

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")

    FEED_OR_COMMUNITY_INPUT = (By.XPATH, "//input[@data-testid='catalogUrl-input']")
    PERIOD_SELECT = (By.XPATH, "//input[@data-testid='catalogPeriod-select']")

    CHECKBOX_UTM_SIGN = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCheckbox')]//*[contains(@class, 'vkuiCheckbox__titleBefore') and text()='Автоматически удалять UTM-метки']",
    )

