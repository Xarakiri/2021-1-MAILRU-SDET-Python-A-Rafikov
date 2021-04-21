from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOGIN_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_MSG = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class ListLocators:
    ACTION_LIST = (By.XPATH, '//span[contains(text(), "Действия")]')
    DELETE_BUTTON = (By.XPATH, '//li[@title="Удалить"]')


class MainPageLocators(ListLocators):
    NEW_USER_CAMPAIGN = (By.XPATH, '//a[text()="Создайте рекламную кампанию"]')
    CREATE_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    TRAFFIC_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Трафик")]')
    URL_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[@class="campaign-name"]//input')
    BANNER_BUTTON = (By.XPATH, '//div[@id="patterns_4"]')
    INPUT_IMAGE = (By.XPATH, '//input[@type="file"]')
    SAVE_IMAGE = (By.XPATH, '//input[@data-loc-ru="Сохранить изображение"]')
    CHECK_CAMPAIGN = (By.XPATH, '//a[contains(text(), "{}")]')
    CAMPAIGN_SETTINGS = (By.XPATH, '//a[contains(text(), {})]/../input')
    CAMPAIGN_ROW = (By.XPATH, '//a[contains(text(), "{}")]/parent::div/parent::div[@data-row-id]')
    TRANSLATION = (By.XPATH, '//div[@data-row-id="{}"]//span[contains(text(), "Кампания удалена")]')
    SEGMENTS_BUTTON = (By.XPATH, '//a[contains(text(), "Аудитории")]')


class SegmentsPageLocators(ListLocators):
    CREATE_NEW = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    ALREADY_CREATED = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    GAMES_SEGMENT = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    GAMES_SEGMENT_CBX = (By.XPATH, '//input[@type="checkbox"]')
    ADD_SEGMENT_BTN = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME_INPUT = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]//input')
    CREATE_SEGMENT_BTN = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    SEGMENT_IN_LIST = (By.XPATH, '//a[@title="{}"]')
    CHECK_SEGMENT = (By.XPATH, '//a[@title="{}"]/../../..//input')
    SEGMENT_DELETED_NOTIFICATION = (By.XPATH, '//div[contains(text(), "1 сегмент был удален.")]')