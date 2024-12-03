from .base_page import BasePage
from ui.locators.company_locators import CompanyPageLocators
from enum import Enum


class CompanyTarget(Enum):
    SITE = 'site'
    CATALOG = 'ecomm'
    PUBLIC = 'social'
    ODKL = 'odkl'


class CompanyPage(BasePage):
    locators = CompanyPageLocators()
    url = 'https://ads.vk.com/hq/dashboard'

    def open_companies_list(self):
        self.click(self.locators.LOGO)
        self.click(self.locators.left_menu.COMPANIES_BTN)

    def open_companies_drafts(self):
        self.click(self.locators.COMPANIES_DRAFTS)

    def get_companies_drafts(self):
        return map(lambda company_draft_name_element: company_draft_name_element.text,
                   self.find_all(self.locators.COMPANY_DRAFT_NAME))

    def open_company_creation(self):
        self.click(self.locators.CREATE_COMPANY_BTN)

    def clear_companies(self):
        pass

    def select_target(self, target: CompanyTarget):
        if target == CompanyTarget.SITE:
            self.click(self.locators.SITE_COMPANY_TARGET)

    def set_site_url(self, url: str):
        self.fill_in(self.locators.SITE_URL_INPUT, url)

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass

    def apply_target(self):
        self.fill(self.locators.COMPANY_BUDGET_INPUT, '1000')
        self.unfocus()
        self.click(self.locators.APPLY_COMPANY_TARGET_BTN)

    def apply_groups(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.APPLY_COMPANY_GROUP_BTN)

    def set_region(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.REGION_RUSSIA_BTN_LOCATOR)

    def wait_for_region(self):
        self.find(self.locators.REGION_RUSSIA_BTN_LOCATOR)

    def is_no_region_message_visible(self):
        return self.is_visible(self.locators.NO_REGION_ERROR_LOCATOR)

    def wait_ad_header(self):
        self.find(self.locators.AD_HEADER_INPUT)

    def set_ad_header(self, header: str):
        elem = self.find(self.locators.AD_HEADER_INPUT)
        elem.send_keys(header)

    def set_ad_short_desc(self, description: str):
        elem = self.find(self.locators.AD_SHORT_DECS_TEXTAREA)
        elem.send_keys(description)

    def save_company(self):
        self.click(self.locators.SAVE_COMPANY_BTN)

    def open_catalogs_dropdown(self):
        self.click(self.locators.CATALOG_SELECT_LOCATOR)

    def select_catalog(self, text):
        self.click(self.locators.VK_UI_SELECT_ELEM(text))

    def set_ad_carousel_desc(self, description: str):
        self.fill_in(self.locators.AD_CAROUSEL_TEXTAREA, description)

    def set_ad_card_desc(self, description: str):
        self.fill_in(self.locators.AD_CARD_TEXTAREA, description)

    def public_company(self):
        self.click(self.locators.PUBLIC_LOCATOR)

    def wait_for_company_load(self):
        self.find(self.locators.CREATE_COMPANY_BTN, 200)

    def open_public_dropdown(self):
        self.click(self.locators.COMPANY_SELECT_PUBLIC_BTN)

    def open_public_another_btn(self):
        self.find(self.locators.ANOTHER_PUBLIC_BTN)

    def set_add_public_modal(self, description: str):
        self.fill_in(self.locators.ADD_PUBLIC_INPUT, description)

    def click_add_public_btn(self):
        self.click(self.locators.ADD_PUBLIC_BTN)

    def open_price_dropdown(self):
        self.click(self.locators.PRICE_DROPDOWN)