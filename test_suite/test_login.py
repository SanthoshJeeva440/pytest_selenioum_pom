from pages.base_page import Base_Page
from pages.login_page import LoginPage
import pytest
import conftest
import os


@pytest.mark.usefixtures(os.getenv("browser_mode"))
class Tests:
    data = conftest.read_data()

    @pytest.mark.usefixtures()
    def test_1(self):
        Base_Page().set_url()
        LoginPage().enter_username_and_password('', '')
        LoginPage().click_login_button()
