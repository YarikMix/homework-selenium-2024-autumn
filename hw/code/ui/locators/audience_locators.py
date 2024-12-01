from selenium.webdriver.common.by import By

from ui.locators.left_menu_locators import LeftMenuLocators


class AudiencePageLocators:
    left_menu = LeftMenuLocators()

    USERS_LIST_TAB_BTN = (By.ID, 'tab_audience.users_list')
    CREATE_USERS_LIST_BTN = (By.CSS_SELECTOR, '[data-testid=download-list]')
    NEW_USERS_LIST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="Введите название списка"]')
    NEW_USERS_LIST_TYPE_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')
    NEW_USERS_LIST_FILE_INPUT = (By.CSS_SELECTOR, 'input[type=file]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[data-testid=submit]')
    SUCCESS_NOTIFY = (By.CSS_SELECTOR, '.vkuiSnackbar')
    USERS_LIST_NAME = (By.CSS_SELECTOR, '.EditableName_name__qWWXi > div')

    @staticmethod
    def NEW_USERS_LIST_TYPE_SELECT_ITEM(list_type):
        return By.CSS_SELECTOR, f'[role=option][title={list_type}]'
