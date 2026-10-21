# Verify that Open Library returns HTTP 404 when requesting a work with a nonexistent ID

from api.open_library_client import OpenLibraryClient


def test_api_get_invalid_work(api_client: OpenLibraryClient):
    work_id = "OL999999999999W"

    response = api_client.get_work(work_id)

    assert response.status == 404
