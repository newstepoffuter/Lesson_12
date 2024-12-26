import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach


# @pytest.fixture(scope="function")
# def browser_settings():
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "126.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options)
#     options.page_load_strategy = 'eager'
#     browser.config.driver = driver
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.driver.maximize_window()
#
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#     browser.quit()



@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver.maximize_window()
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()

