# Usage Guide

This guide helps you quickly get started with and test the basic functionality of the example applications provided in this template.

## Prerequisites

*   The project should be initialized as per the `README.md` or [AI-Assisted Setup Guide](./ai_assisted_setup.md).
*   You have run `task setup` to create the virtual environment and install dependencies.
*   The virtual environment is activated (`source .venv/bin/activate`).

## Running the Examples

This template provides tasks to run each example application.

### 1. FastAPI Web Application (`examples/web/`)

This example demonstrates a simple FastAPI web server.

**To run the server:**

```bash
task serve:web
```

This will start the Uvicorn server, typically on `http://127.0.0.1:8000`. The server will automatically reload when you make changes to the code within `examples/web/` or your core library.

**Interacting with API Endpoints:**

Once the server is running, you can interact with the default API endpoints.

#### Root Endpoint (`/`)

This endpoint provides a basic welcome message.

```bash
curl http://127.0.0.1:8000/
```

**Expected Response (Default):**

```json
{
  "message": "Welcome to your_core_library's FastAPI application!",
  "greeting": "Hello from {{YOUR_PROJECT_NAME}}!"
}
```

*   **Note:** `your_core_library` and `{{YOUR_PROJECT_NAME}}` are placeholders. These values will change after you customize the template.

#### Health Check Endpoint (`/health`)

This endpoint can be used to check if the application is running and healthy.

```bash
curl http://127.0.0.1:8000/health
```

**Expected Response:**

```json
{
  "status": "healthy"
}
```

#### Processing Endpoint (`/process/`)

This endpoint demonstrates calling a function from your core library.

```bash
curl -X POST http://127.0.0.1:8000/process/ \
     -H "Content-Type: application/json" \
     -d '{"data": "sample input string"}'
```

**Expected Response (Default):**

```json
{
  "input_data": "sample input string",
  "processed_data": "Processed by your_core_library.CoreProcessor: SAMPLE INPUT STRING"
}
```

*   **Note:** `your_core_library` is a placeholder and will change after customization.

**Accessing API Documentation (Swagger & ReDoc):**

FastAPI automatically generates interactive API documentation. Once your server is running, you can access them in your browser:

*   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. Typer CLI Application (`examples/cli.py`)

This example demonstrates a simple command-line interface built with Typer.

**To run the CLI:**

```bash
task run:cli -- --name Cascade
```
Or for help:
```bash
task run:cli -- --help
```

**Expected Response (for `--name Cascade`):**

```
Hello Cascade
Processed by your_core_library.CoreProcessor: CASCADE
```
*   **Note:** `your_core_library` is a placeholder and will change after customization.

### 3. Data Pipeline Script (`examples/data_pipeline.py`)

This example demonstrates a basic data extraction, transformation, and loading (ETL) process.

**To run the pipeline:**

```bash
task run:pipeline
```

**Expected Output (will vary slightly due to random data, but structure is key):**

```
INFO:your_core_library.logging_config:ETL process started.
INFO:your_core_library.logging_config:Extracting data...
INFO:your_core_library.logging_config:Transforming data...
INFO:your_core_library.logging_config:Loading data...
INFO:your_core_library.logging_config:Transformed data loaded: [{'id': 1, 'name': 'Product A', 'price': 10.0, 'processed_name': 'PRODUCT A'}, ...]
INFO:your_core_library.logging_config:ETL process completed.
```
*   **Note:** `your_core_library` in the log messages is a placeholder and will change after customization. The exact data will also vary as it's simulated.

## Dockerizing the FastAPI Web Example

This template includes a `Dockerfile` configured for the FastAPI web example (`examples/web/`).

**To build the Docker image:**

```bash
task docker:build
```
This creates an image named `your-app-image:latest` by default (or as configured by `IMAGE_NAME_LOCAL` in `Taskfile.yml` or `.env`).

**To run the Docker container:**

```bash
task docker:run
```
This runs the container, mapping port 8000. You can then interact with the API as described above.

For pushing to a container registry, please see the [Container Registry Guide](./guides/container_registry.md).

## Next Steps

After verifying these basic examples, you can start building out your application's specific features. Remember to:

*   Define your core logic, data models, and utility functions in `src/your_core_library/` (or your renamed library).
*   If building a web API, add new API endpoints and routers in `examples/web/routers/` (or your chosen app structure).
*   If building a CLI, expand `examples/cli.py` with more commands and options.
*   If building data pipelines, enhance `examples/data_pipeline.py` or create new pipeline scripts.
*   Write tests for your new functionality in the `tests/` directory, ensuring good coverage.
*   Update or add new documentation pages as your project grows.
