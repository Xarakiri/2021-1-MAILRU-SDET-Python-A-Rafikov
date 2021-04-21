import os
import string
from random import choices, randint

import allure
import pytest

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

        segment_page.click_create_segment()

        segment_name = ''.join(choices(string.ascii_letters, k=randint(4, 11)))

        self.logger.info(f'Creating segment "{segment_name}".')
        with allure.step(f'Creating segment "{segment_name}".'):
            segment_page.send_segment_name(segment_name)
        segment_page.click_create()
        return segment_page, segment_name

    @pytest.fixture
    def login(self):
        self.base_page.login()
        yield MainPage(driver=self.driver)

    @allure.epic('All tests')
    @allure.feature('UI tests')
    @allure.story('Test negative login1')
    @allure.description('Negative test with invalid username.')
    @pytest.mark.UI
    def test_negative_login1(self):
        self.base_page.login(
            username=''.join(choices(string.ascii_letters, k=randint(2, 10))) + '@' +
                     ''.join(choices(string.ascii_letters, k=randint(2, 10))) + '.ru'
        )
        error_msg = self.base_page.find(self.base_page.locators.ERROR_MSG)
        assert error_msg is not None

    @allure.epic('All tests')
    @allure.feature('UI tests')
    @allure.story('Test negative login2')
    @allure.description('Negative test with invalid password.')
    @pytest.mark.UI
    def test_negative_login2(self):
        self.base_page.login(
            password=''.join(choices(string.ascii_letters, k=randint(2, 10)))
        )
        error_msg = self.base_page.find(self.base_page.locators.ERROR_MSG)
        assert error_msg is not None

    @allure.epic('All tests')
    @allure.feature('UI tests')
    @allure.story('Test create new campaign')
    @allure.description("""Test for creating an advertising campaign 
                        of any type and check that it is created""")
    @pytest.mark.UI
    def test_create_new_campaign(self, login, file_path):
        main_page = login

        main_page.click_create_traffic_campaign()

        url = ''.join(choices(string.ascii_lowercase, k=randint(4, 11))) + '.ru'
        self.logger.info(f'Inputting campaign url {url}.')
        with allure.step(f'Inputting campaign url {url}.'):
            main_page.send_campaign_url(url)

        campaign_name = ''.join(choices(string.ascii_lowercase, k=randint(4, 11)))
        self.logger.info(f'Inputting campaign name {campaign_name}.')
        with allure.step(f'Inputting campaign name {campaign_name}.'):
            main_page.send_campaign_name(campaign_name)

        self.logger.info(f'Downloading photo.')
        with allure.step(f'Downloading photo.'):
            main_page.upload_photo(file_path)

        main_page.click_create_campaign_button()

        campaign = main_page.find_campaign(campaign_name)

        assert campaign is not None

        self.logger.info(f'Deleting campaign {campaign_name}')
        with allure.step(f'Deleting campaign {campaign_name}'):
            main_page.delete_campaign(campaign_name)

        assert main_page.is_campaign_deleted(campaign_name)

    @allure.epic('All tests')
    @allure.feature('UI tests')
    @allure.story('Test create new segment')
    @allure.description("""test for creating a segment in audiences 
                        and check that the segment is created""")
    @pytest.mark.UI
    def test_create_new_segment(self, create_segment):
        segment_page, segment_name = create_segment

        segment_in_list = segment_page.find_segment(segment_name)
        assert segment_in_list is not None

        self.logger.info(f'Deleting segment {segment_name}.')
        with allure.step(f'Deleting segment {segment_name}.'):
            segment_page.delete_segment(segment_name)

        segment_deleted_notification = segment_page.find_segment_deleted_notification()
        assert segment_deleted_notification is not None

    @allure.epic('All tests')
    @allure.feature('UI tests')
    @allure.story('Test delete segment')
    @allure.description('segment deletion test')
    @pytest.mark.UI
    def test_delete_segment(self, create_segment):
        segment_page, segment_name = create_segment

        self.logger.info(f'Deleting segment {segment_name}.')
        with allure.step(f'Deleting segment {segment_name}.'):
            segment_page.delete_segment(segment_name)

        segment_deleted_notification = segment_page.find_segment_deleted_notification()
        assert segment_deleted_notification is not None
