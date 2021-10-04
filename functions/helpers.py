import logging, random, string

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

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
    email = str(random_word(3) + "@" + random_word(3) + "." + random_word(3))
    return email


def log(target_func):
    logger = logging.getLogger(target_func.__name__)

    def wrapper(*args, **kwargs):
        logger.info(f"{target_func.__doc__} --- {kwargs}")
        return target_func(*args, **kwargs)

    return wrapper


def create_driver(browser_name):
    """ Create browser"""
    if browser_name == CHROME:
        options = webdriver.ChromeOptions()
        options.headless = True
        return webdriver.Chrome(options=options, executable_path=self.PATH_TO_CHROME_WEBDRIVER)
    elif browser_name == FIREFOX:
        options = Options()
        options.headless = True
        return webdriver.Firefox(options=options, executable_path=self.PATH_TO_FIREFOX__WEBDRIVER)
    else:

        raise ValueError
