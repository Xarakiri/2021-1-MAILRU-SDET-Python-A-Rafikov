import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import logging
import os
import allure
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


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f'{i["level"]} - {i["source"]}\n{i["message"]}\n\n')

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
