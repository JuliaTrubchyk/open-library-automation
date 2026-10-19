import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def search_results_page(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)