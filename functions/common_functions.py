import random, time
import string
from selenium.common.exceptions import NoSuchElementException
from functions.waitings import Waitings, wait_5_sec

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CommonFunctions(Waitings):
    # common functions  for all/any points of the project

    def clear_input_field(self, locator, locator_type=By.XPATH):
        input_field = self.driver.driver.find_element(by=locator_type, value=locator)
        input_field.clear()

    def press_keyboard_button(self, button):
        actions = ActionChains(self.driver)
        actions.send_keys(button)
        actions.perform()

    @wait_5_sec
    def click_button_and_verify_message_by_message_locator(self, button_locator, message_locator, expected_message, locator_type=By.XPATH):
        """ for verifying appeared text of the message after click the button """
        self.wait_click_ability_and_click(locator=button_locator)
        self.wait_until_visibility_of_element(locator=message_locator, period=2)
        actual_message = self.driver.find_element(by=locator_type, value=message_locator)(message_locator).text
        # self.logger.info(f"expected message: {expected_message} , actual message: {actual_message}")
        assert actual_message == expected_message

    @wait_5_sec
    def click_button_and_verify_appeared_element(self, button_locator, appeared_element_locator, locator_type=By.XPATH):
        # Click  button(by locator) and check XPATH(expecting_locator) for approving existing of the element
        self.wait_click_ability_and_click(locator=button_locator)
        self.wait_until_visibility_of_element(locator=appeared_element_locator, period=2)
        assert self.driver.find_element(by=locator_type, value=appeared_element_locator)

    @wait_5_sec
    def click_button_and_verify_new_url(self, button_locator, button_locator_type, url):
        # Click button(by locator) and check new URL(expected)
        self.wait_click_ability_and_click(locator=button_locator, locator_type=button_locator_type)

        # An expectation for checking the current url.
        WebDriverWait(self.driver, timeout=5).until(EC.url_to_be(url))
        # self.logger.error(f" button for new url:{url} clicked")
        assert self.driver.current_url == url

    def choose_random_from_drop_list(self, locator, locator_type=By.XPATH):
        select = Select(self.driver.driver.find_element(by=locator_type, value=locator))
        lst = select.options
        elem = lst[random.randint(1, len(lst) - 1)]
        elem.click()
        time.sleep(1)
        # self.logger.info(elem.text)
        return elem.text

    def verify_presence_of_element(self, locator, locator_type=By.XPATH):
        """ check the presence of the element by its xpath"""
        # True -- element is present at DOM
        # False -- element is absent at DOM
        try:
            # decrease time up to 0.1 sec for 'find_element_by_xpath'. Else, it will take 10 sec
            self.driver.implicitly_wait(0.1)
            self.driver.find_element(by=locator_type, value=locator)
        except NoSuchElementException:
            return False
        return True

    def verify_checkbox_selected(self, locator, locator_type=By.XPATH):
        # self.logger.info(f"checkbox: {self.driver.find_element_by_xpath(locator).is_selected()}")
        return self.driver.find_element(by=locator_type, value=locator).is_selected()

    def verify_message(self, locator, expected_text, locator_type=By.XPATH):
        """ verify 'expected_text' in 'locator'"""
        # verify that expected_text==text  in locator
        self.wait_until_text_in_element(locator, expected_text)
        # self.logger.error(f"   text: -{expected_text}- presents")
        message = self.driver.find_element(by=locator_type, value=locator).text
        # self.logger.error(f"message: -{message}- was find and get")
        assert message == expected_text

    # self.logger.info(f" Expected text: '{expected_text}' == Actual text: '{message}'")

    def verify_text_presence_in_message(self, message_locator, expected_text):
        # verify that expected_text IN the locator's message
        message = self.get_text_from_locator(message_locator)
        # self.logger.error(f"expected text: -{expected_text}- presents")
        # self.logger.error(f"      message: -{message}- ")
        assert expected_text in message

    def get_value_from_input_field(self, locator, locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator).get_attribute('value')

    def get_text_from_locator(self, locator, locator_type=By.XPATH):
        if self.verify_presence_of_element(locator, locator_type):
            # WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(by=locator_type, value=locator).text
        else:
            return "field is empty"

    def get_list_of_elements(self, list_locator):
        return self.wait_find_elements(list_locator)

    def get_list_of_texts(self, list_locator):
        list_of_elements = self.get_list_of_elements(list_locator)
        list_of_texts = []
        for element in list_of_elements:
            list_of_texts.append(element.text.strip())
        return list_of_texts

    def mouse_move_to_locator(self, locator_list, locator_type=By.XPATH):
        actions = ActionChains(self.driver)
        for locator in locator_list:
            actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))))
            actions.perform()
            time.sleep(1)

    def mouse_click_to_locator(self, list_locator, locator_type=By.XPATH):
        # list_locator --
        actions = ActionChains(self.driver)
        for locator in list_locator:
            actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator))))
            actions.perform()
            time.sleep(1)
        actions.click(self.driver.find_element(by=locator_type, value=list_locator[-1]))
        actions.perform()
        return self.driver.find_element(by=locator_type, value=list_locator[-1]).text
