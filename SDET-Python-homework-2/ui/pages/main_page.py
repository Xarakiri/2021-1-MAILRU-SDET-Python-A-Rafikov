import logging

import allure
from selenium.common.exceptions import TimeoutException

from ui.locators.pages_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentPage

logger = logging.getLogger('test')


class MainPage(BasePage):
    locators = MainPageLocators()

    def is_campaign_deleted(self, campaign_name):
        logger.info(f'Deleting campaign "{campaign_name}".')
        with allure.step(f'Deleting campaign "{campaign_name}".'):
            campaign = self.find(
                (self.locators.CAMPAIGN_ROW[0],
                 self.locators.CAMPAIGN_ROW[1].format(campaign_name))
            )
            row_id = campaign.get_attribute('data-row-id')
            deleted = self.find(
                (self.locators.TRANSLATION[0],
                 self.locators.TRANSLATION[1].format(row_id))
            )
        return deleted is not None

    def go_to_segment_page(self):
        logger.info('Going to segments page.')
        self.click(self.locators.SEGMENTS_BUTTON)
        return SegmentPage(driver=self.driver)

    def click_create_traffic_campaign(self):
        try:
            self.click(self.locators.NEW_USER_CAMPAIGN)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN)
        self.click(self.locators.TRAFFIC_CAMPAIGN)

    def send_campaign_url(self, url):
        self.send_keys(self.locators.URL_INPUT, url)

    def send_campaign_name(self, campaign_name):
        self.click(self.locators.CAMPAIGN_NAME_INPUT)
        self.send_keys(self.locators.CAMPAIGN_NAME_INPUT, campaign_name)

    def upload_photo(self, file_path):
        self.click(self.locators.BANNER_BUTTON)

        input_field = self.find(self.locators.INPUT_IMAGE, timeout=20)
        self.scroll_to(input_field)
        input_field.send_keys(file_path)
        self.click(self.locators.SAVE_IMAGE, timeout=20)

    def click_create_campaign_button(self):
        self.click(self.locators.CREATE_CAMPAIGN)

    def find_campaign(self, campaign_name):
        campaign = self.find((self.locators.CHECK_CAMPAIGN[0],
                              self.locators.CHECK_CAMPAIGN[1].format(campaign_name)))
        return campaign

    def delete_campaign(self, campaign_name):
        self.click(
            (self.locators.CAMPAIGN_SETTINGS[0],
             self.locators.CAMPAIGN_SETTINGS[1].format(campaign_name)),
            timeout=30
        )
        self.click(self.locators.ACTION_LIST)
        self.click(self.locators.DELETE_BUTTON)

    def is_campaign_created(self, campaign_name):
        campaign = self.find_campaign(campaign_name)
        return campaign is not None
