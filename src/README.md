# Intro

This is the best shop application ever, if you don't already have it, you need it!

# Requirements
Mandatory:

    Python 3.8+

Application:

    requirements.txt

Development

    requirements-dev.txt

# Development setup

1. `python3 -m venv .venv && source .venv/bin/activate`
2. `pip3 install --upgrade pip`
3. `pip3 install -r requirements-dev.txt`

# Testing and linting

This repo uses pre-commit hooks to ensure the quality of the application. This means that everytime you commit something there will be checks running, among those are linting and unittests.

You can however run unit/integration tests or linting manually.

## Linting

Show warnings and errors: `pylint shop_app`

View errors only: `pylint shop_app --errors-only`


## Tests

Run unit tests only: `pytest --cov=shop_app tests/unit`

Run integration tests: `pytest --cov=shop_app tests/integration`

Run both unit and integration tests: `pytest --cov=shop_app`
