from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.book_cards = page.locator(                  # we're storing a locator as an instance attribute
            "ul.list-books > li.searchResultItem"
        )

    def get_book_title(self, index: int) -> str:
        book_card = self.book_cards.nth(index)
        title = book_card.locator("h3.booktitle")
        return title.inner_text()

    def get_book_author(self, index: int) -> str | None:
        book_card = self.book_cards.nth(index)
        author = book_card.locator('[itemprop="author"]')

        if author.count() == 0:
            return None

        return author.first.inner_text()