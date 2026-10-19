from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
import re


def test_search_hobbit_returns_results(home_page: HomePage,search_results_page: SearchResultsPage):
    home_page.open()
    home_page.search("The Hobbit")

    expect(home_page.page).to_have_url(
        re.compile(r"/search\?q=The(\+|%20)Hobbit")
    )

    expect(search_results_page.book_cards.first).to_be_visible()

    book_count = search_results_page.book_cards.count()

    assert book_count >= 5, (
        f"Expected at least 5 books, but found {book_count}"
    )

    for index in range(5):
        book_card = search_results_page.book_cards.nth(index)

        expect(book_card).to_be_visible()

        title = search_results_page.get_book_title(index)
        assert title.strip(), f"Book at index {index} has an empty title"

        assert "hobbit" in title.lower(), (
            f"Book at index {index} has an unexpected title: {title}"
        )

        author = search_results_page.get_book_author(index)

        if author is not None:
            assert author.strip(), f"Book at index {index} has an empty author"