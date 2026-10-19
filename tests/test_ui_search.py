from playwright.sync_api import expect
from pages.home_page import HomePage
import re


def test_search_hobbit_returns_results(home_page: HomePage):
    home_page.open()
    home_page.search("The Hobbit")

    expect(home_page.page).to_have_url(
        re.compile(r"/search\?q=The(\+|%20)Hobbit")
    )