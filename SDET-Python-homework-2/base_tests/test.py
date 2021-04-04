import string
from random import choices, randint

import pytest
from selenium.webdriver.common.keys import Keys

from base_tests.base import BaseCase
from ui.pages.main_page import MainPage


class Test(BaseCase):
    def _login(self,
               username='rafikov.ds7777@mail.ru',
               password='RYnT84r-nVpwCx7'):
        self.base_page.click(self.base_page.locators.LOGIN_BUTTON)
        self.base_page.send_keys(self.base_page.locators.LOGIN_INPUT, username)
        self.base_page.send_keys(self.base_page.locators.PASSWORD_INPUT,
                                 password, Keys.ENTER)

    @pytest.fixture
    def login(self):
        self._login()
        yield MainPage(driver=self.driver)

    def test_negative_login1(self):
        self._login(
            username=''.join(choices(string.ascii_letters, k=randint(2, 10))) + '@' +
                     ''.join(choices(string.ascii_letters, k=randint(2, 10))) + '.ru'
        )
        error_msg = self.base_page.find(self.base_page.locators.ERROR_MSG)
        assert error_msg != None

    def test_negative_login2(self):
        self._login(
            password=''.join(choices(string.ascii_letters, k=randint(2, 10)))
        )
        error_msg = self.base_page.find(self.base_page.locators.ERROR_MSG)
        assert error_msg != None
