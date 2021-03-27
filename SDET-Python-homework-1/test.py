import string
from random import choices

import pytest
from selenium.webdriver.common.keys import Keys

import basic_locators
from base import BaseCase


class Test(BaseCase):
    @pytest.fixture
    def login(self,
              username='rafikov.ds7777@mail.ru',
              password='RYnT84r-nVpwCx7'):
        self.click(basic_locators.LOGIN_LOCATOR)

        login_input = self.find(basic_locators.LOGIN_INPUT_LOCATOR)
        login_input.clear()
        login_input.send_keys(username)

        password_input = self.find(
            basic_locators.PASSWORD_INPUT_LOCATOR)
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)

    @pytest.mark.UI
    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self, login):
        self.click(basic_locators.ACCOUNT_BUTTON_LOCATOR)
        self.click(basic_locators.EXIT_BUTTON_LOCATOR)

        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_edit_contact_information(self, login):
        self.click(basic_locators.PROFILE_LOCATOR)

        fio_input = self.find(basic_locators.FIO_LOCATOR)
        fio_input.clear()
        new_fio = ''.join(choices(string.ascii_letters, k=6))
        fio_input.send_keys(new_fio)

        phone_input = self.find(basic_locators.PHONE_LOCATOR)
        phone_input.clear()
        new_phone = ''.join(choices(string.digits, k=11))
        phone_input.send_keys(new_phone)

        email_input = self.find(basic_locators.EMAIL_LOCATOR)
        email_input.clear()
        new_email = ''.join(choices(string.ascii_letters, k=5)) + '@' + \
                    ''.join(choices(string.ascii_letters, k=4)) + '.ru'
        email_input.send_keys(new_email)

        self.click(basic_locators.SAVE_BUTTON_LOCATOR)

        self.driver.refresh()

        fio_input = self.find(basic_locators.FIO_LOCATOR)
        phone_input = self.find(basic_locators.PHONE_LOCATOR)
        email_input = self.find(basic_locators.EMAIL_LOCATOR)

        assert fio_input.get_attribute('value') == new_fio
        assert phone_input.get_attribute('value') == new_phone
        assert email_input.get_attribute('value') == new_email

    @pytest.mark.UI
    @pytest.mark.parametrize(
        'locator, url',
        [
            (
                basic_locators.STATISTIC_PAGE_LOCATOR,
                'https://target.my.com/statistics'),
            (
                basic_locators.BILLING_PAGE_LOCATOR,
                'https://target.my.com/billing',
            ),
        ]
    )
    def test_go_page(self, login, locator, url):
        self.click(locator, 10)
        assert self.driver.current_url == url
