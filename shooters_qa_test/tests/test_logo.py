from shooters_qa_test.pages.header_page import HeaderPage

#Повернення на головну сторінку при натисканні на лого
def test_logo(browser_page):
    logo = HeaderPage(browser_page)
    logo.check_logo()

    assert browser_page.locator("[data-wwt-id='promo-button__get-discount--link']").is_visible()