from shooters_qa_test.pages.main_page import MainPage


def test_all_pet_weight_combinations(browser_page):
    main_page = MainPage(browser_page)

    main_page.login()
    main_page.open_guests_menu()

    main_page.add_new_pet_row()

    expected_weights = ["<1 kg", "1-5 kg", "5-10 kg", "10-15 kg", "15-20 kg", ">20 kg"]

    pet_weights = browser_page.locator(
        "[data-wwt-id='guests-select__pet-weight--select']"
    )

    for i in range(6):
        actual = pet_weights.nth(i).inner_text().strip()
        assert actual == expected_weights[i], f"Mismatch at pet {i}: {actual}"


def test_all_other_weight_combinations(browser_page):
    main_page = MainPage(browser_page)

    main_page.login()
    main_page.open_guests_menu()

    main_page.add_new_other_row()

    expected_weights = ["<1 kg", "1-5 kg", "5-10 kg", "10-15 kg", "15-20 kg", ">20 kg"]

    pet_weights = browser_page.locator(
        "[data-wwt-id='guests-select__pet-weight--select']"
    )

    for i in range(6):
        actual = pet_weights.nth(i).inner_text().strip()
        assert actual == expected_weights[i], f"Mismatch at pet {i}: {actual}"

