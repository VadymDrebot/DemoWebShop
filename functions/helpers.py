import random
import re
import string

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from constants.global_constants import PATH_TO_CHROME_WEBDRIVER, PATH_TO_FIREFOX_WEBDRIVER

CHROME = "chrome"
FIREFOX = "firefox"


def random_word(count=5):
    # generate random word up to 'count' symbols
    random_word = ''
    for elem in range(count):
        random_word = random_word + random.choice(string.ascii_letters)
    return random_word


def random_valid_email():
    # create email in format:  ***@***.***
    return str(random_word(3) + "@" + random_word(3) + "." + random_word(3)).lower()


def verify_email(email):
    if re.match("\\w+[@]\\w+[.]\\w+", email):
        return True
    return False


def create_driver(browser_name):
    """ Create browser"""
    if browser_name == CHROME:
        options = webdriver.ChromeOptions()
        # options.headless = True
        return webdriver.Chrome(options=options, executable_path=PATH_TO_CHROME_WEBDRIVER)
    elif browser_name == FIREFOX:
        options = Options()
        # options.headless = True
        return webdriver.Firefox(options=options, executable_path=PATH_TO_FIREFOX_WEBDRIVER)
    else:
        raise ValueError
