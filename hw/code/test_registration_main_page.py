from base import NoAuthCase


class TestRegistrationMainPage(NoAuthCase):
    def test_main_page_rendering(self, registration_main_page):
        assert registration_main_page.header_became_visible()
        assert registration_main_page.language_switch_became_visible()
        assert registration_main_page.image_became_visible()
        assert registration_main_page.main_page_title_became_visible()
        assert registration_main_page.main_page_subtitle_became_visible()
        assert registration_main_page.create_new_cabinet_button_became_visible()
        assert registration_main_page.import_mytarget_cabinet_button_became_visible()

    def test_main_page_mytarget_hint(self, registration_main_page):
        registration_main_page.hover_import_mytarget_cabinet_button_hint()
        assert registration_main_page.mytarget_hint_became_visible()

    def test_create_new_cabinet_button(self, registration_main_page):
        registration_main_page.click_create_new_cabinet_button()
        assert self.is_opened("https://ads.vk.com/hq/registration/new")

    def test_import_mytarget_cabinet_button(self, registration_main_page):
        registration_main_page.click_import_mytarget_cabinet_button()
        assert self.is_opened("https://ads.vk.com/hq/registration/import/target")
