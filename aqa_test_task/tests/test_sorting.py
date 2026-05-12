from aqa_test_task.pages.inventory_page import InventoryPage


def test_sorting(login):

    inventory = InventoryPage(login)

    sorting_options = {
        "az": "Name (A to Z)",
        "za": "Name (Z to A)",
        "lohi": "Price (low to high)",
        "hilo": "Price (high to low)"
    }

    for value, sorting_name in sorting_options.items():

        inventory.choose_sorting(value)


        if value in ["az", "za"]:

            actual_names = inventory.get_product_names()

            expected_names = sorted(actual_names)

            if value == "za":
                expected_names.reverse()

            assert actual_names == expected_names, (
                f"{sorting_name} sorting failed"
            )

        else:

            actual_prices = inventory.get_product_prices()

            expected_prices = sorted(actual_prices)

            if value == "hilo":
                expected_prices.reverse()

            assert actual_prices == expected_prices, (
                f"{sorting_name} sorting failed"
            )