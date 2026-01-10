FROM python:3.13.11-slim 

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code 

# Copy dependency files first (better layer caching)
COPY pyproject.toml .python-version uv.lock ./
# Install dependencies from lock file 
# (ensures reproducible builds - dependencies in VE in Dockerimage are exactly the same as in VE)
RUN uv sync --locked 
COPY ingest_data.py .

ENTRYPOINT [ "uv", "run", "python", "/code/ingest_data.py" ]