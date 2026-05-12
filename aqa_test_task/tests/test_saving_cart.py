from aqa_test_task.pages.inventory_page import InventoryPage
from aqa_test_task.pages.login_page import LoginPage


def test_saving_cart_after_logout(login):

    inventory = InventoryPage(login)
    login_page = LoginPage(login)

    inventory.add_product_to_cart()

    assert inventory.cart_counter() == "1"

    inventory.open_burger_menu()

    inventory.click_logout()

    assert inventory.is_login_page_opened()
    assert inventory.username_field_empty()
    assert inventory.password_field_empty()

    login_page.enter_login("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in login.url

    inventory.open_cart()

    assert inventory.cart_product_name() == "Sauce Labs Backpack"