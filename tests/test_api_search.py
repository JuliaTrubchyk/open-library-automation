
from playwright.sync_api import Playwright


def test_api_search_books(playwright: Playwright):
    api_context = playwright.request.new_context()

    try:
        response = api_context.get(
            "https://openlibrary.org/search.json",
            params={"q": "The Hobbit", "limit": 5}
        )

        assert response.status == 200

        data = response.json()

        assert len(data["docs"]) == 5
    finally:
        api_context.dispose()


