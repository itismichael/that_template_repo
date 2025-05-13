# Stage 1: Builder environment with uv and build tools
FROM python:3.11-slim AS builder

# Install uv, our super-fast Python package installer
ENV UV_VERSION=0.1.20 # Pin uv version for reproducibility, update as needed
RUN pip install --no-cache-dir uv==${UV_VERSION}

WORKDIR /opt/build

# Copy only the files needed to install dependencies first, for Docker layer caching
COPY pyproject.toml ./pyproject.toml

# Install all dependencies, including hatchling for building our local package
# This will create a virtual environment in /opt/build/.venv
RUN uv pip install --system --no-cache . # Install project itself (your_core_library) and its direct deps
RUN uv pip install --system --no-cache hatchling # Ensure hatchling is available for building
# Install optional dependencies for dev, test, lint
RUN uv pip install --system --no-cache .[dev,test,lint]

# Copy the rest of the source code for the core library
COPY src/ ./src/

# Build the wheel for our core library
# The wheel will be placed in /opt/build/dist/
RUN uv pip install --system --no-cache wheel && \
    python -m hatchling build --wheel

# Stage 2: Final runtime environment
FROM python:3.11-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Create a non-root user for security
RUN addgroup --system app && adduser --system --group app

# Copy the virtual environment (installed packages) from the builder stage
# This includes our compiled core_library wheel and all other dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin /usr/local/bin/

# Copy the application code (FastAPI example)
COPY examples/web/ ./web_example/

# Ensure correct ownership if files were copied as root
RUN chown -R app:app /app /usr/local/lib/python3.11/site-packages /usr/local/bin ./web_example/

USER app

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the application
# Assumes your FastAPI app instance is named 'app' in 'web_example.main'
CMD ["uvicorn", "web_example.main:app", "--host", "0.0.0.0", "--port", "8000"]
