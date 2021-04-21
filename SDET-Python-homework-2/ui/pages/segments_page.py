from ui.locators.pages_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage


class SegmentPage(BasePage):
    locators = SegmentsPageLocators()

    def click_create_segment(self):
        self.click(self.locators.CREATE_SEGMENT_BTN)
        self.click(self.locators.GAMES_SEGMENT)
        self.click(self.locators.GAMES_SEGMENT_CBX)
        self.click(self.locators.ADD_SEGMENT_BTN)

    def click_create(self):
        self.click(self.locators.CREATE_SEGMENT_BTN)

    def send_segment_name(self, segment_name):
        self.click(self.locators.SEGMENT_NAME_INPUT)
        self.send_keys(
            self.locators.SEGMENT_NAME_INPUT,
            segment_name
        )

    def find_segment(self, segment_name):
        segment_in_list = self.find(
            (self.locators.SEGMENT_IN_LIST[0],
             self.locators.SEGMENT_IN_LIST[1].format(segment_name))
        )
        return segment_in_list

    def delete_segment(self, segment_name):
        self.click(
            (self.locators.CHECK_SEGMENT[0],
             self.locators.CHECK_SEGMENT[1].format(segment_name))
        )
        self.click(self.locators.ACTION_LIST)
        self.click(self.locators.DELETE_BUTTON)

    def find_segment_deleted_notification(self):
        segment_deleted_notification = self.find(self.locators.SEGMENT_DELETED_NOTIFICATION)
        return segment_deleted_notification
