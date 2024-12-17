from selenium.webdriver.support import expected_conditions as ec

from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import LeadFormsPageLocators


class LeadFormsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormsPageLocators()

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def get_last_image_name(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def click_last_image(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME)

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def fill_empty_data(self):
        name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()

    def fill_data(self, name, company, title, description):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        leadform_name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()
        leadform_name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)
        description_input.send_keys(description)

    def fill_form(self):
        leadform_name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        leadform_name_input.send_keys('a'*10)
        company_name_input.send_keys('a'*10)
        title_input.send_keys('a'*10)
        description_input.send_keys('a'*10)

    def create_question(self):
        self.click(self.locators.ADD_QUESTION_BUTTON)

    def fill_question(self, description):
        question_input = self.find(self.locators.QUESTION_INPUT)
        question_input.send_keys(description)

    def fill_answers(self, description1, description2):
        answer_input = self.find(self.locators.ANSWER_1_INPUT)
        answer_input.send_keys(description1)

        answer_input = self.find(self.locators.ANSWER_2_INPUT)
        answer_input.send_keys(description2)

    def click_add_contact_data(self):
        self.click(self.locators.ADD_CONTACT_BUTTON)

    def click_multiple_answers_question(self):
        self.click(self.locators.SELECT_QUESTION_TYPE_BUTTON)
        self.click(self.locators.MULTIPLE_ANSWERS_BUTTON)

    def click_user_input_question(self):
        self.click(self.locators.SELECT_QUESTION_TYPE_BUTTON)
        self.click(self.locators.USER_ANSWER_BUTTON)

    def click_add_name_contact(self):
        self.click(self.locators.NAME_CONTACT)

    def click_add_phone_contact(self):
        self.click(self.locators.PHONE_CONTACT)

    def click_add_email_contact(self):
        self.click(self.locators.EMAIL_CONTACT)

    def click_add_link_contact(self):
        self.click(self.locators.LINK_CONTACT)

    def click_add_birthday_contact(self):
        self.click(self.locators.BIRTHDAY_CONTACT)

    def click_add_city_contact(self):
        self.click(self.locators.CITY_CONTACT)

    def click_add_selected_contacts(self):
        self.click(self.locators.ADD_SELECTED_CONTACTS_BUTTON)

    def click_bin_name(self):
        self.click(self.locators.BIN_NAME_BUTTON)

    def click_bin_phone(self):
        self.click(self.locators.BIN_PHONE_BUTTON)

    def fill_empty_header(self):
        heading_input = self.find(self.locators.HEADING_INPUT)
        heading_input.clear()

    def fill_header(self, header):
        answer_input = self.find(self.locators.HEADING_INPUT)
        answer_input.clear()
        answer_input.send_keys(header)

    def fill_description(self, description):
        answer_input = self.find(self.locators.DESCRIPTION_3_INPUT)
        answer_input.clear()
        answer_input.send_keys(description)

    def click_site(self):
        self.click(self.locators.SITE_BUTTON)

    def click_phone(self):
        self.click(self.locators.PHONE_BUTTON)

    def click_promocode(self):
        self.click(self.locators.PROMOCODE_BUTTON)

    def fill_site(self, site):
        site_input = self.find(self.locators.SITE_INPUT)
        site_input.send_keys(site)

    def fill_phone(self, phone):
        phone_input = self.find(self.locators.PHONE_INPUT)
        phone_input.send_keys(phone)

    def fill_promocode(self, promocode):
        promocode_input = self.find(self.locators.PROMOCODE_INPUT)
        promocode_input.send_keys(promocode)

    def click_notify(self):
        self.click(self.locators.NOTIFY_EMAIL_BUTTON)

    def empty_name(self):
        name_input = self.find(self.locators.NAME_4_INPUT)
        name_input.clear()

    def empty_address(self):
        address_input = self.find(self.locators.ADDRESS_INPUT)
        address_input.clear()

    def fill_name(self, name):
        name_input = self.find(self.locators.NAME_4_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    def fill_address(self, address):
        address_input = self.find(self.locators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(address)

    def fill_email(self, email):
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def fill_notify_email(self, email):
        email_input = self.find(self.locators.NOTIFY_EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_inn(self, inn):
        inn_input = self.find(self.locators.INN_INPUT)
        inn_input.send_keys(inn)

    def get_form_name(self) -> str:
        name = self.find(self.locators.FIRST_LEAD_FORM_NAME)
        return name.text

    def remove_lead_form(self):
        self.click(self.locators.ARCHIVE_BUTTON)
        self.click(self.locators.ARCHIVE_ACCEPT_BUTTON)
