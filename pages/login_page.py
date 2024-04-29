from pages.base_page import Base_Page
from locators import po_login


class LoginPage(Base_Page):
    def __init__(self):
        super().__init__()
        self.locator = po_login

    def enter_username_and_password(self, ENTER_USERNAME, ENTER_PASSWORD):
        self.clear_element(self.locator.INPUT_USERNAME)
        self.clear_element(self.locator.INPUT_PASSWORD)
        if ENTER_USERNAME is None or ENTER_USERNAME == '':
            self.input_text(self.locator.INPUT_USERNAME, self.ENV_CONFIG.username)
            self.input_text(self.locator.INPUT_PASSWORD, self.ENV_CONFIG.password)
        else:
            self.input_text(self.locator.INPUT_USERNAME, ENTER_USERNAME)
            self.input_text(self.locator.INPUT_PASSWORD, ENTER_PASSWORD)
        self.set_time(2)

    def click_login_button(self):
        self.click_element(self.locator.BUTTON_SIGNIN)
        self.set_time(3)
