from base import NoAuthCase


class TestMainPage(NoAuthCase):
    def test_go_to_main_page_nav(self, main_page):
        main_page.click_vk_ads_logo()
        assert self.is_opened("https://ads.vk.com/")

    def test_go_to_news_page_nav(self, main_page):
        main_page.click_nav_item("Новости")
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_insights_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Полезные материалы")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_go_to_events_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Мероприятия")
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_videocourses_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Видеокурсы")
        main_page.go_to_new_tab()
        assert self.is_opened("https://expert.vk.com/catalog/courses/")

    def test_go_to_certification_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Сертификация")
        main_page.go_to_new_tab()
        assert self.is_opened("https://expert.vk.com/certification/")

    def test_go_to_cases_page_nav(self, main_page):
        main_page.click_nav_item("Кейсы")
        assert self.is_opened("https://ads.vk.com/cases")

    def test_go_to_ideas_forum_page_nav(self, main_page):
        main_page.click_nav_item("Форум идей")
        assert self.is_opened("https://ads.vk.com/upvote")

    def test_go_to_monetization_page_nav(self, main_page):
        main_page.click_nav_item("Монетизация")
        main_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/partner")

    def test_go_to_help_page_nav(self, main_page):
        main_page.click_nav_item("Справка")
        assert self.is_opened("https://ads.vk.com/help")

    def test_go_to_auth_page_nav(self, main_page):
        main_page.click_nav_cabinet_button()
        assert self.is_opened("https://id.vk.com/auth")

    def test_go_to_all_case_page(self, main_page):
        main_page.click_see_all_cases()
        assert self.is_opened("https://ads.vk.com/cases")

    def test_go_to_example_case_page(self, main_page):
        raw_title = main_page.get_case_title(new_page=False)
        main_page.click_case_item()
        new_title = main_page.get_case_title(new_page=True)
        print(new_title, raw_title)
        assert self.is_opened("https://ads.vk.com/cases")
        assert raw_title == new_title

    def test_go_to_webinar(self, main_page):
        main_page.click_webinar_item()
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_news(self, main_page):
        main_page.click_news_item()
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_auth_page_footer(self, main_page):
        main_page.click_footer_cabinet_button()
        assert self.is_opened("https://id.vk.com/auth")

    def test_go_to_news_page_footer(self, main_page):
        main_page.click_footer_item("Новости")
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_insights_page_footer(self, main_page):
        main_page.click_footer_item("Полезные материалы")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_go_to_events_page_footer(self, main_page):
        main_page.click_footer_item("Мероприятия")
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_documents_page_footer(self, main_page):
        main_page.click_footer_item("Документы")
        assert self.is_opened("https://ads.vk.com/documents")

    def test_go_to_education_page_footer(self, main_page):
        main_page.click_footer_item("Обучение для бизнеса")
        main_page.go_to_new_tab()
        assert self.is_opened("https://expert.vk.com/")

    def test_go_to_cases_page_footer(self, main_page):
        main_page.click_footer_item("Кейсы")
        assert self.is_opened("https://ads.vk.com/cases")

    def test_go_to_help_page_footer(self, main_page):
        main_page.click_footer_item("Помощь")
        assert self.is_opened("https://ads.vk.com/help")

    def test_go_to_monetization_page_footer(self, main_page):
        main_page.click_footer_item("Монетизация")
        main_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/partner")
