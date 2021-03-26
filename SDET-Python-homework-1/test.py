import time

import pytest
from selenium.webdriver.common.keys import Keys

import basic_locators
from base import BaseCase


class Test(BaseCase):
    @pytest.fixture
    def login(self,
              username='rafikov.ds7777@mail.ru',
              password='RYnT84r-nVpwCx7'):
        time.sleep(3)
        enter_btn = self.find(basic_locators.LOGIN_LOCATOR)
        enter_btn.click()

        login_input = self.find(basic_locators.LOGIN_INPUT_LOCATOR)
        login_input.clear()
        login_input.send_keys(username)

        password_input = self.find(
            basic_locators.PASSWORD_INPUT_LOCATOR)
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)

    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'
