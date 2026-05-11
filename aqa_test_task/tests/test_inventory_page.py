from aqa_test_task.pages.inventory_page import InventoryPage

def test_logout(page):
    inventory = InventoryPage(page)


    inventory.open_burger_menu()

    # Step 2: click logout
    inventory.click_logout()

    # Expected result
    assert inventory.is_login_page_opened()

    # fields are empty
    assert inventory.username_field_empty()
    assert inventory.password_field_empty()