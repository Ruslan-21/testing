from shooters_qa_test.pages.home_page import HomePage
from shooters_qa_test.pages.login_page import LoginPage
from shooters_qa_test.pages.builder_page import BuilderPage

def test_signup_and_builder(driver):

    driver.get("https://events.shooters.global/")


    home_page = HomePage(driver)
    home_page.go_to_build()

    email = "e6086862@gmail.com"
    password = "0VH72H64oQ"


    login_page = LoginPage(driver)
    login_page.login(email, password)

    builder_page = BuilderPage(driver)
    builder_page.wait_for_canvas(timeout=30)


    login_page.logout()
