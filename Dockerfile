FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /proj

COPY . .

RUN uv sync --frozen --no-dev
RUN mkdir /output

ENTRYPOINT ["uv", "run", "src/main.py", "/output/output.csv"]
