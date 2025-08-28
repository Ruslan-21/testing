from selenium.webdriver.common.by import By

class CartLocators:
    CART_ITEMS = (By.CSS_SELECTOR, "li.cart-item")
    PRODUCT_NAME = (By.CSS_SELECTOR, "p.product-name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "a.product-remove")
