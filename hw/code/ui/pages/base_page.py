import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None) -> list[WebElement]:
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def clear(self, locator, timeout: float | None = None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()

        if elem.get_attribute('value') != '':
            size = len(elem.get_attribute('value'))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    def fill(self, locator, keys):
        self.find(locator).send_keys(keys)

    def fill_in(self, locator, query: str, timeout: float | None = None) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def find_invisible(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))