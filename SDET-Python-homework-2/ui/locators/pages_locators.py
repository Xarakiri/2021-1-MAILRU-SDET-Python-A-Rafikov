from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOGIN_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_MSG = (By.XPATH, '//div[contains(text(), "Invalid login or password")]')
