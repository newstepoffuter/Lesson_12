import pytest
import os
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "126.0"


def pytest_addoption(parser):
    parser.addoption("--browser_name")
    parser.addoption("--browser_version")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def browser_settings(request):
    browser_name = request.config.getoption('browser_name') or DEFAULT_BROWSER_NAME
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    selenoid_host = os.getenv("SELENOID_HOST")
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{selenoid_host}/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver.maximize_window()

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()

# @pytest.fixture(scope='session', autouse=True)
# def browser_settings():
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = 'eager'
#     browser.config.driver.maximize_window()
#     browser.config.driver_options = driver_options
#     browser.config.base_url = 'https://demoqa.com'
#
#     yield
#     browser.quit()
