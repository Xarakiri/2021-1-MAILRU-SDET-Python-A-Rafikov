from ui.locators.pages_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentPage


class MainPage(BasePage):
    locators = MainPageLocators()

    def is_company_deleted(self, campaign_name):
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
        self.click(self.locators.SEGMENTS_BUTTON)
        return SegmentPage(driver=self.driver)
