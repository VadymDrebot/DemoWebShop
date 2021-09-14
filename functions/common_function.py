from selenium.webdriver.common.by import By

from functions.neutral_functions import NeutralFunctions


class CommonFunction(NeutralFunctions):
    """ functions which used throughout the project (product page , shopping cart, ..."""

    def make_list_of_dom_indexes(self, product, list_locator, locator_type=By.XPATH):
        """ 'list_locator' -- list of items on a page(shopping cart,products page, etc...).
        Return: list of DOM indexes(from 1 to ...) into the 'product' object"""
        product_amount_on_page = len(self.driver.find_elements(by=locator_type, value=list_locator))  # f.e. len=5
        product.list_of_dom_indexes = [index for index in range(1, product_amount_on_page + 1)]  # lst= [1,2,3,4,5]
        return product
