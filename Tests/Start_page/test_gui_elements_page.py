import logging

from Pages.Start_Page import product_page_constants as prod_const


class TestGuiElements:
    """
    test1 : testing 'Sort by' element
    test2 : testing 'Display per page' element
    test3 : testing 'View as' element
    test4 : testing 'Filter by price' element
    """
    logger = logging.getLogger()
    def test1_sort_by_element(self, product_page_elements):
        """
        Summary: verify functionality of the 'Sort by' dropdown box on category page
        1. open random category page
        2. verify existence of 'Sort by' element
        3. choose each value of the 'Sort by' dropdown box
        4. verify all products are sorted by the value chosen from the dropdown box
        """
        product_page_elements.open_random_product_category_page()
        assert product_page_elements.check_presence_of_element(prod_const.DROP_DOWN_SORT_BY_LIST_xpath)
        product_page_elements.verify_elements_to_be_sorted_from_whole_dropdown_menu(locator=prod_const.DROP_DOWN_SORT_BY_SELECT_BLOCK_xpath)

    def test2_display_per_page_element(self, product_page_elements):
        """
        Summary: verify functionality of the 'Display per page' dropdown box on category page
        1. open random category page
        2. verify existence of 'Display per page' element
        3. choose each value of the 'Display per page' dropdown box
        4. verify that the number of products matches to the chosen value from the dropdown menu
        """
        product_page_elements.open_random_product_category_page()
        assert product_page_elements.check_presence_of_element(prod_const.DROP_DOWN_DISPLAY_PER_PAGE_BLOCK_xpath)
        product_page_elements.verify_number_of_products_on_page(locator=prod_const.DROP_DOWN_DISPLAY_PER_PAGE_SELECT_BLOCK_xpath)

    def test3_view_as_element(self, product_page_elements):
        """
        Summary: verify functionality of the 'Display per page' dropdown box on category page
        1. open random category page
        2. verify existence of 'View as' element
        3. choose each value of the 'View as' dropdown box
        4. verify that the output of products matches to the chosen value from the dropdown menu
        """
        product_page_elements.open_random_product_category_page()
        assert product_page_elements.check_presence_of_element(prod_const.DROP_DOWN_VIEW_AS_BLOCK_xpath)
        product_page_elements.verify_products_type_view_on_page(prod_const.DROP_DOWN_VIEW_AS_SELECT_BLOCK_xpath)

    def test4_filter_by_price(self, product_page_elements):
        flag = True
        while flag:
            product_page_elements.open_random_product_category_page()
            if product_page_elements.check_presence_of_element(prod_const.FILTER_BY_PRICE_BLOCK_xpath):
                product_page_elements.verify_filter_by_price_functionality(prod_const.FILTER_BY_PRICE_LIST_OF_VALUES_xpath)
                flag = False
