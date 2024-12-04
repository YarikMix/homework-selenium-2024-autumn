from selenium.webdriver.common.by import By


class TrainingPageSharedLocators:
    SIGN_OPENING_MODAL_VIEW = (By.ID, '_modal_24')


class SitePageLocators:
    SIGN_OPENNING_SITE = (By.ID, "pixels")

    LABEL_ID_PIXEL = (By.XPATH, '//h4[text()="ID пикселя"]')

    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Поиск"]')
    PIXEL_ID_INPUT = (By.XPATH, '//input[@placeholder="ID пикселя"]')
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email владельца"]')
    DOMAIN_INPUT = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    PIXEL_HREF_LINK = (By.XPATH, '//a[contains(@href="/hq/pixels")]')

    BUTTON_ADD_PIXEL = (By.XPATH, "//button[contains(@class, 'vkuiButton')]")
    BUTTON_CREATE_NEW_PIXEL = (By.XPATH, "//span[text()='Добавить пиксель']")
    BUTTON_SUBMIT_UPDATE = (By.XPATH, '//button[@data-testid="submit"]')
    BUTTON_UPDATE = (By.XPATH, '//span[text()="Изменить"]')
    BUTTON_CLOSE_MODAL = (By.XPATH, '//div[@aria-label="Закрыть"]')
    BUTTON_DELETE_CONFIRM = (By.XPATH, '//div[contains(@class, "vkuiButtonGroup")]//button[last()]')
    BUTTON_CREATE_COPY_PIXEL = (By.XPATH, '//span[text()="Создать новый пиксель"]')

    TEXT_ADD_PIXEL_HEADER = (By.XPATH, '//*[text()="Добавление пикселя"]')
    TEXT_CREATE_PIXEL_ID_CONFIRM = (By.XPATH, '//h2[text()="Создан ID пикселя"]')
    TEXT_NO_PIXELS_FOUND = (By.XPATH, '//h2[text()="Нет привязанных пикселей трекинга"]')
    TEXT_NOTHING_FOUND = (By.XPATH, '//h2[text()="Ничего не найдено"]')
    TEXT_PIXEL_DOMAIN_FOUND = (By.XPATH, '//span[text()="Kopilka"]')
    ERROR_DOMAIN_INPUT = (By.XPATH, "//span[text()='Введите корректный адрес сайта (вида: example.ru)']")
    MESSAGE_PIXEL_FOUND = (By.XPATH, "//div[contains(@class, 'FlowSelectStep_header__')]")

    FRAME_MODEL_PIXEL = (By.XPATH, '//div[contains(@class, "vkui__portal-root")]')
    BUTTON_GROUP_IFRAME = (By.XPATH, '//div[contains(@class, "vkuiButtonGroup")]/button')

    BUTTON_MENU_MORE = (By.XPATH, '//button[@aria-label="More"]')
    ELEMENT_TABLE_DOMAIN = (By.XPATH, "//div[contains(@class, 'BaseTable__row-cell') and"
                                      " contains(@style, 'width: 50px')]")

    DROPDOWN_MENU_DELETE = (By.XPATH, '//div[contains(@class, "ContextMenu_dropdown__")]//label[last()]')
    DROPDOWN_MENU_UPDATE = (By.XPATH, '//div[contains(@class, "ContextMenu_dropdown__")]//label[1]')
    INPUT_PIXEL_NAME_UPDATE = (By.XPATH, '//input[@name="name"]')

    @staticmethod
    def PIXEL_ROW(name):
        return (By.XPATH, f'//div[contains(@class, "PixelsList__row")]//span[text()="{name}"]')

    @staticmethod
    def PIXEL_ROW_BY_ID(id):
        return (By.XPATH, f'//div[contains(@class, "PixelsList__row")]//div[text()="{id}"]')

    BUTTON_REQUEST_ACCESS = (By.XPATH, '//span[text()="Запросить доступ к пикселю"]')
    BUTTON_REQUEST = (By.XPATH, '//span[text()="Запросить доступ"]')
    INPUT_EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Введите email"]')
    BUTTON_CLEAR = (By.XPATH, '//button[@aria-label="Очистить"]')

    @staticmethod
    def PIXEL_NAME(name):
        return (By.XPATH, f'.//span[text()="{name}"]')

    @staticmethod
    def PIXEL_ID(id):
        return (By.XPATH, f'.//div[text()="{id}"]')

    @staticmethod
    def PIXEL_STATUS(status="Данные не поступают"):
        return (By.XPATH, f'.//span[text()="{status}"]')