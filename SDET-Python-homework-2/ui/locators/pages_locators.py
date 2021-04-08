from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOGIN_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_MSG = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')


class MainPageLocators:
    NEW_USER_CAMPAIGN = (By.XPATH, '//a[text()="Создайте рекламную кампанию"]')
    CREATE_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    TRAFFIC_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Трафик")]')
    URL_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[@class="campaign-name"]//input')
    BANNER_BUTTON = (By.XPATH, '//div[@id="patterns_4"]')
    INPUT_IMAGE = (By.XPATH, '//input[@type="file"]')
    SAVE_IMAGE = (By.XPATH, '//input[@data-loc-ru="Сохранить изображение"]')
    CHECK_CAMPAIGN = (By.XPATH, '//a[contains(text(), {})]')
    CAMPAIGN_SETTINGS = (By.XPATH, '//a[contains(text(), {})]/../input')
    ACTION_LIST = (By.XPATH, '//span[contains(text(), "Действия")]')
    DELETE_CAMPAIGN_BUTTON = (By.XPATH, '//li[@title="Удалить"]')
    CAMPAIGN_ROW = (By.XPATH, '//a[contains(text(), "{}")]/parent::div/parent::div[@data-row-id]')
    TRANSLATION = (By.XPATH, '//div[@data-row-id="{}"]//span[contains(text(), "Кампания удалена")]')
