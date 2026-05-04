from shooters_qa_test.pages.main_page import MainPage

#Task2 Max Adults Selection
def test_adult(browser_page):
    adult = MainPage(browser_page)
    adult.login()
    adult.max_adult()

    counter = browser_page.locator("[data-wwt-id='number-counter__input--input']").first
    plus = browser_page.locator(adult.adult_plus).first

    assert int(counter.input_value()) == 10

    assert plus.is_disabled()


