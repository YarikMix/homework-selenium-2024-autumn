from selenium.webdriver.common.by import By


class OverviewPageChooseCampaignLocators:
    BUTTON_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[contains(@class, "FavoritesWidget_wrapper")]'
                                         '//button//*[contains(text(), "Выбрать кампании")]')
    SIGN_OPENING_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]')

    INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS = (By.CSS_SELECTOR, '[data-testid="search"')
    SIGN_SEARCH_NOT_FOUND_RESULTS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                               '//*[contains(text(), "Ничего не нашлось")]')
    SIGN_SEARCH_FOUND_RESULTS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                           '//*[contains(@class, "vkuiCheckbox__title")'
                                           ' and contains(text(), "Кампания")]')

    COUNTER_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                         '//*[contains(@class, "PlansSelector_desc")]')
    CHECKBOX_CHOOSE_CAMPAIGN_OFF = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                              '//*[contains(@class, "PlansSelector_list")]'
                                              '//*[contains(@class, "vkuiCheckbox__icon--off")]')
    CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP = (By.XPATH, '(//*[contains(@class, "PlansSelector_modal")]'
                                                      '//*[contains(@class, "PlansSelector_list")]'
                                                      '//*[contains(@class, "vkuiCheckbox__icon--off")])[6]')
    TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "Tooltip_tooltip") and'
                                                   ' contains(text(), "Выбрано максимальное количество кампаний")]')


class OverviewPageLocators:
    choose_campaign_locators = OverviewPageChooseCampaignLocators()

    WIDGET_CAMPAIGNS = \
        (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Кампании")]')
    WIDGET_BUDGET = (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Бюджет")]')
    WIDGET_LIMIT = \
        (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Лимит объявлений")]')
    WIDGET_FAVOURITES = (By.XPATH, '//*[contains(@class, "FavoritesWidget_wrapper")]//*[contains(text(),'
                                   ' "Избранные кампании")]')
    BUTTON_CREATE_CAMPAIGN = (By.CSS_SELECTOR, '[data-testid="create-button"]')
    BUTTON_BUDGET_REPLENISH = (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]'
                                         '//button//*[contains(text(), "Пополнить")]')
    BUTTON_LIMIT_ARTICLE = (By.CSS_SELECTOR, '[href="/help/articles/ad_limits"]')