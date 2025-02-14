FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

COPY . .

RUN uv sync --frozen --no-dev
