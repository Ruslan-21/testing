import pytest
from selenium import webdriver
from tests_task.pages.products_page import ProductsPage
from tests_task.pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_and_remove_products(driver):
    products_page = ProductsPage(driver)
    cart = CartPage(driver)

    products_page.open()
    products_page.search_product("ro")
    products_page.add_carrot(5)
    products_page.add_mushroom(3)
    products_page.open_cart()

    cart.remove_carrot()
    items = cart.get_cart_items()

    assert all("Carrot" not in name for name in items), "Carrot не удалился из корзины"
    assert any("Mushroom" in name for name in items), "Mushroom отсутствует в корзине"
