import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage


class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')

        self.logger.debug('Initial setup done!')
