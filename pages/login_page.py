from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input: Locator = page.locator("#username")
        self.password_input: Locator = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message: Locator = page.locator("#flash")

    def open(self):
        self.go_to(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username) #nie uzywamy juz wait_for_element bo Playwright ma auto-waiting
        self.password_input.fill(password) #nie uzywamy juz wait_for_element bo Playwright ma auto-waiting
        self.login_button.click()          #nie uzywamy juz wait_for_element bo Playwright ma auto-waiting
#kazda z tych operacji (fill, click juz zawiera implicit wait) automatycznie:czeka aż element będzie w DOM, aż będzie widoczny, aż będzie enabled,aż będzie stabilny