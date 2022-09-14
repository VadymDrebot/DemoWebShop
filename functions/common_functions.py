import logging
import random
import time

import selenium.webdriver.support.expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from functions.waitings import Waitings, wait_5_sec


class CommonFunctions(Waitings):
    """common/universal functions  for all/any points of the project or even other projects"""

    logger = logging.getLogger()

    def clear_input_field(self, locator, locator_type=By.XPATH):
        input_field = self.driver.find_element(by=locator_type, value=locator)
        input_field.clear()

    def press_keyboard_button(self, button):
        actions = ActionChains(self.driver)
        actions.send_keys(button)
        actions.perform()

    def wait_send_keys_and_click_button(self, locator, data, button):
        self.wait_send_keys(locator=locator, data=data)
        self.press_keyboard_button(button=button)

    @wait_5_sec
    def click_button_and_verify_new_url(self, button, url):
        """ Click button(by locator) and check new URL(expected)"""
        self.wait_click_ability_and_click(locator=button)
        # An expectation for checking the current url.
        self.logger.info(f" Actual  url: -{self.driver.current_url}-")
        self.logger.info(f"Expected url: -{url}-")
        WebDriverWait(self.driver, timeout=5).until(EC.url_to_be(url))
        assert self.driver.current_url == url

    def get_list_of_drop_list_web_elements(self, locator):
        """ return list of WEB_ELEMENTS """
        select = Select(self.driver.find_element(*locator))
        return select.options

    def get_list_of_drop_down_values(self, locator):
        """ return list of VALUES from drop down menu"""
        web_elements_list = self.get_list_of_drop_list_web_elements(locator)
        return [element.text for element in web_elements_list]

    def click_random_from_drop_list(self, locator) -> str:
        """ from 'drop list' choose random element, click on it and return the value(text) of the clicked element"""
        web_elements = self.get_list_of_drop_list_web_elements(locator)
        web_element = web_elements[random.randint(1, len(web_elements) - 1)]
        clicked_name_from_dropdown_menu = web_element.text
        web_element.click()
        time.sleep(1)
        return clicked_name_from_dropdown_menu

    def click_concrete_value_from_drop_down_list(self, value: str, locator):
        """ from 'drop list' choose CONCRETE element by given name(value) and click on it """
        web_elements = self.get_list_of_drop_list_web_elements(locator)
        for web_element in web_elements:
            if web_element.text == value:
                web_element.click()
                time.sleep(1)
                return
        else:
            raise ValueError("Wrong input 'value'")

    def check_presence_of_element(self, locator) -> bool:
        """ check the presence of the element by its locator
        return:
            True -- element is present at DOM
            False -- element is absent at DOM   """
        try:
            # decrease comment up to 1 sec for 'find_element_by_xpath'. By default, it will take 10 sec
            self.driver.implicitly_wait(1)
            self.driver.find_element(*locator)
            # self.logger.info(f" Element exists: -{self.driver.find_element(*locator).text}-")
        except NoSuchElementException:
            return False
        return True

    def verify_checkbox_selected(self, locator):
        # self.logger.info(f"checkbox: {product_page_constants.py.driver.find_element_by_xpath(locator).is_selected()}")
        return self.driver.find_element(*locator).is_selected()

    def verify_message(self, locator, expected_text, comments=""):
        """ verify that expected_text==actual text in 'locator'   """
        actual_text = self.get_text_from_locator(locator)
        # self.logger.info(f"  actual  message {comments}: --{actual_text}--")
        # self.logger.info(f"expected  message {comments}: --{expected_text}--")
        assert actual_text == expected_text, f"{actual_text=} , {expected_text=}"

    def verify_text_partly_present_in_locator(self, message_locator, expected_text):
        """verify that 'expected_text' PARTLY IN the  message(with 'message_locator')"""
        message = self.get_text_from_locator(message_locator)

        # self.logger.info(f"expected part of text: --{expected_text}--")
        # self.logger.info(f"    actual whole text: --{message}--")
        assert expected_text in message

    def get_value_from_input_field(self, locator) -> str:
        """ returns as string"""
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute('value')

    def take_attribute(self, locator, attribute) -> str:
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))
        # self.logger.info(f"value of the attribute: '{product_page_constants.py.driver.find_element(by=locator_type, value=locator).get_attribute(attribute)}-")
        return self.driver.find_element(*locator).get_attribute(attribute)

    def formated_locator(self, locator, index) -> tuple:
        """
        uses for locators witch have '.format'  function
        unpack tuple, (like: (By.XPATH,"xpath")) , modify with '.format' and pack/return new tuple  """
        _, xpath = locator
        new_xpath = xpath.format(index=index)
        return _, new_xpath

    def get_text_from_locator(self, locator):
        return self.driver.find_element(*locator).text if self.check_presence_of_element(locator=locator) else None

    def get_list_of_texts(self, list_locator) -> list:
        list_of_elements = self.wait_find_elements(list_locator=list_locator)
        return [element.text.strip() for element in list_of_elements]

    @wait_5_sec
    def scroll_to_element(self, locator):
        self.driver.execute_script(f"window.scrollTo(0, 1500)")

    def move_mouse_to_locator(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)))
        actions.perform()

    def move_mouse_through_list_of_locators(self, locator_list):
        actions = ActionChains(self.driver)
        for locator in locator_list:
            actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)))
            actions.perform()

    def move_mouse_to_locator_and_click(self, locator):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        actions.move_to_element(element)
        actions.perform()
        actions.click(element)

    def move_mouse_through_list_of_locators_and_click_last(self, mouse_movement_locators_list):
        """elements of the 'list_locator' -- queue(line) for mouse movement
        the last element of the queue will be clicked
        return: the name(text) of the last(clicked) element"""
        actions = ActionChains(self.driver)
        element = ''
        for locator in mouse_movement_locators_list:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            actions.move_to_element(element)
            actions.perform()
        actions.click(element)
        actions.perform()
