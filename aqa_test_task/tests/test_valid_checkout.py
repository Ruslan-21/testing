from aqa_test_task.pages.inventory_page import InventoryPage
from aqa_test_task.pages.cart_page import CartPage
from aqa_test_task.pages.checkout_page import CheckoutPage


def test_valid_checkout(login):

    inventory = InventoryPage(login)
    cart = CartPage(login)
    checkout = CheckoutPage(login)

    inventory.add_product_to_cart()

    assert inventory.cart_counter() == "1"

    inventory.open_cart()

    assert cart.product_name() == "Sauce Labs Backpack"
    cart.click_checkout()
    checkout.enter_first_name("Alex")
    checkout.enter_last_name("Test")
    checkout.enter_postal_code("49000")
    checkout.click_continue()

    assert checkout.overview_product_name() == "Sauce Labs Backpack"
    assert checkout.total_price_visible()

    checkout.click_finish()

    assert (
        checkout.success_message()
        == "Thank you for your order!"
    )

    checkout.click_back_home()

    assert "inventory" in login.url
    assert checkout.cart_is_empty()