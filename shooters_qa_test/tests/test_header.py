

#Наявність іконок хедера
def test_main(browser_page):


    assert browser_page.locator("[data-wwt-id='promo-button__get-discount--link']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__share--button']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__notifications--button']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__like-link-not-active--unique']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__account--button']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__register--button']").is_visible()
    assert browser_page.locator("[data-wwt-id='header__sign-in--button']").is_visible()


