
import re
import pytest

from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.book_details_page import BookDetailsPage

@pytest.mark.blocked
def test_book_details_match_search_result(
    home_page: HomePage,
    search_results_page: SearchResultsPage,
    book_details_page: BookDetailsPage
):
    # Open homepage and search for a book
    home_page.open()
    home_page.search("The Hobbit")

    # Verify search results URL
    expect(home_page.page).to_have_url(
        re.compile(r"/search\?q=The(\+|%20)Hobbit")
    )

    # Save the first book's title before navigating
    expect(search_results_page.book_cards.first).to_be_visible()
    search_title = search_results_page.get_book_title(0)

    # Open the first book
    search_results_page.open_book(0)

    # Verify the details page is displayed
    try:
        expect(book_details_page.book_title).to_be_visible(timeout=10000)
    except AssertionError:
        verification_heading = book_details_page.page.get_by_role(
            "heading", name="Human Verification"
        )

        if verification_heading.is_visible():
            pytest.fail(
                "Open Library displayed a human verification challenge "
                "instead of the book details page."
            )

        raise

    # Compare the book titles
    details_title = book_details_page.book_title.inner_text()

    assert search_title.strip() == details_title.strip(), (
        f"Search title '{search_title}' doesn't match "
        f"details title '{details_title}'"
    )

    # Navigate back to search results
    book_details_page.page.go_back()

    # Verify the original search URL is restored
    expect(search_results_page.page).to_have_url(
        re.compile(r"/search\?q=The(\+|%20)Hobbit")
    )

    # Verify search results are still displayed
    expect(search_results_page.book_cards.first).to_be_visible()

    # Verify the first book title is preserved
    returned_title = search_results_page.get_book_title(0)

    assert returned_title.strip() == search_title.strip(), (
        f"Expected '{search_title}' after navigating back, "
        f"but found '{returned_title}'"
    )
