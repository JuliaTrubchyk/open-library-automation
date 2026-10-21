# Verify that Open Library returns HTTP 404 when requesting a work with a nonexistent ID


from playwright.sync_api import APIRequestContext


def test_api_get_invalid_work(api_context: APIRequestContext):
    work_id = "OL999999999999W"

    response = api_context.get(
        f"https://openlibrary.org/works/{work_id}.json"
    )

    assert response.status == 404
