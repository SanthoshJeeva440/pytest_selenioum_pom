from config.config_setup import Configuration
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import conftest


class Base_Page:
    ENV_CONFIG = Configuration.get_config()

    def __init__(self):
        self.driver = conftest.driver
        self.wait = WebDriverWait(self.driver, 10)
        self.time = time

    def set_url(self):
        self.driver.get(self.ENV_CONFIG.url)

    def input_text(self, by_locator, text):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def click_element(self, by_locator):
        self.wait.until((EC.presence_of_element_located(by_locator))).click()

    def clear_element(self, by_locator):
        self.wait.until((EC.presence_of_element_located(by_locator))).clear()

    def set_time(self, t=5):
        self.time.sleep(t)
