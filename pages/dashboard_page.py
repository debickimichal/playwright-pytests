from playwright.sync_api import Page
from .base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")

    def logout(self):
        self.logout_button.click()
