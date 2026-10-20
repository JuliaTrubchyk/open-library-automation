
from playwright.sync_api import Playwright


def test_api_get_book_details(playwright: Playwright):
    api_context = playwright.request.new_context()

    try:
        work_id = "OL27482W"

        response = api_context.get(
            f"https://openlibrary.org/works/{work_id}.json"
        )

        assert response.status == 200

        data = response.json()

        assert data["title"] == "The Hobbit"
        assert data["key"] == f"/works/{work_id}"
        assert data["type"]["key"] == "/type/work"

    finally:
        api_context.dispose()
