from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

import logging

from Helpers.logging_functions import create_logger


def wait_5_sec(target):
    def wrapper(*args, **kwargs):
        limit = 0
        while limit < 5:
            try:
                target(*args, **kwargs)
                limit = 5
            except TimeoutError:
                limit = limit + 0.5

    return wrapper


class Waitings:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def wait_and_get_element_after_visibility(self, locator, period=5):
        # wait until element became visible and return it
        WebDriverWait(self.driver, timeout=period).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # @wait_5_sec
    def wait_find_element(self, locator, timeout=5):
        # b, xpath=locator
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # @wait_5_sec
    # disable @wait5sec as it somehow nullify 'return' result(list of elements) of the function
    def wait_find_elements(self, list_locator):
        WebDriverWait(self.driver, timeout=3).until(EC.presence_of_all_elements_located(list_locator))
        # self.logger.info(f"list in waitings:{list_wait}")
        return self.driver.find_elements(*list_locator)

    @wait_5_sec
    def wait_click_ability_and_click(self, locator):
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_send_keys(self, locator, data):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(data)
        if data != "":
            WebDriverWait(self.driver, timeout=5).until(
                EC.text_to_be_present_in_element_value(locator=locator, text_=data))
        # input_field.click()

    def wait_send_keys_without_clear(self, locator, data):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        input_field = self.driver.find_element(*locator)
        input_field.send_keys(data)
        WebDriverWait(self.driver, timeout=5).until(
            EC.text_to_be_present_in_element_value(locator=locator, text_=data))

    def wait_send_keys_empty_value(self, locator, data=''):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(data)

    def wait_slow_send_keys(self, locator, data):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        input_field = self.driver.find_element(*locator)
        for data_item in data:
            input_field.send_keys(data_item)
