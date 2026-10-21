# Verify that Open Library returns the correct edition details for a valid edition ID



from playwright.sync_api import Playwright


def test_api_get_edition_details(playwright: Playwright):
    api_context = playwright.request.new_context()

    try:
        edition_id = "OL51709286M"

        response = api_context.get(
            f"https://openlibrary.org/books/{edition_id}.json"
        )

        assert response.status == 200

        data = response.json()

        assert data["title"] == "The Hobbit"
        assert data["key"] == f"/books/{edition_id}"

    finally:
        api_context.dispose()
