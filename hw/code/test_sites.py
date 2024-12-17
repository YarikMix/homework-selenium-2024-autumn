from ui.pages.sites_page import SitePage
from base import BaseCase
import random


class TestSitePage(BaseCase):
    EXISTED_DOMAIN = "you-note.ru"
    NEW_DOMAIN = f"you-note{random.randint(100, 1000)}.ru"

    def test_pixel_create(self, site_page: SitePage):
        site_page.create_pixel()
        site_page.set_pixel_name(self.NEW_DOMAIN)
        site_page.submit_pixel()

        site_page.close_create_pixel_modal()

        get_pixels = site_page.get_pixels()
        assert len(get_pixels) == 1
        assert self.NEW_DOMAIN in get_pixels