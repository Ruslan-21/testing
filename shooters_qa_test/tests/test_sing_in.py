from shooters_qa_test.pages.header_page import HeaderPage

#З'являється модальне вікно для авторизації
def test_sign_in(browser_page):
    logo = HeaderPage(browser_page)
    logo.check_sing_in()

    assert browser_page.locator("[data-wwt-id='auth__email--input']").is_visible()
    text = browser_page.get_by_text("Welcome back!").inner_text()
    assert "Welcome back!" == text