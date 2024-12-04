from ui.pages.base_page import BasePage
from ui.locators.site_locators import SitePageLocators

from ui.pages.base_page_functionality import add_write, add_clicks


class SitePage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SitePageLocators()

    @property
    @add_clicks
    def BUTTON_CLEAR_SEARCH(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CLEAR)

    @property
    @add_clicks
    def BUTTON_CREATE_PIXEL_BY_ID(self):
        return self.find(self.locators.LABEL_ID_PIXEL)

    @property
    @add_clicks
    def BUTTON_CREATE_PIXEL(self):
        return self.find(self.locators.BUTTON_CREATE_NEW_PIXEL)

    @property
    @add_clicks
    def BUTTON_CREATE_PIXEL_COPY(self):
        return self.find(self.locators.BUTTON_CREATE_COPY_PIXEL)

    @property
    def ERROR_MESSAGE(self):
        return self.find(self.locators.ERROR_DOMAIN_INPUT).text

    @property
    @add_write
    def INPUT_FIELD_PIXEL_ID(self):
        return self.find(self.locators.PIXEL_ID_INPUT)

    @property
    @add_write
    def INPUT_EMAIL_OWNER(self):
        return self.find(self.locators.EMAIL_INPUT, 3)

    @property
    @add_write
    def INPUT_EMAIL_OWNER_INPUT(self):
        return self.find(self.locators.INPUT_EMAIL_INPUT, 3)

    @property
    @add_clicks
    def FRAME_BUTTON(self):
        return self.find(self.locators.BUTTON_GROUP_IFRAME, 5)

    @property
    def PIXEL_CREATE_MESSAGE(self):
        return self.find(self.locators.TEXT_CREATE_PIXEL_ID_CONFIRM).text

    @property
    def PIXEL_NOT_FOUND_MESSAGE(self):
        return self.find(self.locators.MESSAGE_PIXEL_FOUND).text

    @property
    @add_write
    def INPUT_FIELD_DOMAIN_NAME(self):
        return self.find(self.locators.DOMAIN_INPUT)

    @property
    def ADD_PIXEL_MESSAGE(self):
        return self.find(self.locators.TEXT_ADD_PIXEL_HEADER).text

    @property
    def NOT_FOUND_PIXEL_MESSAGE(self):
        return self.find(self.locators.TEXT_NOTHING_FOUND).text

    def open_more_menu(self):
        self.hover_wrapper(self.locators.BUTTON_MENU_MORE)
        self.click(self.locators.BUTTON_MENU_MORE)

    @property
    @add_clicks
    def SUBMIT_UPDATE_BUTTON(self):
        return self.find(self.locators.BUTTON_SUBMIT_UPDATE)

    @property
    @add_write
    def UPDATE_NAME_INPUT(self):
        return self.find(self.locators.INPUT_PIXEL_NAME_UPDATE)

    @property
    @add_clicks
    def BUTTON_DELETE(self):
        return self.find(self.locators.BUTTON_DELETE_CONFIRM)

    @property
    def NO_PIXELS_MESSAGE(self):
        return self.find(self.locators.TEXT_NO_PIXELS_FOUND).text

    @property
    def NOTHING_FOUND_MESSAGE(self):
        return self.find(self.locators.TEXT_NOTHING_FOUND).text

    @property
    def DOMAIN_FOUND_MESSAGE(self):
        return self.find(self.locators.TEXT_PIXEL_DOMAIN_FOUND).text

    @property
    @add_write
    def SEARCH_INPUT_FIELD(self):
        return self.find(self.locators.SEARCH_INPUT, timeout=20)

    @property
    @add_clicks
    def BUTTON_ADD_PIXEL(self):
        return self.find(self.locators.BUTTON_ADD_PIXEL)

    @property
    @add_clicks
    def BUTTON_CLOSE_MODAL(self):
        return self.find(self.locators.BUTTON_CLOSE_MODAL)

    def PIXEL_RAW(self, name):
        return self.find(self.locators.PIXEL_ROW(name), timeout=20).parent

    def PIXEL_RAW_BY_ID(self, id):
        return self.find(self.locators.PIXEL_ROW_BY_ID(id), timeout=20).parent

    def SPAN_PIXEL_NAME(self, pixel_raw, name):
        return self.find_child(pixel_raw, self.locators.PIXEL_NAME(name))

    def DIV_PIXEL_ID(self, pixel_raw, id):
        return self.find_child(pixel_raw, self.locators.PIXEL_ID(id))

    def SPAN_PIXEL_STATUS(self, pixel_raw, status):
        return self.find_child(pixel_raw, self.locators.PIXEL_STATUS(status))

    @property
    @add_clicks
    def BUTTON_ACCESS(self):
        return self.find(self.locators.BUTTON_REQUEST_ACCESS)

    @property
    @add_clicks
    def CONFIRM_ACCESS_BUTTON(self):
        return self.find(self.locators.BUTTON_REQUEST)

    def open_update_modal(self):
        self.open_more_menu()
        self.click(self.locators.DROPDOWN_MENU_UPDATE)

    def open_delete_modal(self):
        self.open_more_menu()
        self.click(self.locators.DROPDOWN_MENU_DELETE)
