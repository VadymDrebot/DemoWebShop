import logging
import random, time
import string
from selenium.common.exceptions import NoSuchElementException

from constants.start_page_const import product_dict, GlobalConstants
from functions.waitings import Waitings, wait_5_sec
from functions.common_function import CommonFunction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class NeutralFunctions(Waitings, GlobalConstants):
    """common functions  for all/any points of the project or even other projects"""

    logger = logging.getLogger(__name__)

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
        # start_page_const.py.logger.info(f"expected message: {expected_message} , actual message: {actual_message}")
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
        # start_page_const.py.logger.info(f" Actual  url: -{start_page_const.py.driver.current_url}-")
        # start_page_const.py.logger.info(f"Expected url: -{url}-")
        assert self.driver.current_url == url

    def choose_random_from_drop_list(self, locator, locator_type=By.XPATH):
        select = Select(self.driver.driver.find_element(by=locator_type, value=locator))
        lst = select.options
        elem = lst[random.randint(1, len(lst) - 1)]
        elem.click()
        time.sleep(1)
        # start_page_const.py.logger.info(elem.text)
        return elem.text

    def verify_presence_of_element(self, locator, locator_type=By.XPATH):
        """ check the presence of the element by its xpath
        True -- element is present at DOM
        False -- element is absent at DOM   """
        try:
            # decrease time up to 1 sec for 'find_element_by_xpath'. By default, it will take 10 sec
            self.driver.implicitly_wait(1)
            self.driver.find_element(by=locator_type, value=locator)
            # start_page_const.py.logger.info(f" Element exists: -{start_page_const.py.driver.find_element(by=locator_type, value=locator+).text}-")
        except NoSuchElementException:
            return False
        return True

    def verify_checkbox_selected(self, locator, locator_type=By.XPATH):
        # start_page_const.py.logger.info(f"checkbox: {start_page_const.py.driver.find_element_by_xpath(locator).is_selected()}")
        return self.driver.find_element(by=locator_type, value=locator).is_selected()

    def verify_message(self, locator, expected_text, locator_type=By.XPATH):
        """ verify that expected_text==text in 'locator'   """
        self.wait_until_text_in_element(locator=locator, expected_text=expected_text, locator_type=locator_type)
        message = self.driver.find_element(by=locator_type, value=locator).text.strip()
        # self.logger.info(f" Actual  'verify message': -{message}-")
        # self.logger.info(f"Expected 'verify message': -{expected_text}-")
        assert message == expected_text
        return True

    # start_page_const.py.logger.info(f" Expected text: '{expected_text}' == Actual text: '{message}'")

    def verify_text_presence_in_message(self, message_locator, expected_text):
        """verify that 'expected_text' PARTLY IN the  message(with 'message_locator')"""
        message = self.get_text_from_locator(message_locator)
        # start_page_const.py.logger.error(f"expected text: -{expected_text}- presents")
        # start_page_const.py.logger.error(f"      message: -{message}- ")
        assert expected_text in message

    def get_value_from_input_field(self, locator, locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator).get_attribute('value')

    def take_attribute(self, locator, attribute, locator_type=By.XPATH):
        WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator_type, locator)))
        # start_page_const.py.logger.info(f"value of the attribute: '{start_page_const.py.driver.find_element(by=locator_type, value=locator).get_attribute(attribute)}-")
        return self.driver.find_element(by=locator_type, value=locator).get_attribute(attribute)

    def get_text_from_locator(self, locator, locator_type=By.XPATH):
        if self.verify_presence_of_element(locator=locator, locator_type=locator_type):
            # WebDriverWait(start_page_const.py.driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(by=locator_type, value=locator).text
        else:
            return "field is empty"

    def get_list_of_elements(self, list_locator):
        # start_page_const.py.logger.info(f"list in common: {list}")
        return self.wait_find_elements(list_locator=list_locator)

    def get_list_of_texts(self, list_locator):
        list_of_elements = self.get_list_of_elements(list_locator=list_locator)
        list_of_texts = []
        for element in list_of_elements:
            # start_page_const.py.logger.info(f"element: -{element.text.strip()}-")
            list_of_texts.append(element.text.strip())
        return list_of_texts

    def get_list_of_texts_from_several_locators(self, list_of_different_locators):
        list_of_texts = []
        for element in list_of_different_locators:
            # start_page_const.py.logger.info(f"element: -{element.text.strip()}-")

            list_of_texts.append(self.get_text_from_locator(locator=element).strip())
        return list_of_texts

    def move_mouse_to_locator(self, locator, locator_type=By.XPATH):
        actions = ActionChains(self.driver)
        actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator_type, locator))))
        actions.perform()

    def move_mouse_through_list_of_locators(self, locator_list, locator_type=By.XPATH):
        actions = ActionChains(self.driver)
        for locator in locator_list:
            actions.move_to_element(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator_type, locator))))
            actions.perform()

    def move_mouse_to_locator_and_click(self, locator, locator_type=By.XPATH):
        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((locator_type, locator)))
        actions.move_to_element(element)
        actions.perform()
        actions.click(element)

    # def move_mouse_to_locator_and_click(start_page_const.py, locator, locator_type=By.XPATH):
    #     actions = ActionChains(start_page_const.py.driver)
    #     actions.move_to_element(WebDriverWait(start_page_const.py.driver, 5).until(EC.element_to_be_clickable((locator_type, locator))))
    #     actions.perform().click()

    def move_mouse_through_list_of_locators_and_click_last(self, movement_list_locator, locator_type=By.XPATH):
        """elements of the 'list_locator' -- queue(line) for mouse movement
        the last element of the queue will be clicked
        return: the name(text) of the last(clicked) element"""
        actions = ActionChains(self.driver)
        element = ''
        for locator in movement_list_locator:
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((locator_type, locator)))
            actions.move_to_element(element)
            actions.perform()
        actions.click(element)
        actions.perform()
        return self.driver.find_element(by=locator_type, value=movement_list_locator[-1]).text

    def verify_breadcrumb(self, list_locator_of_breadcrumb_elements, list_of_expected_breadcrumb_items):
        """ 'actual_list_of_breadcrumb_elements' concatenation of texts of elements of breadcrumb FROM DOM
        'expected_breadcrumb' is taken from manually given 'names'  """
        actual_list_of_breadcrumb_texts = self.get_list_of_texts(list_locator=list_locator_of_breadcrumb_elements)
        actual_breadcrumb = "".join(actual_list_of_breadcrumb_texts).upper()

        expected_breadcrumb = " /".join(list_of_expected_breadcrumb_items).upper()

        self.logger.info(f"ACTUAL   breadcrumb: -{actual_breadcrumb}-")
        self.logger.info(f"EXPECTED breadcrumb: -{expected_breadcrumb}-")
        assert actual_breadcrumb == expected_breadcrumb

    def open_random_product_category_page(self):
        """ open random END POINT category page (with list of PRODUCTS , not with SUBCATEGORIES) """
        mouse_movement_locators_list = []
        while not mouse_movement_locators_list:
            item = random.choice(list(product_dict.values()))
            if "sub_menu" not in item:
                mouse_movement_names_list = item["mouse_movement"]  # ["Computers", "Desktops"]
                mouse_movement_locators_list = [product_dict[name]["xpath"] for name in mouse_movement_names_list]
        self.move_mouse_through_list_of_locators_and_click_last(movement_list_locator=mouse_movement_locators_list)
