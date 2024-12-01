from base import BaseCase
from ui.pages.audience_page import AudiencePage


class TestAudience(BaseCase):
    def test_create_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config['users_list_path']

        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)

        assert users_list_name in audience_page.driver.page_source
        assert users_list_type in audience_page.driver.page_source
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        users_lists = audience_page.get_users_lists()
        assert len(users_lists) == 1
        assert users_list_name in users_lists
