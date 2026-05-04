from playwright.sync_api import Page

class MainPage:


    guest_adult = "[data-wwt-id='guests-select__open--button']"
    adult_plus = "[data-wwt-id='number-counter__plus--button']"
    sign_in_btn = "[data-wwt-id='header__sign-in--button']"
    email_sign_in = "[data-wwt-id='auth__email--input']"
    password_sign_in = "[data-wwt-id='auth__password--input']"
    sign_in_button = "[data-wwt-id='auth__sign-in-submit--button']"
    go_to_home_btn = "[data-wwt-id='error-dialog__home--link']"
    card_filter = "[data-wwt-id='main-search__recommended-filter--button']"



    def __init__(self, page: Page):
        self.page = page

    def login (self):
        self.page.locator(self.sign_in_btn).click()
        self.page.locator(self.email_sign_in).fill("o95142662@gmail.com")
        self.page.locator(self.password_sign_in).fill("Qwerty!@123")
        self.page.locator(self.sign_in_button).click()
        self.page.locator(self.go_to_home_btn).click()

    def max_adult(self):
        self.page.wait_for_timeout(3000)

        self.page.locator(self.guest_adult).first.click()
        plus = self.page.locator(self.adult_plus).first
        counter = self.page.locator("[data-wwt-id='number-counter__input--input']").first

        while True:
            value = int(counter.input_value())

            if value >= 10:
                break

            plus.click()

        return int(counter.input_value())


    def open_guests_menu(self):
        self.page.wait_for_timeout(3000)
        self.page.locator(self.guest_adult).first.click()


    def add_new_pet_row(self):

        plus = self.page.locator("[data-wwt-id='number-counter__plus--button']").last

        for _ in range(6):
            plus.wait_for(state="visible")
            plus.click()

        weights = ["<1 kg", "1-5 kg", "5-10 kg", "10-15 kg", "15-20 kg", ">20 kg"]

        for i, weight in enumerate(weights):

            self.page.locator(
                "[data-wwt-id='guests-select__pet-weight--select']"
            ).nth(i).click()


            option = self.page.locator("div[role='option']").filter(has_text=weight)
            option.wait_for(state="visible")
            option.click()

            self.page.mouse.wheel(0, 500)

    def add_new_other_row(self):

        plus = self.page.locator("[data-wwt-id='number-counter__plus--button']").last

        for _ in range(6):
            plus.wait_for(state="visible")
            plus.click()

        weights = ["<1 kg", "1-5 kg", "5-10 kg", "10-15 kg", "15-20 kg", ">20 kg"]

        for i, weight in enumerate(weights):

            self.page.locator(
                "[data-wwt-id='guests-select__pet-weight--select']"
            ).nth(i).click()

            option = self.page.locator("div[role='option']").filter(has_text=weight)
            option.scroll_into_view_if_needed()
            option.click()

            self.page.mouse.wheel(0, 400)

            pet_type = self.page.locator(
                "[data-wwt-id='guests-select__pet-type--select']"
            ).nth(i)

            pet_type.click()

            self.page.locator("div[role='option']").filter(has_text="Other").click()

            self.page.mouse.wheel(0, 400)


    def filter_affect_request(self):

        for i in range(5):
            self.page.locator(self.card_filter).nth(i).click()

        with self.page.expect_response(
                lambda r: "/api/v1/statistics/offers/count" in r.url,
                timeout=60000
        ) as response:
            self.page.locator(
                "[data-wwt-id='main-search__big-filter-open--button']"
            ).last.click()

        return response.value

