from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui.pages.budget_page import BudgetPage
from ui.pages.overview_page import OverviewPage
from ui.pages.audience_page import AudiencePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.commerce_page import CommercePage


@pytest.fixture()
def driver(config):
    url = config['url']
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=opts)
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
