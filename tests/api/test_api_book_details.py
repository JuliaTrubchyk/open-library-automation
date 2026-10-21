# Verify that Open Library returns the correct work details for a valid work ID.

from playwright.sync_api import APIRequestContext


def test_api_get_book_details(api_context: APIRequestContext):

    work_id = "OL27482W"

    response = api_context.get(
        f"https://openlibrary.org/works/{work_id}.json"
    )

    assert response.status == 200

    data = response.json()

    assert data["title"] == "The Hobbit"
    assert data["key"] == f"/works/{work_id}"    # key is the identifier path for the returned record
    assert data["type"]["key"] == "/type/work"
