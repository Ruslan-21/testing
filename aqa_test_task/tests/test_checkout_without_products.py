from aqa_test_task.pages.inventory_page import InventoryPage
from aqa_test_task.pages.cart_page import CartPage


def test_checkout_without_products(login):

    inventory = InventoryPage(login)
    cart = CartPage(login)

    inventory.open_cart()
    assert cart.cart_is_empty()

    cart.click_checkout()

    assert "Cart is empty" in cart.get_error_message()
    assert "checkout" not in login.url