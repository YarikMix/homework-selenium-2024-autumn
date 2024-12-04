import pytest

from cases import LoggedNewUserCase, LoggedCase
from ui.pages.overview_page import  OverviewPage


class TestNewUserOverview(LoggedNewUserCase):

    def test_display(self):
        self.overview_new_user_page.check_display_start_actions()


class TestOverview(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_overview(self, driver):
        self.overview_page = OverviewPage(self.driver)
        self.max_count_campaigns = 5

    def test_display(self):
        self.overview_page.check_display()

    @pytest.fixture(scope="function")
    def setup_choose_campaigns(self):
        self.overview_page.BUTTON_CHOOSE_CAMPAIGNS.open_view()

    @pytest.mark.parametrize('query, view',
                             [
                                 pytest.param(
                                     "asdfasdf",
                                     lambda overview_page: overview_page.SIGN_SEARCH_NOT_FOUND_RESULTS,
                                 ),
                                 pytest.param(
                                     "Кампания",
                                     lambda overview_page: overview_page.SIGN_SEARCH_FOUND_RESULTS,
                                 )
                             ], 
                            )
    
    def test_search_in_choose_campaigns(self, setup_choose_campaigns, query, view):
        self.overview_page.INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS.write(query)

        assert view(self.overview_page)

    def test_tooltip_max_count_campaigns(self, setup_choose_campaigns):
        count_choose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        self.overview_page.activate_amount_campaigns(self.max_count_campaigns - count_choose_campaigns)

        self.overview_page.CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP.hover()
        assert self.overview_page.TOOLTIP_MAX_COUNT_CHOSE_CAMPAIGN