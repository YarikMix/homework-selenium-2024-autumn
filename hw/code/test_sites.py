from ui.pages.sites_page import SitePage
from base import BaseCase
import pytest
import random


class TestSitePage(BaseCase):
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

    def test_pixel_create_delete(self, site_page : SitePage):
        site_page.BUTTON_CREATE_PIXEL.clicks()
        site_page.INPUT_FIELD_DOMAIN_NAME.write(self.NEW_DOMAIN)
        site_page.FRAME_BUTTON.clicks()
        site_page.BUTTON_CLOSE_MODAL.clicks()
        site_page.SEARCH_INPUT_FIELD.write(self.NEW_DOMAIN)
        raw = site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        site_page.open_delete_modal()
        site_page.BUTTON_DELETE.clicks()

        site_page.BUTTON_CREATE_PIXEL

    def test_input_existed_domain(self, site_page: SitePage):
        site_page.BUTTON_CREATE_PIXEL.clicks()
        site_page.INPUT_FIELD_DOMAIN_NAME.write(self.ONE_EXISTED_DOMAIN)

        site_page.FRAME_BUTTON.clicks()
        site_page.BUTTON_ACCESS.clicks()
        site_page.INPUT_EMAIL_OWNER_INPUT.write(self.EMAIL)
        site_page.CONFIRM_ACCESS_BUTTON.clicks()
        site_page.BUTTON_CLOSE_MODAL.clicks()

        site_page.SEARCH_INPUT_FIELD.write(self.ONE_EXISTED_DOMAIN)
        raw = site_page.PIXEL_RAW(self.ONE_EXISTED_DOMAIN)

        assert raw
        assert site_page.SPAN_PIXEL_NAME(raw, self.ONE_EXISTED_DOMAIN)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        site_page.open_delete_modal()
        site_page.BUTTON_DELETE.clicks()

        site_page.BUTTON_CREATE_PIXEL

    def test_input_two_existed_domain(self, site_page: SitePage):
        site_page.BUTTON_CREATE_PIXEL.clicks()
        site_page.INPUT_FIELD_DOMAIN_NAME.write(self.TWO_EXISTED_DOMAIN)
        site_page.FRAME_BUTTON.clicks()
        site_page.BUTTON_ACCESS.clicks()
        site_page.INPUT_EMAIL_OWNER_INPUT.write(self.EMAIL)
        site_page.CONFIRM_ACCESS_BUTTON.clicks()
        site_page.BUTTON_CLOSE_MODAL.clicks()

        site_page.SEARCH_INPUT_FIELD.write(self.TWO_EXISTED_DOMAIN)
        raw = site_page.PIXEL_RAW(self.TWO_EXISTED_DOMAIN)

        assert raw
        assert site_page.SPAN_PIXEL_NAME(raw, self.TWO_EXISTED_DOMAIN)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        site_page.open_delete_modal()
        site_page.BUTTON_DELETE.clicks()

        site_page.BUTTON_CREATE_PIXEL

    def test_create_delete_pixel_by_id(self, site_page: SitePage):
        site_page.BUTTON_CREATE_PIXEL.clicks()
        site_page.BUTTON_CREATE_PIXEL_BY_ID.clicks()
        site_page.INPUT_EMAIL_OWNER.write(self.EMAIL)
        site_page.INPUT_FIELD_PIXEL_ID.write(self.ID)
        site_page.FRAME_BUTTON.clicks()
        site_page.BUTTON_CLOSE_MODAL.clicks()

        site_page.SEARCH_INPUT_FIELD.write(self.ID)
        raw = site_page.PIXEL_RAW_BY_ID(self.ID)

        assert raw
        assert site_page.DIV_PIXEL_ID(raw, self.ID)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_ACCESS_REQUESTED)

        site_page.open_delete_modal()
        site_page.BUTTON_DELETE.clicks()

        site_page.BUTTON_CREATE_PIXEL

    def test_pixel_search(self, site_page: SitePage):
        site_page.BUTTON_CREATE_PIXEL.clicks()
        site_page.INPUT_FIELD_DOMAIN_NAME.write(self.NEW_DOMAIN)
        site_page.FRAME_BUTTON.clicks()
        site_page.BUTTON_CLOSE_MODAL.clicks()

        search = site_page.SEARCH_INPUT_FIELD
        search.write(self.NEW_DOMAIN)
        raw = site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        search.write("")
        site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write(self.NEW_DOMAIN[:2])
        raw = site_page.PIXEL_RAW(self.NEW_DOMAIN)

        assert raw
        assert site_page.SPAN_PIXEL_NAME(raw, self.NEW_DOMAIN)
        assert site_page.SPAN_PIXEL_STATUS(raw, self.STATUS_DONT_ARRIVE)

        search.write("")
        site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write(self.INVALID_DOMAIN)

        assert site_page.NOT_FOUND_PIXEL_MESSAGE == self.NOTHING_FIND_TEXT

        search.write("")
        site_page.BUTTON_CLEAR_SEARCH.clicks()
        search.write("")

        site_page.open_delete_modal()
        site_page.BUTTON_DELETE.clicks()

        site_page.BUTTON_CREATE_PIXEL