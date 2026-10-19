from playwright.sync_api import Page
# A Page is a Playwright object representing a browser tab. It provides methods such as goto(), locator(), and get_by_role()
import re

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_button = page.get_by_role("button", name="Search", exact=True)
        self.search_input = page.locator("ol-search-modal input.search-input") # from modal window

    def get_url(self) -> str:
        return self.page.url

    def search(self, title: str):
        self.search_button.click()
        self.search_input.fill(title)
        self.page.get_by_text(
            re.compile(r"See all \d+ books")
        ).click()