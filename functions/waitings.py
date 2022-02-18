from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


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


class Waitings:
    logger = logging.getLogger()

    def __init__(self, driver):
        self.driver = driver
        # product_page_constants.py.logger = logging.getLogger(__name__)

    def wait_and_get_element_after_visibility(self, locator, locator_type=By.XPATH, period=5):
        # wait until element became visible and return it
        WebDriverWait(self.driver, timeout=period).until(EC.visibility_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    # def wait_and_get_text_from_element(self, locator, expected_text, locator_type=By.XPATH):
    # product_page_constants.py.logger.warning(f"locator before:{locator} , text before:{text}")

    # WebDriverWait(self.driver, timeout=5).until(EC.text_to_be_present_in_element((locator_type, locator), expected_text))

    @wait_5_sec
    def wait_find_element(self, locator, locator_type=By.XPATH, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))
        # product_page_constants.py.logger.info(product_page_constants.py.driver.find_element_by_xpath(locator))
        # return self.driver.find_element(by=locator_type, value=locator)
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))

    # @wait_5_sec
    # disable @wait5sec as it somehow nullify 'return' result(list of elements) of the function
    def wait_find_elements(self, list_locator):
        WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located( list_locator))
        # product_page_constants.py.logger.info(f"list in waitings:{list_wait}")
        return self.driver.find_elements(*list_locator)

    # ok
    @wait_5_sec
    def wait_click_ability_and_click(self, button):
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(button))
        self.driver.find_element(*button).click()

    # ok
    def wait_send_keys(self, locator, data):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(data)
        if data != "":
            WebDriverWait(self.driver, timeout=5).until(
                EC.text_to_be_present_in_element_value(locator=locator, text_=data))
        # input_field.click()

    def wait_send_keys_without_clear(self, locator, data, locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        input_field = self.driver.find_element(by=locator_type, value=locator)
        input_field.send_keys(data)
        WebDriverWait(self.driver, timeout=5).until(
            EC.text_to_be_present_in_element_value(locator=(locator_type, locator), text_=data))

    def wait_send_keys_empty_value(self, locator, data='', locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        input_field = self.driver.find_element(by=locator_type, value=locator)
        input_field.clear()
        input_field.send_keys(data)

    def wait_slow_send_keys(self, locator, data, locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        input_field = self.driver.find_element(by=locator_type, value=locator)
        for i in range(len(data)):
            input_field.send_keys(data[i])
