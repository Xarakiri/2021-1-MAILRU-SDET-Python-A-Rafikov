from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
LOGIN_INPUT_LOCATOR = (By.NAME, 'email')
PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
ACCOUNT_BUTTON_LOCATOR = (By.CLASS_NAME, 'right-module-rightWrap-3lL6mf')
EXIT_BUTTON_LOCATOR = (By.XPATH, '//a[contains(text(), "Выйти")]')
