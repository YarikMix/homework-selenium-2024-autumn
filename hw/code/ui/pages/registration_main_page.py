from ui.pages.base_page import BasePage
from ui.locators.registration_main_page_locators import RegistrationMainPageLocators


class RegistrationMainPage(BasePage):
    locators = RegistrationMainPageLocators()
    url = "https://ads.vk.com/hq/registration"

    page_text = {
        "Русский": {
            "MAIN_PAGE_TITLE": "Добро пожаловать\nв VK Рекламу",
            "MAIN_PAGE_SUBTITLE": "Перенесите настройки и кампании из существующего рекламного кабинета или создайте новый",
            "CREATE_CABINET": "Создать новый кабинет",
            "IMPORT_MYTARGET": "Использовать рекламный кабинет myTarget",
            "IMPORT_MYTARGET_HINT_ITEMS": [
                "Будут использованы настройки кабинета myTarget и реквизиты",
                "Все мобильные приложения будут привязаны к новому кабинету",
                "Вы сможете использовать аудитории myTarget в кабинете VK Рекламы",
                "Вы сможете копировать кампании из myTarget в новый кабинет",
            ],
        },
        "English": {
            "MAIN_PAGE_TITLE": "Welcome \nto VK Ads",
            "MAIN_PAGE_SUBTITLE": "Transfer settings and campaigns from an existing account or create a new one",
            "CREATE_CABINET": "Create a new account",
            "IMPORT_MYTARGET": "Use myTarget ad account",
            "IMPORT_MYTARGET_HINT_ITEMS": [
                "MyTarget account settings and details will be used",
                "All mobile applications will be linked to the new account",
                "You will be able to use myTarget audiences in your VK Advertising account",
                "You will be able to copy campaigns from myTarget to a new account",
            ],
        },
    }

    def language_options_became_visible(self) -> bool:
        return self.became_visible(self.locators.TEXT("Русский")) & self.became_visible(
            self.locators.TEXT("English")
        )

    def language_text_became_visible(self, language: str):
        return (
            self.became_visible(
                self.locators.TEXT(self.page_text[language]["MAIN_PAGE_TITLE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["MAIN_PAGE_SUBTITLE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["CREATE_CABINET"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["IMPORT_MYTARGET"])
            )
            & self.check_mytarget_hint_contents(language)
        )

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)

    def image_became_visible(self):
        return self.became_visible(self.locators.REGISTRATION_IMAGE)

    def click_image(self):
        self.click(self.locators.REGISTRATION_IMAGE)

    def hover_image(self):
        self.hover(self.locators.REGISTRATION_IMAGE)

    def language_switch_became_visible(self):
        return self.became_visible(self.locators.LANGUAGE_SWITCH)

    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text

    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))

    def main_page_title_became_visible(self):
        return self.became_visible(self.locators.MAIN_PAGE_TITLE)

    def main_page_subtitle_became_visible(self):
        return self.became_visible(self.locators.MAIN_PAGE_SUBTITLE)

    def create_new_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.CREATE_NEW_CABINET_BUTTON)

    def import_mytarget_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.IMPORT_MYTARGET_CABINET_BUTTON)

    def click_create_new_cabinet_button(self):
        self.click(self.locators.CREATE_NEW_CABINET_BUTTON)

    def click_import_mytarget_cabinet_button(self):
        self.click(self.locators.IMPORT_MYTARGET_CABINET_BUTTON)

    def hover_import_mytarget_cabinet_button_hint(self):
        self.hover(self.locators.IMPORT_MYTARGET_CABINET_BUTTON_HINT)

    def mytarget_hint_became_visible(self):
        return self.became_visible(self.locators.IMPORT_MYTARGET_CABINET_BUTTON_HINT)

    def check_mytarget_hint_contents(self, language: str) -> bool:
        self.hover_import_mytarget_cabinet_button_hint()
        check = True
        for item in self.page_text[language]["IMPORT_MYTARGET_HINT_ITEMS"]:
            check &= self.became_visible(self.locators.TEXT(item))
        self.hover_image()
        return check
