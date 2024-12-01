from ui.pages.base_page import BasePage
from ui.locators.overview_locators import OverviewPageLocators


class OverviewPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = OverviewPageLocators()