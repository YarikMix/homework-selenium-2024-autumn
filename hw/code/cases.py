import pytest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup_base_case(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)


@pytest.mark.usefixtures('setup_base_case')
class LoggedCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials):
        self.main_page = self.login_page.login(credentials)


@pytest.mark.usefixtures('setup_base_case')
class LoggedNewUserCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials_new_user):
        self.main_page = self.login_page.login(credentials_new_user)
