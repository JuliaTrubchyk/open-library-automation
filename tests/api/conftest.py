
import pytest
from playwright.sync_api import Playwright, APIRequestContext
from api.open_library_client import OpenLibraryClient


@pytest.fixture
def api_context(playwright: Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


@pytest.fixture
def api_client(api_context: APIRequestContext):
    return OpenLibraryClient(api_context)
