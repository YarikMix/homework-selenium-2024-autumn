from ui.pages.base_page import BasePage
from ui.locators.commerce_page_locators import CommercePageLocators
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class CommercePage(BasePage):
    url = "https://ads.vk.com/hq/ecomm/catalogs"
    catalog_url = r"https://ads.vk.com/hq/ecomm/catalogs/\d+"
    locators = CommercePageLocators()

    TABS_LIST = ["Фид или сообщество", "Маркетплейс", "Вручную"]

    ERRORS_FEED_LIST = [
        "Необходимо указать протокол http(s)",
        "Невалидный url",
        "Неверный формат файла",
        "Не удалось выполнить запрос по HTTP",
    ]
    INPUTS_FEED_LIST = [
        "h",
        "http://",
        "https://nota-tabula.ru",
        "https://nota-tabula.rur",
    ]
    CATALOG_NAME = "Тестовый каталог"
    VK_COMMUNITY = "https://vk.com/otpechatayru"
    REFRESH_PERIODS = ["1 час", "4 часа", "8 часов", "Ежедневно"]

    ERRORS_MARKETPLACE_LIST = [
        "Необходимо указать протокол http(s)",
        "Невалидный url",
        "Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе",
    ]
    INPUTS_MARKETPLACE_LIST = [
        "h",
        "http://",
        "https://www.wildberries.rus/brands/310451382-miryuyu",
    ]

    CATALOG_COUNT = 1

    ITEMS = [
        {
            "name": "Стикерпаки / плоттерная резка наклеек",
            "price": 90,
        },
        {
            "name": "Наклейки на плёнке и бумаге",
            "price": 60,
        },
        {
            "name": "Меню",
            "price": 40,
        },
        {
            "name": "Листовки",
            "price": 7,
        },
        {
            "name": "Брошюры",
            "price": 150,
        },
        {
            "name": "Блокноты",
            "price": 50,
        },
        {
            "name": "Визитки шелкография",
            "price": 25,
        },
        {
            "name": "Визитки (стандартные)",
            "price": 9,
        },
        {
            "name": "Пластиковые карты",
            "price": 50,
        },
        {
            "name": "Визитки на плотной бумаге",
            "price": 17,
        },
    ]

    def sidebar_became_visible(self):
        return self.became_visible(self.locators.SIDEBAR)

    def sidebar_became_invisible(self):
        return self.became_invisible(self.locators.SIDEBAR)

    def new_catalog_has_h2_content_title(self):
        return self.became_visible(self.locators.NEW_CATALOG_H2)

    def name_input_became_visible(self):
        return self.became_visible(self.locators.NAME_INPUT)

    def has_tabs_content(self):
        for t in self.TABS_LIST:
            if not self.became_visible(self.locators.TABS_NAME(t)):
                return False
        return True

    def sidebar_buttons_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON) and self.became_visible(
            self.locators.CANCEL_BUTTON
        )

    def cross_button_became_visible(self):
        return self.became_visible(self.locators.CROSS_BUTTON)

    def has_feed_or_community_tabs_content(self):
        return (
                self.became_visible(self.locators.FEED_OR_COMMUNITY_INPUT)
                and self.became_visible(self.locators.PERIOD_SELECT)
                and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
        )

    def utm_checkbox_became_invisible(self):
        return self.became_invisible(self.locators.CHECKBOX_UTM_SIGN)

    def has_input_error_feed_content(self):
        for i in range(0, 4):
            feed_link = self.find(self.locators.SELLER_INPUT)
            feed_link.clear()
            feed_link.send_keys(self.INPUTS_FEED_LIST[i])
            self.click(self.locators.SUBMIT_BUTTON)
            if not self.became_visible(
                    self.locators.ALERT_SIGN(self.ERRORS_FEED_LIST[i])
            ):
                return False
        return True

    def has_marketplace_tabs_content(self):
        return self.became_visible(self.locators.SELLER_INPUT) and self.became_visible(
            self.locators.MARKERPLACE_BANNER
        )

    def has_input_error_marketplace_content(self, input, error):
        for i in range(0, 3):
            feed_link = self.find(self.locators.SELLER_INPUT)
            feed_link.clear()
            feed_link.send_keys(self.INPUTS_MARKETPLACE_LIST[i])
            self.click(self.locators.SUBMIT_BUTTON)
            self.became_visible(self.locators.ALERT_SIGN(self.ERRORS_MARKETPLACE_LIST))

    def has_manual_tabs_content(self):
        return (
                self.became_visible(self.locators.CATEGORY_SELECT)
                and self.became_visible(self.locators.DOWNLOAD_BUTTON)
                and self.became_visible(self.locators.DROPZONE)
                and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
        )

    def click_create_button(self):
        self.click(self.locators.CREATE_BUTTON)

    def click_feed_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[0]))

    def click_marketplace_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[1]))

    def click_manual_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[2]))

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

    def click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON)

    def enter_catalog_name(self):
        name_input = self.find(self.locators.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(self.CATALOG_NAME)

    def get_catalog_name_in_settings(self) -> str:
        return self.find(self.locators.NAME_INPUT).get_attribute("value")

    def get_catalog_name_in_selector(self) -> str:
        return self.find(self.locators.CATALOG_NAME_IN_SELECTOR).text

    def catalog_name_matches_in_settings(self) -> bool:
        return self.CATALOG_NAME in self.get_catalog_name_in_settings()

    def catalog_name_matches_in_selector(self) -> bool:
        return self.CATALOG_NAME in self.get_catalog_name_in_selector()

    def enter_community_link(self):
        link_input = self.find(self.locators.FEED_OR_COMMUNITY_INPUT)
        link_input.clear()
        link_input.send_keys(self.VK_COMMUNITY)

    def click_period_selector(self):
        self.click(self.locators.PERIOD_SELECT)

    def select_period(self, period: str):
        self.click(self.locators.PERIOD_SELECT)
        self.click(self.locators.PERIOD_SELECT_ELEMENT(period))

    def get_selected_period_in_settings(self):
        return self.find(self.locators.SELECTED_PERIOD).text

    def get_selected_period_in_history(self):
        return self.find(self.locators.HISTORY_PERIOD).text

    def select_4hr_period(self):
        self.select_period(self.REFRESH_PERIODS[1])

    def period_is_4hr_in_settings(self) -> bool:
        return self.get_selected_period_in_settings() == self.REFRESH_PERIODS[1]

    def period_is_4hr_in_history(self) -> bool:
        return self.REFRESH_PERIODS[1] in self.get_selected_period_in_history()

    def click_modal_create_button(self):
        self.click(self.locators.MODAL_CREATE_BUTTON)

    def finish_creating(self):
        while not self.sidebar_became_invisible():
            try:
                self.click_modal_create_button()
            except Exception as e:
                if e in [ElementClickInterceptedException, TimeoutException]:
                    continue

    def click_settings_button(self):
        self.click(self.locators.CATALOG_SETTINGS_BUTTON)

    def settings_title_became_visible(self):
        return self.became_visible(self.locators.SETTINGS_H2)

    def delete_catalog(self):
        self.click_settings_button()
        assert self.became_visible(self.locators.SETTINGS_H2)
        self.click(self.locators.DELETE_CATALOG_BUTTON)
        assert self.became_visible(self.locators.CONFIRM_POPUP)
        self.click(self.locators.DELETE_BUTTON)

    def count_catalogs(self):
        return len(self.find_all(self.locators.CATALOG_LIST_ITEM))

    def set_item_count(self, count: int):
        self.CATALOG_COUNT = count

    def catalog_gone(self) -> bool:
        return len(self.find_all(self.locators.CATALOG_LIST_ITEM)) == self.CATALOG_COUNT

    def close_settings(self):
        while not self.sidebar_became_invisible():
            try:
                self.click_cancel_button()
                self.click_cross_button()
            except Exception as e:
                if e in [ElementClickInterceptedException, TimeoutException]:
                    continue

    def goods_loaded(self) -> bool:
        return self.became_invisible(self.locators.SPINNER, timeout=60)

    def click_goods_tab(self):
        self.click(self.locators.CATALOG_GOODS_TAB)

    def get_catalog_items(self) -> int:
        name_elems = self.find_all(self.locators.STOCK_ITEM_NAME)
        price_elems = self.find_all(self.locators.STOCK_ITEM_PRICE)
        return list(
            zip(
                [elem.text for elem in name_elems],
                [elem.text for elem in price_elems]
            )
        )

    def items_match(self) -> bool:
        page_items = self.get_catalog_items()
        print(len(page_items))
        if len(page_items) != len(self.ITEMS):
            return False

        for item in page_items:
            dict_form = {
                "name": item[0],
                "price": int(item[1].split(',')[0])
            }
            print(dict_form)
            if dict_form not in self.ITEMS:
                return False

        return True
