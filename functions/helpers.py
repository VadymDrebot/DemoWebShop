from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from constants import start_page_const

CHROME = "chrome"
FIREFOX = "firefox"


def create_driver(browser_name):
    """ Create broser"""
    if browser_name == CHROME:
        options = webdriver.ChromeOptions()
        # options.headless=True
        options.add_argument("headless")
        return webdriver.Chrome(options=options, executable_path=start_page_const.PATH_TO_WEBDRIVER)
    elif browser_name == FIREFOX:
        options = Options()
        options.add_argument("--headless")
        return webdriver.Firefox
    else:
        raise ValueError
