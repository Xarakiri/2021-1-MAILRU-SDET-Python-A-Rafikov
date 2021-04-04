import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']

    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())

    browser.maximize_window()
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)
