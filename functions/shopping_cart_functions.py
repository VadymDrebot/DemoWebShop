import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import start_page_const

from functions.common_functions import CommonFunctions


class ShoppingCartFunctions(CommonFunctions):
    logger = logging.getLogger(__name__)

    def choose_product_from_header_and_click(self, product):
        self.mouse_click_to_locator(
            list_locator=[product.chosen_category_button_xpath, product.chosen_subcategory_button_xpath])

    def verify_correct_transition_to_page(self, product):
        # verify URL
        self.logger.info(f"actual   url: -{self.driver.current_url}-")
        self.logger.info(f"expected url: -{start_page_const.PRODUCT_SUBCATEGORY_PAGE_url.format(subcategory=product.product_subcategory.lower())}-")
        assert self.driver.current_url == start_page_const.PRODUCT_SUBCATEGORY_PAGE_url.format(subcategory=product.product_subcategory.lower())

        # verify page name
        self.logger.info(f"actual   name of the page: -{self.get_text_from_locator(locator=start_page_const.PAGE_TITLE_class, locator_type=By.CLASS_NAME)}-")
        self.logger.info(f"expected name of the page: -{product.product_subcategory}-")
        assert self.get_text_from_locator(locator=start_page_const.PAGE_TITLE_class, locator_type=By.CLASS_NAME) == product.product_subcategory


        # verify breadcrumb
        list = self.get_list_of_texts(list_locator=start_page_const.LIST_OF_PRODUCT_BREADCRUMB_xpath)
        breadcrumb = "/".join(list)
        object_string = f"HOME/{product.chosen_product_category.upper()}/{product.product_subcategory.upper()}"
        assert breadcrumb == object_string, f"breadcrumb:{breadcrumb}, object_string: {object_string}"
