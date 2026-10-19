# Open Library Test Automation Framework

## Project Overview

This project is a test automation framework for [Open Library](https://openlibrary.org), developed using **Python, Playwright, and pytest**.

The framework covers UI and API testing and follows the **Page Object Model (POM)** design pattern to improve code reusability, readability, and maintainability.

The project is currently under development.

## Tech Stack

- **Python** — Programming language
- **Playwright** — Browser automation and API testing
- **pytest** — Test execution, fixtures, and assertions
- **GitHub Actions** — Continuous integration (CI)
- **Git and GitHub** — Version control

## Project Structure

```text
open_library_automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── book_details_page.py
├── tests/
│   ├── test_home.py
│   ├── test_ui_search.py
│   ├── test_book_details.py
│   └── test_api_search.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Framework Architecture

The framework uses the **Page Object Model (POM)** pattern to separate page interactions from test logic.

- `BasePage` contains common functionality shared between pages.
- `HomePage` provides navigation to the Open Library homepage.
- `SearchResultsPage` contains locators and methods for interacting with book search results.
- `BookDetailsPage` contains locators for validating book details.
- `conftest.py` defines pytest fixtures for creating Page Object instances.
- `pytest.ini` contains test execution and Playwright configuration.

## Implemented Tests

| Test | Description | Status |
|---|---|---|
| UI TC01 | Search for "The Hobbit" and validate search results | Previously passed |
| UI TC02 | Open book details, compare titles, and navigate back | Implemented; validation pending |
| API TC01 | Search for books using the Open Library API | Passed locally |

**Note:** Open Library has experienced intermittent connectivity issues and human verification challenges during automated testing. These external conditions have affected test execution.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JuliaTrubchyk/open-library-automation.git
cd open-library-automation
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Chromium

```bash
python -m playwright install chromium
```

## Running Tests

Run all tests:

```bash
pytest
```

Run UI search tests:

```bash
pytest tests/test_ui_search.py -v
```

Run book details tests:

```bash
pytest tests/test_book_details.py -v
```

Run API tests:

```bash
pytest tests/test_api_search.py -v
```

## CI/CD — GitHub Actions

The project includes a GitHub Actions workflow designed to run UI and API tests automatically.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Chromium for Playwright.
5. Executes the pytest test suite.
6. Uploads available test artifacts when tests fail.

## Future Improvements

- Expand UI and API test coverage.
- Improve handling and reporting of external website availability issues.
- Introduce reusable API client methods.
- Add HTML test reports.
- Improve test data management and parametrization.
- Validate tests consistently in GitHub Actions.

## Author

QA Automation Practice Project
