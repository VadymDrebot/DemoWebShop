PATH_TO_CHROME_WEBDRIVER = "P:/Pycharm/PycharmProjects/DemoWebShop/drivers/chromedriver.exe"
PATH_TO_FIREFOX__WEBDRIVER = "P:/Pycharm/PycharmProjects/DemoWebShop/drivers/geckodriver.exe"
START_PAGE_url = "http://demowebshop.tricentis.com/"
REGISTER_PAGE_url = f"{START_PAGE_url}register"
PRODUCT_SUBCATEGORY_PAGE_url = "http://demowebshop.tricentis.com/{subcategory}"

LOGIN_BUTTON_IN_HEADER_xpath = "//a[@class='ico-login']"
REGISTER_BUTTON_IN_HEADER_xpath = "//a[@class='ico-register']"
REGISTER_BUTTON_IN_HEADER_class = "ico-register"

# Menu in header
BOOKS_BUTTON_xpath = "//ul[@class='top-menu']//a[@href='/books']"
COMPUTERS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/computers']"
DESKTOPS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/desktops']"
NOTEBOOKS_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/notebooks']"
ACCESSORIES_BUTTON_IN_HEADER_xpath = "//ul[@class='top-menu']//a[@href='/accessories']"

PAGE_TITLE_xpath = "//div[@class='page-title']"
PAGE_TITLE_class = 'page-title'
LIST_OF_PRODUCT_BREADCRUMB_xpath = "//div[@class='breadcrumb']/ul/li"
# PRODUCT_LIST_xpath = "//div[@class='product-grid']"
# PRODUCT_LIST_class = "product-grid"
LIST_OF_PRODUCTS_ON_PAGE_xpath = "//div[@class='item-box']"
LIST_OF_PRODUCTS_ON_PAGE_class = "item-box"


class Product():
    def __init__(self, product_subcategory):
        self.__product_subcategory = ""
        self.product_subcategory = product_subcategory

    @property
    def product_subcategory(self):
        return self.__product_subcategory

    @product_subcategory.setter
    def product_subcategory(self, product_subcategory):
        self.__product_subcategory=product_subcategory
        if product_subcategory == "Desktops":
            self.chosen_category_button_xpath = COMPUTERS_BUTTON_IN_HEADER_xpath
            self.chosen_subcategory_button_xpath = DESKTOPS_BUTTON_IN_HEADER_xpath
            self.chosen_product_category = "computers"
