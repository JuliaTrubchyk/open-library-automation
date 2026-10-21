from playwright.sync_api import APIRequestContext


class OpenLibraryClient:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    def search_book(self, query: str, limit: int):
        return self.api_context.get(
            f"https://openlibrary.org/search.json",
            params={"q": query, "limit": limit}
        )

    def get_work(self, work_id: str):
        return self.api_context.get(
            f"https://openlibrary.org/works/{work_id}.json"
        )

    def get_edition(self, edition_id: str):
        return self.api_context.get(
            f"https://openlibrary.org/books/{edition_id}.json"
        )