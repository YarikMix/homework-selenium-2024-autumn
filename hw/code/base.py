import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.main_page import MainPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            credentials = request.getfixturevalue("credentials")
            driver.get(MainPage.url)
            MainPage(driver).login(*credentials)