FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR proj

COPY . .

RUN uv sync --frozen --no-dev

CMD "uv run src/main.py"
