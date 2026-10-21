# Verify that Open Library returns the correct work details for a valid work ID.

from api.open_library_client import OpenLibraryClient


def test_api_get_book_details(api_client: OpenLibraryClient):
    work_id = "OL27482W"

    response = api_client.get_work(work_id)

    assert response.status == 200

    data = response.json()

    assert data["title"] == "The Hobbit"
    assert data["key"] == f"/works/{work_id}"    # key is the identifier path for the returned record


 