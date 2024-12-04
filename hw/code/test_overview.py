import pytest
from base import BaseCase
from ui.pages.overview_page import  OverviewPage


class TestOverview(BaseCase):
    def test_display(self, overview_page: OverviewPage):
        overview_page.check_display()

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
    
    def test_search_in_choose_campaigns(self, query, view, overview_page: OverviewPage):
        overview_page.BUTTON_CHOOSE_CAMPAIGNS.open_view()
        overview_page.INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS.write(query)

        assert view(overview_page)

    def test_tooltip_max_count_campaigns(self, overview_page: OverviewPage):
        overview_page.BUTTON_CHOOSE_CAMPAIGNS.open_view()

        count_choose_campaigns = overview_page.get_current_count_chosen_campaigns()
        overview_page.activate_amount_campaigns(self.max_count_campaigns - count_choose_campaigns)

        overview_page.CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP.hover()
        assert overview_page.TOOLTIP_MAX_COUNT_CHOSE_CAMPAIGN