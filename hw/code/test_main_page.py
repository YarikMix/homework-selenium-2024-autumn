from base import NoAuthCase


class TestMainPage(NoAuthCase):
    def test_main_go_to_main_page_nav(self, main_page):
        main_page.click_vk_ads_logo()
        assert self.is_opened("https://ads.vk.com/")

    def test_main_go_to_news_page_nav(self, main_page):
        main_page.click_nav_item("Новости")
        assert self.is_opened("https://ads.vk.com/news")

    def test_main_go_to_insights_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Полезные материалы")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_main_go_to_events_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Мероприятия")
        assert self.is_opened("https://ads.vk.com/events")
