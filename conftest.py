import os
import pytest
from drivers.browser import Browser_Config
import yaml

driver = None


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption('--browser', action="store", default='chrome', help='')
    parser.addoption('--mode', action="store", default="head")
    parser.addoption('--browser_mode', action="store", default='browser')


def read_data():
    with open("test_data/" + os.getenv("env") + "_test_data.yaml", 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


def pytest_configure(config):
    os.environ['env'] = config.getoption('env')
    os.environ['browser'] = config.getoption('browser')
    os.environ['mode'] = config.getoption('mode')
    os.environ['browser_mode'] = config.getoption('browser_mode')


@pytest.fixture(scope='class')
def browser():
    global driver
    driver = Browser_Config().open_browser(cross=None)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def cross_browser(request):
    global driver
    if request.param == 'chrome':
        driver = Browser_Config().open_browser(cross='chrome')
    elif request.param == 'firefox':
        driver = Browser_Config().open_browser(cross='firefox')
    elif request.param == 'edge':
        driver = Browser_Config().open_browser(cross='edge')
    driver.maximize_window()
    yield driver
    driver.quit()
