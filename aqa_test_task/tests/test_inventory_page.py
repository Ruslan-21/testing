from aqa_test_task.pages.inventory_page import InventoryPage

def test_logout(login):
    inventory = InventoryPage(login)

    inventory.open_burger_menu()
    inventory.click_logout()

    assert inventory.is_login_page_opened()