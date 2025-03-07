FROM python:3.12-bookworm
WORKDIR /code
LABEL project_name="{{ cookiecutter.project_name }}"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv sync
ENV PATH="/code/.venv/bin:$PATH"

COPY . .
CMD ["python", "src/server.py"]
