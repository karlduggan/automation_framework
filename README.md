# Automation Framework

This repository contains a robust automation framework designed for scalable and maintainable UI.

## Key Components

| Area             | Details                                                                                      |
|------------------|----------------------------------------------------------------------------------------------|
| **Language/Framework** | Python with [Playwright](https://playwright.dev/python/) for UI automation                |
| **Test Runner**        | [Pytest](https://docs.pytest.org/) – supports fixtures, parametrization, and hooks        |
| **Design Pattern**     | Page Object Model – keeps locators and methods separate from tests                        |
| **Reporting**          | [Allure](https://docs.qameta.io/allure/) – integrated via pytest plugin for detailed HTML reports |             |
| **CI/CD**              | Jenkins pipeline runs tests on code push or pull request, iterations                      |
| **Parallel Execution** | Achieved using `pytest-xdist` or Playwright's native parallelism                         |
| **Cross-browser**      | Configured via Playwright (Chromium, Firefox, WebKit) using CLI args or config           |
| **Utilities**          | Custom utility classes for logging with Python `logging` module for debugging and error tracking, Browser handlers and helper function

## Getting Started

1. **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```
2. **Run tests:**  
    ```bash
    pytest
    ```
3. **Generate reports:**  
    ```bash
    pytest --alluredir=allure-results
    allure serve allure-results
    ```

## Folder Structure

- `tests/` – Test cases
- `pages/` – Page Object classes
- `utils/` – Utility modules (API, DB, data)
- `logs/` – Log files
- `reports/` – Test reports

