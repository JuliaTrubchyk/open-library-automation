# Open Library Test Automation Framework

An automated testing framework for [Open Library](https://openlibrary.org), built using **Python, pytest, and Playwright**.

The project demonstrates UI and API test automation, reusable test components, Page Object Model (POM), pytest fixtures, and continuous integration with GitHub Actions.

## Tech Stack

- **Python** — Programming language
- **pytest** — Test framework and assertions
- **Playwright** — Browser automation and API testing
- **GitHub Actions** — Continuous integration (CI)

## Project Structure

```text
open_library_automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── api/
│   ├── __init__.py
│   └── open_library_client.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── book_details_page.py
├── tests/
│   ├── api/
│   │   ├── conftest.py
│   │   ├── test_api_search.py
│   │   ├── test_api_book_details.py
│   │   ├── test_api_edition_details.py
│   │   └── test_api_invalid_work.py
│   └── ui/
│       ├── test_home.py
│       ├── test_ui_search.py
│       └── test_book_details.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Coverage

### UI Testing

- Verify that the Open Library homepage loads successfully.
- Search for books and validate search results.
- Navigate to book details and verify book information.

UI tests follow the **Page Object Model (POM)** design pattern, separating page locators and interactions from test assertions.

### API Testing

- **TC01 — Search Books:** Verify that searching with a valid keyword returns the expected number of records.
- **TC02 — Get Work Details:** Verify work details for a valid work ID.
- **TC03 — Get Edition Details:** Verify edition details for a valid edition ID.
- **TC04 — Invalid Work ID:** Verify that requesting a nonexistent work returns HTTP 404.

API tests use a reusable `OpenLibraryClient` class with methods such as `search_books()`, `get_work()`, and `get_edition()`.

Pytest fixtures manage API request context setup and cleanup.

## Installation

Clone the repository:

```bash
git clone https://github.com/JuliaTrubchyk/open-library-automation.git
cd open-library-automation
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the Chromium browser for Playwright:

```bash
python -m playwright install chromium
```

## Running Tests

Run all API tests:

```bash
pytest tests/api/ -v
```

Run UI tests, excluding the known blocked test:

```bash
pytest tests/ui/ -v -m "not blocked"
```

Run all tests except blocked tests:

```bash
pytest -v -m "not blocked"
```

## Continuous Integration

GitHub Actions automatically runs tests when changes are pushed to the repository.

The workflow contains two independent jobs:

- **API Tests:** Installs Python dependencies and executes API tests.
- **UI Tests:** Installs Python dependencies and Chromium, then executes UI tests excluding blocked tests.

When UI tests fail, the workflow attempts to upload Playwright test artifacts for debugging.

## Known Limitations

One UI test involving navigation to book details is marked with `@pytest.mark.blocked` because Open Library's human-verification challenge can interrupt automated browser navigation.

This test is excluded from regular CI execution using `-m "not blocked"`.

## Key Framework Features

- Page Object Model for reusable UI interactions
- Reusable API client for HTTP requests
- Pytest fixtures for setup and teardown
- Positive and negative API testing
- Separate UI and API test suites
- Automated execution through GitHub Actions
- Playwright screenshots and traces for debugging UI failures
