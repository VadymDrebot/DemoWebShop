from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


def log(target_func):
    logger = logging.getLogger(target_func.__name__)

    def wrapper(*args, **kwargs):
        logger.info(f"{target_func.__doc__} --- {kwargs}")
        return target_func(*args, **kwargs)

    return wrapper



def wait_5_sec(target):
    def wrapper(*args, **kwargs):
        limit = 0
        while limit < 5:
            try:
                target(*args, **kwargs)
                limit = 5
            except Exception:
                limit = limit + 0.5

    return wrapper


class Waitings():
    logger = logging.getLogger(__name__)

    def __init__(self, driver):
        self.driver = driver
        # self.logger = logging.getLogger(__name__)

    def wait_until_visibility_of_element(self, locator, period=5):
        # wait until element became visible
        WebDriverWait(self.driver, timeout=period).until(EC.visibility_of_element_located((By.XPATH, locator)))

    # def invisibility_of_element(self,locator):
    # 	return WebDriverWait(self.driver, timeout=1).until(EC.visibility_of_element_located((By.XPATH, locator)))

    @wait_5_sec
    def scroll_to_element(self, locator):
        self.driver.execute_script(f"window.scrollTo(0, 1500)")

    def wait_until_text_in_element(self, locator, text):
        # self.logger.warning(f"locator before:{locator} , textbefore:{text}")
        WebDriverWait(self.driver, timeout=5).until(EC.text_to_be_present_in_element((By.XPATH, locator), text))

    @wait_5_sec
    def wait_click_ability_and_click(self, locator):
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((By.XPATH, locator)))
        self.driver.find_element_by_xpath(locator).click()

    def wait_send_keys(self, locator, data):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        input_field = self.driver.find_element(by=By.XPATH, value=locator)
        input_field.clear()
        input_field.send_keys(data)
        if data != "":
            WebDriverWait(self.driver, timeout=5).until(
                EC.text_to_be_present_in_element_value(locator=(By.XPATH, locator), text_=data))
        # input_field.click()

    def wait_send_keys_without_clear(self, locator, data):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, locator)))
        input_field = self.driver.find_element(by=By.XPATH, value=locator)
        input_field.send_keys(data)
        WebDriverWait(self.driver, timeout=5).until(
            EC.text_to_be_present_in_element_value(locator=(By.XPATH, locator), text_=data))

    def wait_send_keys_empty_value(self, locator, data=''):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, locator)))
        input_field = self.driver.find_element(by=By.XPATH, value=locator)
        input_field.clear()
        input_field.send_keys(data)

    def slow_send_keys(self, locator, data):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, locator)))
        input_field = self.driver.find_element(by=By.XPATH, value=locator)
        for i in range(len(data)):
            input_field.send_keys(data[i])

    @wait_5_sec
    def wait_find_element(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        # self.logger.info(self.driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)

    @wait_5_sec
    def wait_find_elements(self, locator):
        WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        # self.logger.info(self.driver.find_element_by_xpath(locator))
        return self.driver.find_elements_by_xpath(locator)
