from base import BaseCase
from ui.pages.education_page import EducationPage
from selenium.webdriver.support.wait import WebDriverWait


class TestFooterPage(BaseCase):
    
    def test_close_window(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_cross()
        assert education_page.is_window_not_visible()
    
    def test_vk_group(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_vkgroup()
        assert education_page.find_header_vk_group().text == 'Как хотите учиться?'
        assert len(education_page.find_vk_group_buttons()) == 3
    
    def test_vk_group_popup(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_vkgroup()
        education_page.move_to_tune_vk_group()
        assert education_page.find_vk_group_tune_popup()
    
    def test_vk_group_video(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_vkgroup()
        education_page.click_videocourse_vk_group()
        assert education_page.is_visible_video_vkgroup()
        
    def test_vk_group_courses(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_vkgroup()
        education_page.click_course_vk_group()
        education_page.switch_to_new_tab()
        assert self.is_redirect_occurred('https://ads.vk.com/hq/overview')

    def test_vk_group_hat_sign(self, education_page: EducationPage):
        education_page.click_education()
        education_page.move_to_hat_vk_group()
        assert education_page.is_visible_hat_popup_vk_group()
        
    def test_catalog(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_catalog()
        assert education_page.find_header_catalog().text == 'Как хотите учиться?'
        assert len(education_page.find_catalog_buttons()) == 3
    
    def test_catalog_create_btn(self, education_page: EducationPage):
        education_page.click_education()
        education_page.click_catalog()
        education_page.click_catalog_create_btn()
        assert self.is_url_open('https://ads.vk.com/hq/ecomm/catalogs')