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
        Base_Page(conftest.driver).set_url()
        LoginPage(conftest.driver).enter_username_and_password('', '')
        LoginPage(conftest.driver).click_login_button()
