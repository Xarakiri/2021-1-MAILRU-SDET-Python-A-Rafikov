import string
import time
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

    def test_logout(self, login):
        time.sleep(3)
        account_btn = self.find(basic_locators.ACCOUNT_BUTTON_LOCATOR)
        account_btn.click()

        exit_btn = self.find(basic_locators.EXIT_BUTTON_LOCATOR)
        exit_btn.click()

        assert self.driver.current_url == 'https://target.my.com/'

    def test_edit_contact_information(self, login):
        time.sleep(3)
        profile_btn = self.find(basic_locators.PROFILE_LOCATOR)
        profile_btn.click()
        time.sleep(3.5)

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

        save_btn = self.find(basic_locators.SAVE_BUTTON_LOCATOR)
        save_btn.click()

        self.driver.refresh()
        time.sleep(3)

        fio_input = self.find(basic_locators.FIO_LOCATOR)
        phone_input = self.find(basic_locators.PHONE_LOCATOR)
        email_input = self.find(basic_locators.EMAIL_LOCATOR)

        assert fio_input.get_attribute('value') == new_fio
        assert phone_input.get_attribute('value') == new_phone
        assert email_input.get_attribute('value') == new_email

    @pytest.mark.parametrize(
        'locator, url',
        [
            (
                basic_locators.STATISTIC_PAGE_LOCATOR,
                'https://target.my.com/statistics/summary'),
            (
                basic_locators.BILLING_PAGE_LOCATOR,
                'https://target.my.com/billing#deposit',
            ),
        ]
    )
    def test_go_page(self, login, locator, url):
        time.sleep(3)
        to_go = self.find(locator)
        to_go.click()
        time.sleep(3)
        assert self.driver.current_url == url
