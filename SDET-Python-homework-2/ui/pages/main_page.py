import logging

import allure

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
