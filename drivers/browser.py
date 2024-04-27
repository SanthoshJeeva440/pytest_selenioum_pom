import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService


class Browser_Config:

    def __init__(self):
        self.BROWSER = os.getenv("browser")
        self.HEADLESS = os.getenv("mode")

    def chrome_driver(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--" + self.HEADLESS)
        chrome_option.add_argument("--no-sandbox")
        chrome_option.add_argument("--disable-dev-shm-usage")
        chrome_option.add_argument("--ignore-certificate-errors")
        chrome_option.add_argument("--remote-allow-origins=*")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)

    def edge_driver(self):
        edge_option = webdriver.EdgeOptions()
        edge_option.add_argument("--" + self.HEADLESS)
        edge_option.add_argument("--ignore-certificate-errors")
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_option)

    def firefox_driver(self):
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument("--" + self.HEADLESS)
        firefox_option.add_argument("--ignore-certificate-errors")
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_option)

    def open_browser(self, cross):
        if cross is None:
            browserName = self.BROWSER
        else:
            browserName = cross
        match browserName:
            case "chrome":
                driver = self.chrome_driver()
            case "edge":
                driver = self.edge_driver()
            case "firefox":
                driver = self.firefox_driver()
            case _:
                driver = self.chrome_driver()
        return driver
