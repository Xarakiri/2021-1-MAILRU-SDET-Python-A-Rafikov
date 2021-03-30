import string
from random import choices, randint

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

        self.send_keys(basic_locators.LOGIN_INPUT_LOCATOR, username)
        self.send_keys(basic_locators.PASSWORD_INPUT_LOCATOR,
                       password, Keys.ENTER)

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

        new_fio = ''.join(choices(string.ascii_letters, k=randint(4, 10)))
        self.send_keys(basic_locators.FIO_LOCATOR, new_fio)

        new_phone = ''.join(choices(string.digits, k=11))
        self.send_keys(basic_locators.PHONE_LOCATOR, new_phone)

        new_email = ''.join(choices(string.ascii_letters, k=randint(4, 10))) + \
            '@' + ''.join(choices(string.ascii_letters,
                                  k=randint(4, 10))) + '.ru'
        self.send_keys(basic_locators.EMAIL_LOCATOR, new_email)

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
        'button_locator, item_locator, url',
        [
            (
                basic_locators.STATISTIC_PAGE_LOCATOR,
                basic_locators.STATISTIC_CONSTRUCTOR_LOCATOR,
                'https://target.my.com/statistics/summary'),
            (
                basic_locators.BILLING_PAGE_LOCATOR,
                basic_locators.BILLING_DEPOSIT_PAYMENT_LOCATOR,
                'https://target.my.com/billing#deposit',
            ),
        ]
    )
    def test_go_page(self, login, button_locator, item_locator, url):
        self.click(button_locator, 10)
        item = self.find(item_locator)
        assert item != None
        assert self.driver.current_url == url
