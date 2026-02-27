from playwright.sync_api import Page
from pages.base_page import BasePage

class ExamplePage(BasePage):
    URL = "https://example.com"

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.heading = page.locator("h1")
        self.main_paragraph = page.locator("p").first
        self.more_info_link = page.get_by_role("link", name="Learn more")

    def open(self):
        self.go_to(self.URL)

    def get_heading_text(self) -> str:
        return self.wait_for_element(self.heading).inner_text()

    def is_main_paragraph_visible(self) -> bool:
        self.wait_for_element(self.main_paragraph)
        return self.main_paragraph.is_visible()

    def click_more_information(self):
        self.wait_for_element(self.more_info_link).click()
