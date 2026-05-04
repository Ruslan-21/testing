from shooters_qa_test.pages.header_page import HeaderPage

#З'являється модальне вікно для реєстрації
def test_register(browser_page):
    logo = HeaderPage(browser_page)
    logo.check_register()

    assert browser_page.locator("[data-wwt-id='auth__email--input']").is_visible()
    text = browser_page.get_by_text("Let's discover this world together").inner_text()
    assert "Let's discover this world together" == text