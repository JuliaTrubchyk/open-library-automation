
import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture
def api_context(playwright: Playwright):
    context = playwright.request.new_context()

    yield context

    context.dispose()
