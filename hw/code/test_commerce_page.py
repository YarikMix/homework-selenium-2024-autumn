from base import BaseCase


class TestCommercePage(BaseCase):
    def test_is_commerce_page_opened(self, commerce_page):
        commerce_page.click_create_button()
        assert commerce_page.sidebar_became_visible()
        assert commerce_page.new_catalog_has_h2_content_title()
        assert commerce_page.name_input_became_visible()
        assert commerce_page.has_tabs_content()
        assert commerce_page.sidebar_buttons_became_visible()
        assert commerce_page.cross_button_became_visible()

    def test_is_commerce_page_closed(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_cancel_button()
        assert commerce_page.sidebar_became_invisible()
        commerce_page.click_create_button()
        commerce_page.click_cross_button()
        assert commerce_page.sidebar_became_invisible()

    def test_has_feed_or_community_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()
        assert commerce_page.has_feed_or_community_tabs_content()

    def test_has_input_error_feed_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()

        assert commerce_page.has_input_error_feed_content()

    def test_has_marketplace_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        assert commerce_page.has_marketplace_tabs_content()

    def test_has_input_error_marketplace_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        for i in range(0, 3):
            assert commerce_page.has_input_error_marketplace_content()

    def test_has_manual_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_manual_tabs()
        assert commerce_page.manual_became_visible()

    def test_create_catalog(self, commerce_page):
        catalog_count = commerce_page.count_catalogs()
        commerce_page.set_item_count(catalog_count)
        commerce_page.click_create_button()
        assert commerce_page.sidebar_became_visible()
        assert commerce_page.new_catalog_has_h2_content_title()
        assert commerce_page.name_input_became_visible()
        assert commerce_page.has_tabs_content()
        assert commerce_page.sidebar_buttons_became_visible()
        assert commerce_page.cross_button_became_visible()
        commerce_page.enter_catalog_name()
        commerce_page.click_feed_tabs()
        assert commerce_page.has_feed_or_community_tabs_content()
        commerce_page.enter_community_link()
        commerce_page.select_4hr_period()
        assert commerce_page.utm_checkbox_became_invisible()
        commerce_page.finish_creating()
        assert self.is_opened(r"https://ads.vk.com/hq/ecomm/catalogs/\d+")
        commerce_page.click_settings_button()
        assert commerce_page.sidebar_became_visible()
        assert commerce_page.settings_title_became_visible()
        assert commerce_page.catalog_name_matches_in_settings()
        assert commerce_page.period_is_4hr_in_settings()
        commerce_page.close_settings()
        assert commerce_page.catalog_name_matches_in_selector()
        assert commerce_page.period_is_4hr_in_history()
        assert commerce_page.goods_loaded()
        commerce_page.click_goods_tab()
        assert commerce_page.items_match()
        commerce_page.delete_catalog()
        assert commerce_page.catalog_gone()
