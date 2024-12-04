from cases import LoggedCase
from ui.pages.sites_page import SitePage
import pytest
import random


class TestSitePage(LoggedCase):
    INVALID_DOMAIN = "INVALID_DOMAIN"
    ERROR_MSG_INVALID_DOMAIN = "Введите корректный адрес сайта (вида: example.ru)"
    NOTHING_FIND_TEXT = "Ничего не найдено"

    EXISTED_DOMAIN = "you-note.ru"

    NEW_DOMAIN = f"you-note{random.randint(100, 1000)}.ru"
    UPDATE_DOMAIN = "update-domain.ru"
    STATUS_DONT_ARRIVE = "Данные не поступают"
    STATUS_ACCESS_REQUESTED = "Доступ запрошен"

    ID = "3518620"
    EMAIL = "sachatarba@rambler.ru"

    ONE_EXISTED_DOMAIN = "you-note100.ru"
    TWO_EXISTED_DOMAIN = "etotopchel.com"

    @pytest.fixture(scope='function', autouse=True)
    def setup_site_page(self):
        self.main_page.click_redirect_to_site_page()
        self.site_page = SitePage(self.driver)

    def test_pixel_create_delete(self):
        self.site_page.BUTTON_CREATE_PIXEL.clicks()
        self.site_page.INPUT_FIELD_DOMAIN_NAME.write(self.NEW_DOMAIN)
        self.site_page.FRAME_BUTTON.clicks()
        self.site_page.BUTTON_CLOSE_MODAL.clicks()
        self.site_page.SEARCH_INPUT_FIELD.write(self.NEW_DOMAIN)
        raw = self.site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert self.site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        self.site_page.open_delete_modal()
        self.site_page.BUTTON_DELETE.clicks()

        self.site_page.BUTTON_CREATE_PIXEL

    def test_input_existed_domain(self):
        self.site_page.BUTTON_CREATE_PIXEL.clicks()
        self.site_page.INPUT_FIELD_DOMAIN_NAME.write(self.ONE_EXISTED_DOMAIN)

        self.site_page.FRAME_BUTTON.clicks()
        self.site_page.BUTTON_ACCESS.clicks()
        self.site_page.INPUT_EMAIL_OWNER_INPUT.write(self.EMAIL)
        self.site_page.CONFIRM_ACCESS_BUTTON.clicks()
        self.site_page.BUTTON_CLOSE_MODAL.clicks()

        self.site_page.SEARCH_INPUT_FIELD.write(self.ONE_EXISTED_DOMAIN)
        raw = self.site_page.PIXEL_RAW(self.ONE_EXISTED_DOMAIN)

        assert raw
        assert self.site_page.SPAN_PIXEL_NAME(raw, self.ONE_EXISTED_DOMAIN)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        self.site_page.open_delete_modal()
        self.site_page.BUTTON_DELETE.clicks()

        self.site_page.BUTTON_CREATE_PIXEL

    def test_input_two_existed_domain(self):
        self.site_page.BUTTON_CREATE_PIXEL.clicks()
        self.site_page.INPUT_FIELD_DOMAIN_NAME.write(self.TWO_EXISTED_DOMAIN)
        self.site_page.FRAME_BUTTON.clicks()
        self.site_page.BUTTON_ACCESS.clicks()
        self.site_page.INPUT_EMAIL_OWNER_INPUT.write(self.EMAIL)
        self.site_page.CONFIRM_ACCESS_BUTTON.clicks()
        self.site_page.BUTTON_CLOSE_MODAL.clicks()

        self.site_page.SEARCH_INPUT_FIELD.write(self.TWO_EXISTED_DOMAIN)
        raw = self.site_page.PIXEL_RAW(self.TWO_EXISTED_DOMAIN)

        assert raw
        assert self.site_page.SPAN_PIXEL_NAME(raw, self.TWO_EXISTED_DOMAIN)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        self.site_page.open_delete_modal()
        self.site_page.BUTTON_DELETE.clicks()

        self.site_page.BUTTON_CREATE_PIXEL

    def test_create_delete_pixel_by_id(self):
        self.site_page.BUTTON_CREATE_PIXEL.clicks()
        self.site_page.BUTTON_CREATE_PIXEL_BY_ID.clicks()
        self.site_page.INPUT_EMAIL_OWNER.write(self.EMAIL)
        self.site_page.INPUT_FIELD_PIXEL_ID.write(self.ID)
        self.site_page.FRAME_BUTTON.clicks()
        self.site_page.BUTTON_CLOSE_MODAL.clicks()

        self.site_page.SEARCH_INPUT_FIELD.write(self.ID)
        raw = self.site_page.PIXEL_RAW_BY_ID(self.ID)

        assert raw
        assert self.site_page.DIV_PIXEL_ID(raw, self.ID)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        self.site_page.open_delete_modal()
        self.site_page.BUTTON_DELETE.clicks()

        self.site_page.BUTTON_CREATE_PIXEL

    def test_pixel_search(self):
        self.site_page.BUTTON_CREATE_PIXEL.clicks()
        self.site_page.INPUT_FIELD_DOMAIN_NAME.write(self.NEW_DOMAIN)
        self.site_page.FRAME_BUTTON.clicks()
        self.site_page.BUTTON_CLOSE_MODAL.clicks()

        search = self.site_page.SEARCH_INPUT_FIELD
        search.write(self.NEW_DOMAIN)
        raw = self.site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert self.site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        search.write("")
        self.site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write(self.NEW_DOMAIN[:2])
        raw = self.site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert self.site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert self.site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        search.write("")
        self.site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write(self.INVALID_DOMAIN)

        assert self.site_page.NOT_FOUND_PIXEL_MESSAGE == self.NOTHING_FIND_TEXT

        search.write("")
        self.site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write("")

        self.site_page.open_delete_modal()
        self.site_page.BUTTON_DELETE.clicks()

        self.site_page.BUTTON_CREATE_PIXEL