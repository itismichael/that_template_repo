# Stage 1: Builder environment with uv and build tools
FROM python:3.11-slim AS builder

# Install uv, our super-fast Python package installer
# Pin uv version for reproducibility, update as needed
ENV UV_VERSION=0.1.20
RUN pip install --no-cache-dir uv==${UV_VERSION}

WORKDIR /opt/build

# Copy project files necessary for building the wheel and installing runtime deps
COPY pyproject.toml ./pyproject.toml
COPY src/ ./src/
# If your setup needs other files like README.md for hatchling to build, copy them too.
# COPY README.md ./README.md

# First, build the wheel for our core library.
# Install hatchling and wheel temporarily for this build step.
RUN uv pip install --system --no-cache hatchling wheel
# The wheel will be placed in /opt/build/dist/
RUN python -m hatchling build --wheel

# Now, create a clean installation directory for runtime dependencies.
ENV RUNTIME_DEPS_DIR=/opt/runtime_deps
RUN mkdir -p $RUNTIME_DEPS_DIR

# Install ONLY production/runtime dependencies into the target directory.
# 'uv pip install .' installs the current project (which includes its wheel if pyproject.toml is set up for it)
# and its runtime dependencies (specified in [project.dependencies]).
# It will NOT install optional groups like [dev, test, lint] by default.
RUN uv pip install --no-cache --target $RUNTIME_DEPS_DIR .

# Stage 2: Final runtime environment
FROM python:3.11-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Create a non-root user for security
RUN addgroup --system app && adduser --system --group app

# Copy the cleanly installed runtime dependencies from the builder stage
COPY --from=builder $RUNTIME_DEPS_DIR /usr/local/lib/python3.11/site-packages/
# If executables from dependencies were installed into a bin within $RUNTIME_DEPS_DIR, copy them too.
# Example: COPY --from=builder /opt/runtime_deps/bin /usr/local/bin/

# Copy the application code (FastAPI example)
COPY examples/web/ ./web_example/

# Ensure correct ownership for copied files
# Grouping chown operations
RUN chown -R app:app /app /usr/local/lib/python3.11/site-packages ./web_example/
# If /usr/local/bin was copied and needs chown:
# RUN chown -R app:app /usr/local/bin

USER app

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the application
CMD ["uvicorn", "web_example.main:app", "--host", "0.0.0.0", "--port", "8000"]
