from ui.locators.audience_locators import AudiencePageLocators
from ui.pages.base_page import BasePage


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    def open_users_list_list(self):
        self.click(self.locators.left_menu.AUDIENCE_BTN)
        self.click(self.locators.USERS_LIST_TAB_BTN)

    def open_users_list_creation(self):
        self.click(self.locators.CREATE_USERS_LIST_BTN)

    def load_new_users_list(self, users_list_name: str, type: str, file_name: str):
        self.fill_in(self.locators.NEW_USERS_LIST_NAME_INPUT, users_list_name)
        self.click(self.locators.NEW_USERS_LIST_TYPE_SELECT)
        self.click(self.locators.NEW_USERS_LIST_TYPE_SELECT_ITEM(type))
        self.find_invisible(self.locators.NEW_USERS_LIST_FILE_INPUT).send_keys(file_name)

    def submit_users_list_creation(self):
        self.click(self.locators.SUBMIT_BTN)

    def wait_for_success_notify(self):
        self.find(self.locators.SUCCESS_NOTIFY, 600)

    def get_users_lists(self):
        return list(map(lambda users_list_name_element: users_list_name_element.text, self.find_all(self.locators.USERS_LIST_NAME)))