from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

from ui.pages.auth_page import AuthPage
from ui.pages.budget_page import BudgetPage
from ui.pages.company_page import CompanyPage
from ui.pages.overview_page import OverviewPage
from ui.pages.audience_page import AudiencePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.commerce_page import CommercePage
from ui.pages.registration_main_page import RegistrationMainPage
from ui.pages.leadform_page import LeadformPage
from ui.pages.sites_page import SitePage


@pytest.fixture()
def driver(config):
    url = config['url']
    opts = Options()
    service = Service(environ.get("CHROMEDRIVER_PATH"))
    driver = webdriver.Chrome(options=opts, service=service)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def credentials():
    return (environ.get("MAIL_LOGIN"), environ.get("MAIL_PASSWORD"))


@pytest.fixture()
def main_page(driver):
    driver.get(MainPage.url)
    return MainPage(driver)


@pytest.fixture()
def overview_page(driver):
    driver.get(OverviewPage.url)
    return OverviewPage(driver)


@pytest.fixture()
def audience_page(driver):
    driver.get(AudiencePage.url)
    return AudiencePage(driver)


@pytest.fixture()
def budget_page(driver):
    driver.get(BudgetPage.url)
    return BudgetPage(driver)


@pytest.fixture()
def settings_page(driver):
    driver.get(SettingsPage.url)
    return SettingsPage(driver)


@pytest.fixture
def commerce_page(driver, cabinet_page):
    driver.get(CommercePage.url)
    return CommercePage(driver=driver)



@pytest.fixture()
def company_page(driver):
    driver.get(CompanyPage.url)
    return CompanyPage(driver)


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture(scope="session")
def credentials_without_cabinet():
    return os.getenv("NEW_LOGIN"), os.getenv("NEW_PASSWORD")

@pytest.fixture
def registration_main_page(driver, credentials_without_cabinet, auth_page):
    driver.get(RegistrationMainPage.url)
    auth_page.login(*credentials_without_cabinet)
    return RegistrationMainPage(driver=driver)

@pytest.fixture
def leadform_page(driver, home_page):
    driver.get(LeadformPage.url)
    return LeadformPage(driver=driver)


@pytest.fixture
def site_page(driver):
    driver.get(SitePage.url)
    return SitePage(driver=driver)