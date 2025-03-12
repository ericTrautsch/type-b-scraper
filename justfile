default: 
    @just --list

# Format, lint, test
build: fmt lint test

fmt: 
    uv run ruff format

# Lint, not break on errors
lint: 
    -uv run ruff check

test:
    uv run pytest

# Run data scraper and processing
run:
    uv run ./src/main.py
