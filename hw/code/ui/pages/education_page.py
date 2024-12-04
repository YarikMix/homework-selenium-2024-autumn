from .base_page import BasePage
from  ui.locators.education_locators import EducationLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class EducationPage(BasePage):
    
    url = 'https://ads.vk.com/hq/overview'
    locators = EducationLocators()
    
    def click_education(self):
        self.click(self.locators.EDUCATION_LOCATOR)
    
    def click_cross(self):
        self.click(self.locators.CROSS_LOCATOR)
    
    def is_window_not_visible(self):
        return self.is_not_visible(self.locators.WINDOW_LOCATOR)
    
    def click_vkgroup(self):
        self.click(self.locators.VKGROUP_LOCATOR)
    
    def find_header_vk_group(self):
        return self.find(self.locators.VKGROUP_H2)
    
    def find_elements_within(self, parent_element, child_locator):
        return parent_element.find_elements(*child_locator)
    
    def find_vk_group_buttons(self):
        parent_element = self.find(self.locators.VKGROUP_BUTTONS)
        return self.find_elements_within(parent_element, self.locators.VKGROUP_BUTTONS_DIV)
    
    def is_visible_vk_group_tune_popup(self):
        return self.find(self.locators.VKGROUP_TUNE_POPUP)
    
    def move_to_tune_vk_group(self):
        self.hover(self.locators.VKGROUP_TUNE_BUTTON)

    def click_videocourse_vk_group(self):
        self.click(self.locators.VKGROUP_VIDEO_BUTTON)
    
    def is_visible_video_vkgroup(self):
        return self.is_visible(self.locators.VKGROUP_VIDEO)
    
    def click_course_vk_group(self):
        return self.click(self.locators.VKGROUP_COURSE_BUTTON)
    
    def move_to_hat_vk_group(self):
        self.hover(self.locators.VKGROUP_HAT_SIGN)
    
    def is_visible_hat_popup_vk_group(self):
        return self.is_visible(self.locators.VKGROUP_HAT_SIGN_POPUP)
    
    def click_catalog(self):
        self.click(self.locators.CATALOG_LOCATOR)
    
    def find_header_catalog(self):
        return self.find(self.locators.CATALOG_H2)
    
    def find_catalog_buttons(self):
        parent_element = self.find(self.locators.CATALOG_BUTTONS)
        return self.find_elements_within(parent_element, self.locators.CATALOG_BUTTONS_DIV)

    def click_catalog_create_btn(self):
        self.click(self.locators.CATALOG_CREATE_BTN)
        