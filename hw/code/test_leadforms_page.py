import os

from base import BaseCase
from ui.locators.leadforms_locators import LeadFormsPageLocators

FILEPATH = os.path.join(os.path.dirname(__file__), 'files/img.png')


class TestLeadFormsPage(BaseCase):
    locators = LeadFormsPageLocators()

    def test_create_with_all_fields(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        leadforms_page.click_last_image()

        leadforms_page.fill_data('ф', 'ф', 'ф', 'ф')
        leadforms_page.click_continue()

        leadforms_page.click_bin_name()
        leadforms_page.click_bin_phone()
        leadforms_page.click_add_contact_data()
        leadforms_page.click_add_name_contact()
        leadforms_page.click_add_phone_contact()
        leadforms_page.click_add_email_contact()
        leadforms_page.click_add_link_contact()
        leadforms_page.click_add_birthday_contact()
        leadforms_page.click_add_city_contact()
        leadforms_page.click_add_selected_contacts()
        leadforms_page.create_question()
        leadforms_page.fill_question('Когда?')
        leadforms_page.fill_answers('Вчера', 'Сегодня')
        leadforms_page.create_question()
        leadforms_page.click_multiple_answers_question()
        leadforms_page.fill_question('Зачем?')
        leadforms_page.fill_answers('Так надо', 'Так хочется')
        leadforms_page.create_question()
        leadforms_page.click_user_input_question()
        leadforms_page.fill_question('Что?')
        leadforms_page.click_continue()

        leadforms_page.fill_header('Заголовок')
        leadforms_page.fill_description('Описание')
        leadforms_page.click_site()
        leadforms_page.fill_site('https://you-note.ru')
        leadforms_page.click_phone()
        leadforms_page.fill_phone('+77777777777')
        leadforms_page.click_promocode()
        leadforms_page.fill_promocode('promo')
        leadforms_page.click_continue()

        leadforms_page.click_notify()
        leadforms_page.fill_notify_email('dont_read_it@mail.ru')
        leadforms_page.fill_name('Имя')
        leadforms_page.fill_address('Адрес')
        leadforms_page.fill_email('dont_read_it@mail.ru')
        leadforms_page.fill_inn('ИНН')
        leadforms_page.click_continue()

        assert leadforms_page.get_form_name() == 'Имя'

        leadforms_page.remove_lead_form()

    def test_negative_compact_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_empty_data()
        leadforms_page.click_continue()

        logo_empty = self.find(self.locators.ERROR_1_LOGO)
        company_name_empty = self.find(self.locators.ERROR_1_COMPANY)
        title_empty = self.find(self.locators.ERROR_1_HEADING)
        description_empty = self.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Обязательное поле'
        assert logo_empty.text == expected_message, f"Expected '{expected_message}', got '{logo_empty.text}'"
        assert company_name_empty.text == expected_message, f"Expected '{expected_message}', got '{company_name_empty.text}'"
        assert title_empty.text == expected_message, f"Expected '{expected_message}', got '{title_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def test_negative_contacts_error(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form()
        leadforms_page.click_last_image()
        leadforms_page.click_continue()

        leadforms_page.click_bin_name()
        leadforms_page.click_bin_phone()

        error = self.find(self.locators.ERROR_2_CONTACT)

        expected_message = 'Минимальное количество полей: 1'
        assert error.text == expected_message, f"Expected '{expected_message}', got '{error.text}'"

    def test_negative_add_question_errors(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form()
        leadforms_page.click_last_image()
        leadforms_page.click_continue()
        leadforms_page.click_continue()

        leadforms_page.fill_empty_header()
        leadforms_page.click_continue()

        heading_empty = self.find(self.locators.ERROR_3_HEADING)

        expected_message = 'Обязательное поле'
        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"

        leadforms_page.fill_header('a' * 26)
        leadforms_page.fill_description('a' * 161)
        leadforms_page.click_continue()

        heading_empty = self.find(self.locators.ERROR_3_HEADING)
        description_empty = self.find(self.locators.ERROR_3_DESCRIPTION)

        expected_message = 'Превышена максимальная длина поля'
        assert heading_empty.text == expected_message, f"Expected '{expected_message}', got '{heading_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"

    def test_negative_empty_data(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_form()
        leadforms_page.click_last_image()
        leadforms_page.click_continue()
        leadforms_page.click_continue()
        leadforms_page.click_continue()

        leadforms_page.empty_name()
        leadforms_page.empty_address()
        leadforms_page.click_continue()

        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)

        expected_message = 'Обязательное поле'
        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"

        leadforms_page.fill_name('a' * 256)
        leadforms_page.fill_address('a' * 256)
        leadforms_page.fill_inn('a' * 33)
        leadforms_page.click_continue()

        name_input = self.find(self.locators.ERROR_4_NAME)
        address_input = self.find(self.locators.ERROR_4_ADDRESS)

        expected_message = 'Превышена максимальная длина поля'
        assert name_input.text == expected_message, f"Expected '{expected_message}', got '{name_input.text}'"
        assert address_input.text == expected_message, f"Expected '{expected_message}', got '{address_input.text}'"

        leadforms_page.fill_email('a')

        email_input = self.find(self.locators.ERROR_4_EMAIL)

        expected_message = 'Некорректный email адрес'
        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"

        leadforms_page.click_notify()
        leadforms_page.fill_notify_email('a')
        leadforms_page.click_continue()

        email_input = self.find(self.locators.ERROR_4_NOTIFY_EMAIL)

        expected_message = 'Поле содержит невалидный email адрес'
        assert email_input.text == expected_message, f"Expected '{expected_message}', got '{email_input.text}'"
