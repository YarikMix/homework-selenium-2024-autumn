from selenium.webdriver.common.by import By


class SettingsLocators:
    PHONE_LOCATOR = (By.CSS_SELECTOR, '[data-testid="general-phone"]')
    SAVE_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid="settings-save"]')
    CANCEL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid="settings-cancel"]')
    MUST_HAVE_FIELD = (By.XPATH, f'//div[text()="Обязательное поле"]')
    INVALID_PHONE_LOCATOR = (By.XPATH, f'//div[text()="Некорректный номер телефона"]')
    ADD_EMAIL_LOCATOR = (By.CSS_SELECTOR, '[data-testid="add-email"]')
    EXTRA_EMAIL_LOCATOR = (By.CSS_SELECTOR, '[data-testid="email-0"]')
    INVALID_EMAIL_LOCATOR = (By.XPATH, f'//div[text()="Некорректный email адрес"]')
    INN_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid="general-ord-inn"]')
    INVALID_INN_LOCATOR = (By.XPATH, f'//div[text()="Некорректный ИНН"]')
    SMALL_INN_LOCATOR = (By.XPATH, f'//div[text()="Длина ИНН должна быть 12 символов"]')
    LANGUAGE_SELECT_LOCATOR = (By.CSS_SELECTOR, '[data-testid="interface-language"]')
    ENGLISH_TEXT = (By.XPATH, f'//span[text()="EN"]')
    FIO_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid="general-ord-name"]')

    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")
