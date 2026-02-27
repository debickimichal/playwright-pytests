from playwright.sync_api import Page
from .base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.signup_button = page.get_by_role("button", name="Sign Up")
        self.error_message = page.locator("#error")

    def signup(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.signup_button.click()
