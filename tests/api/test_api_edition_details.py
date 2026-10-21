# Verify that Open Library returns the correct edition details for a valid edition ID

from api.open_library_client import OpenLibraryClient


def test_api_get_edition_details(api_client: OpenLibraryClient):
    edition_id = "OL51709286M"

    response = api_client.get_edition(edition_id)

    assert response.status == 200

    data = response.json()

    assert data["title"] == "The Hobbit"
    assert data["key"] == f"/books/{edition_id}"
