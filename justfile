default: 
    @just --list

# Format, lint, test
build: fmt lint test

fmt: 
    ruff format

# Lint, not break on errors
lint: 
    -ruff check

test:
    uv run pytest

# Run data scraper and processing
run:
    uv run ./src/main.py
