# Verify that Open Library returns the expected number of book records when searching with a valid keyword

from api.open_library_client import OpenLibraryClient


def test_api_search_books(api_client: OpenLibraryClient):    # playwright is the fixture provided by pytest-playwright

    response = api_client.search_book("The Hobbit", 5)

    assert response.status == 200

    data = response.json()

    assert len(data["docs"]) == 5


