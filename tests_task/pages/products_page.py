from .base_page import BasePage
from tests_task.locators.products_locators import ProductsLocators
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):
    URL = "https://rahulshettyacademy.com/seleniumPractise/#/"

    def open(self):
        self.driver.get(self.URL)

    def search_product(self, text):
        self.enter_text(ProductsLocators.SEARCH_INPUT, text)

    def get_product_by_name(self, product_name: str):
        products = self.find_all(ProductsLocators.PRODUCTS)
        for product in products:
            name = product.find_element(*ProductsLocators.PRODUCT_NAME).text
            if product_name in name:
                return product
        return None

    def add_carrot(self, quantity=5):
        carrot = self.get_product_by_name("Carrot")
        if carrot:
            qty_input = carrot.find_element(*ProductsLocators.QUANTITY_INPUT)
            qty_input.clear()
            qty_input.send_keys(str(quantity))
            carrot.find_element(*ProductsLocators.ADD_BUTTON).click()

    def add_mushroom(self, quantity=3):
        mushroom = self.get_product_by_name("Mushroom")
        if mushroom:
            increment_button = mushroom.find_element(*ProductsLocators.INCREMENT_BUTTON)
            for _ in range(quantity - 1):
                increment_button.click()
            mushroom.find_element(*ProductsLocators.ADD_BUTTON).click()

    def open_cart(self):
        self.click(ProductsLocators.CART_ICON)
