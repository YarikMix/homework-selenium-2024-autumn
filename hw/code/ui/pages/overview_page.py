from ui.pages.base_page import BasePage
from ui.locators.overview_locators import OverviewPageLocators



class OverviewPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewPageLocators()

    @property
    def WIDGET_CAMPAIGNS(self):
        return self.find_with_check_visibility(self.locators.WIDGET_CAMPAIGNS)

    @property
    def WIDGET_BUDGET(self):
        return self.find_with_check_visibility(self.locators.WIDGET_BUDGET)

    @property
    def WIDGET_LIMIT(self):
        return self.find_with_check_visibility(self.locators.WIDGET_LIMIT)

    @property
    def WIDGET_FAVOURITES(self):
        return self.find_with_check_visibility(self.locators.WIDGET_FAVOURITES)

    @property
    def BUTTON_CREATE_CAMPAIGN(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_CAMPAIGN)

    @property
    def BUTTON_BUDGET_REPLENISH(self):
        return self.find_with_check_visibility(self.locators.BUTTON_BUDGET_REPLENISH)

    @property
    def BUTTON_LIMIT_ARTICLE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_LIMIT_ARTICLE)

    def check_display(self):
        assert self.WIDGET_CAMPAIGNS
        assert self.WIDGET_BUDGET
        assert self.WIDGET_LIMIT
        assert self.WIDGET_FAVOURITES
        assert self.BUTTON_CREATE_CAMPAIGN
        assert self.BUTTON_BUDGET_REPLENISH
        assert self.BUTTON_LIMIT_ARTICLE

    @property
    def SIGN_SEARCH_NOT_FOUND_RESULTS(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.SIGN_SEARCH_NOT_FOUND_RESULTS)

    @property
    def SIGN_SEARCH_FOUND_RESULTS(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.SIGN_SEARCH_FOUND_RESULTS)

    @property
    def TOOLTIP_MAX_COUNT_CHOSE_CAMPAIGN(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN)

    @property
    def COUNTER_CHOOSE_CAMPAIGN(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.COUNTER_CHOOSE_CAMPAIGN)

    def get_current_count_chosen_campaigns(self):
        text_choose_campaign = self.COUNTER_CHOOSE_CAMPAIGN.text
        idx_counter = text_choose_campaign.find(' ')

        try:
            result = int(text_choose_campaign[idx_counter:idx_counter + 2])
        except ValueError:
            result = 0

        return result