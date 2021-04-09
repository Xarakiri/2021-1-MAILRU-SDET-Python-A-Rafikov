from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.pages_locators import BasePageLocators

CLICK_RETRY = 3


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, *query):
        search = self.find(locator)
        search.clear()
        for q in query:
            search.send_keys(q)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
