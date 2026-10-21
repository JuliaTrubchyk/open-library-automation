# Verify that Open Library returns the correct edition details for a valid edition ID

from playwright.sync_api import APIRequestContext


def test_api_get_edition_details(api_context: APIRequestContext):
    edition_id = "OL51709286M"

    response = api_context.get(
        f"https://openlibrary.org/books/{edition_id}.json"
    )

    assert response.status == 200

    data = response.json()

    assert data["title"] == "The Hobbit"
    assert data["key"] == f"/books/{edition_id}"
