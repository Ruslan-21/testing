from .base_page import BasePage
from tests_task.locators.cart_locators import CartLocators
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    def remove_carrot(self):
        cart_items = self.find_all(CartLocators.CART_ITEMS)
        for item in cart_items:
            product_name = item.find_element(*CartLocators.PRODUCT_NAME).text
            if "Carrot" in product_name:
                remove_btn = item.find_element(*CartLocators.REMOVE_BUTTON)
                remove_btn.click()
                self.wait.until(EC.staleness_of(item))
                break

    def get_cart_items(self):
        items = self.find_all(CartLocators.CART_ITEMS)
        return [item.find_element(*CartLocators.PRODUCT_NAME).text for item in items]
