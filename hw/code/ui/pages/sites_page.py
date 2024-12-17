from ui.pages.base_page import BasePage
from ui.locators.site_locators import SitePageLocators


class SitePage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SitePageLocators()

    def create_pixel(self):
        self.click(self.locators.BUTTON_CREATE_NEW_PIXEL)

    def set_pixel_name(self, pixel_name):
        self.fill_in(self.locators.DOMAIN_INPUT, pixel_name)

    def submit_pixel(self):
        self.click(self.locators.BUTTON_GROUP_IFRAME)

    def close_create_pixel_modal(self):
        self.click(self.locators.BUTTON_CLOSE_MODAL)

    def get_pixels(self):
        return list(map(lambda pixel_name_element: pixel_name_element.text, self.find_all(self.locators.PIXEL_LIST_ITEM, 5)))
