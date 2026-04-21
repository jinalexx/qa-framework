# QA Automation Framework

A Selenium-based test automation framework for a job board web application, built with Python, pytest, and Page Object Model design pattern.

## Project Structure

```
qa-framework/
├── app.py              # Flask web application (job board)
├── conftest.py         # pytest fixtures and configuration
├── pages/
│   └── search_page.py  # Page Object Model
├── tests/
│   └── test_job_board.py  # Test cases
├── reports/            # HTML test reports and screenshots
└── .github/
    └── workflows/
        └── tests.yml   # CI/CD pipeline
```

## Features

- Page Object Model (POM) design pattern
- 8 automated UI tests using Selenium WebDriver
- HTML test report generation with pytest-html
- Screenshot capture on test execution
- CI/CD pipeline with GitHub Actions

## Test Coverage

- Homepage loads correctly
- All job listings displayed
- Results count accuracy
- Search by keyword functionality
- Search by location functionality
- Job detail page navigation
- Empty search returns all results
- Screenshot evidence capture

## Tech Stack

- Python 3.9
- Selenium WebDriver
- pytest + pytest-html
- Flask (test application)
- GitHub Actions (CI/CD)

## How to Run

```bash
# Install dependencies
pip install selenium pytest pytest-html flask

# Start the application
python app.py

# Run tests (in a new terminal)
pytest tests/test_job_board.py -v --html=reports/report.html
```

## Results

8/8 tests passing.
