import json
import random
import re
import string

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from Pages.Base_Page.global_constants import PATH_TO_CHROME_WEBDRIVER, PATH_TO_FIREFOX_WEBDRIVER, PATH_TO_USERS_JSON, CHROME, FIREFOX


def email_iterator():
    with open(PATH_TO_USERS_JSON) as file:
        return iter([key["login"] for key in json.load(file).values()])


def random_word(count=5):
    # generate random word up to 'count' symbols
    random_w = ''
    for _ in range(count):
        random_w = random_w + random.choice(string.ascii_letters)
    return random_w


def random_valid_email():
    # create email in format:  ***@***.***
    return str(random_word(3) + "@" + random_word(3) + "." + random_word(3)).lower()


def random_invalid_email():
    return str(random_word(random.randint(1, 6)))


def random_valid_password():
    return str(random_word(random.randint(6, 10)))


def random_invalid_password():
    return str(random_word(random.randint(1, 5)))


def verify_email(email):
    return True if re.match("\\w+[@]\\w+[.]\\w+", email) else False


def verify_password(password):
    return False if 0 < len(password) < 6 else True


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
