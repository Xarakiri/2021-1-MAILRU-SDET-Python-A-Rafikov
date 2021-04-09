import os
import string
from random import choices, randint

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from base_tests.base import BaseCase
from ui.pages.main_page import MainPage


class Test(BaseCase):
    @pytest.fixture(scope='function')
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'ui', 'test.png')

    @pytest.fixture
    def create_segment(self, login):
        main_page = login
        segment_page = main_page.go_to_segment_page()

        try:
            segment_page.click(segment_page.locators.CREATE_NEW)
        except TimeoutException:
            segment_page.click(segment_page.locators.ALREADY_CREATED)

        segment_page.click(segment_page.locators.GAMES_SEGMENT)
        segment_page.click(segment_page.locators.GAMES_SEGMENT_CBX)
        segment_page.click(segment_page.locators.ADD_SEGMENT_BTN)

        segment_name = ''.join(choices(string.ascii_letters, k=randint(4, 11)))

        segment_page.click(segment_page.locators.SEGMENT_NAME_INPUT)
        segment_page.send_keys(
            segment_page.locators.SEGMENT_NAME_INPUT,
            segment_name
        )
        segment_page.click(segment_page.locators.CREATE_SEGMENT_BTN)
        return segment_page, segment_name

    def _login(self,
               username='rafikov.ds7777@mail.ru',
               password='RYnT84r-nVpwCx7'):
        self.base_page.click(self.base_page.locators.LOGIN_BUTTON)
        self.base_page.send_keys(self.base_page.locators.LOGIN_INPUT, username)
        self.base_page.send_keys(self.base_page.locators.PASSWORD_INPUT,
                                 password, Keys.ENTER)

    def _delete_segment(self, segment_page, segment_name):
        segment_page.click(
            (segment_page.locators.CHECK_SEGMENT[0],
             segment_page.locators.CHECK_SEGMENT[1].format(segment_name))
        )
        segment_page.click(segment_page.locators.ACTION_LIST)
        segment_page.click(segment_page.locators.DELETE_BUTTON)

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

    def test_create_new_campaign(self, login, file_path):
        main_page = login
        try:
            main_page.click(main_page.locators.NEW_USER_CAMPAIGN)
        except TimeoutException:
            main_page.click(main_page.locators.CREATE_CAMPAIGN)

        main_page.click(main_page.locators.TRAFFIC_CAMPAIGN)
        url = ''.join(choices(string.ascii_lowercase, k=randint(4, 11))) + '.ru'
        main_page.send_keys(main_page.locators.URL_INPUT, url)

        campaign_name = ''.join(choices(string.ascii_lowercase, k=randint(4, 11)))
        main_page.click(main_page.locators.CAMPAIGN_NAME_INPUT)
        main_page.send_keys(main_page.locators.CAMPAIGN_NAME_INPUT, campaign_name)

        main_page.click(main_page.locators.BANNER_BUTTON)

        input_field = main_page.find(main_page.locators.INPUT_IMAGE, timeout=20)
        main_page.scroll_to(input_field)
        input_field.send_keys(file_path)

        main_page.click(main_page.locators.SAVE_IMAGE, timeout=20)

        main_page.click(main_page.locators.CREATE_CAMPAIGN)

        campaign = main_page.find((main_page.locators.CHECK_CAMPAIGN[0],
                                   main_page.locators.CREATE_CAMPAIGN[1].format(campaign_name)))

        assert campaign is not None

        main_page.click(
            (main_page.locators.CAMPAIGN_SETTINGS[0],
             main_page.locators.CAMPAIGN_SETTINGS[1].format(campaign_name)),
            timeout=30
        )
        main_page.click(main_page.locators.ACTION_LIST)
        main_page.click(main_page.locators.DELETE_BUTTON)

        assert main_page.is_company_deleted(campaign_name)

    def test_create_new_segment(self, create_segment):
        segment_page, segment_name = create_segment

        segment_in_list = segment_page.find(
            (segment_page.locators.SEGMENT_IN_LIST[0],
             segment_page.locators.SEGMENT_IN_LIST[1].format(segment_name))
        )
        assert segment_in_list is not None

        self._delete_segment(segment_page, segment_name)

        segment_deleted_notification = segment_page.find(segment_page.locators.SEGMENT_DELETED_NOTIFICATION)

        assert segment_deleted_notification is not None

    def test_delete_segment(self, create_segment):
        segment_page, segment_name = create_segment
        self._delete_segment(segment_page, segment_name)
        segment_deleted_notification = segment_page.find(segment_page.locators.SEGMENT_DELETED_NOTIFICATION)
        assert segment_deleted_notification is not None
