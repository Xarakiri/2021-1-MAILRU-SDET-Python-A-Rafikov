from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
LOGIN_INPUT_LOCATOR = (By.NAME, 'email')
PASSWORD_INPUT_LOCATOR = (By.NAME, 'password')
ACCOUNT_BUTTON_LOCATOR = (By.CLASS_NAME, 'right-module-rightWrap-3lL6mf')
EXIT_BUTTON_LOCATOR = (By.XPATH, '//a[contains(text(), "Выйти")]')
PROFILE_LOCATOR = (By.XPATH, '//a[contains(@href,"profile")]')
FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
PHONE_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
EMAIL_LOCATOR = (By.XPATH, '//div[@class="js-additional-emails"]//input')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//button[@data-class-name="Submit"]')
STATISTIC_PAGE_LOCATOR = (By.XPATH, '//a[contains(@href,"statistics")]')
BILLING_PAGE_LOCATOR = (By.XPATH, '//a[contains(@href,"billing")]')
