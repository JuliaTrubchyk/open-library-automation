# Verify that Open Library returns the expected number of book records when searching with a valid keyword

from playwright.sync_api import APIRequestContext


def test_api_search_books(api_context: APIRequestContext):    # playwright is the fixture provided by pytest-playwright

    response = api_context.get(
        "https://openlibrary.org/search.json",
        params={"q": "The Hobbit", "limit": 5}
    )

    assert response.status == 200

    data = response.json()

    assert len(data["docs"]) == 5


