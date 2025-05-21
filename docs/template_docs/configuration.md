# Configuration Guide

This guide provides an overview of how to configure a project initialized with the Catalyst Kit template. Understanding these configuration points will help you tailor the project to your specific needs.

## Environment Variables & Local Development

Modern applications often rely on environment variables to manage settings that vary between deployment environments (development, staging, production).

*   **`.env` Files:** For local development convenience, you can use a `.env` file in the project's root directory. This file allows you to define environment variables that your application can load.
    *   **Usage:** Tools like `docker-compose` can automatically load `.env` files. If your application uses Pydantic for settings management (as shown in the examples), it can also be configured to load variables from an `.env` file (e.g., using `python-dotenv` integration).
    *   **Security:** **Crucially, `.env` files should always be listed in your `.gitignore` file and never committed to version control.** They often contain sensitive information like API keys or database credentials. A `.env.example` file is often provided as a template.

*   **Pydantic's `BaseSettings`:** The example FastAPI application (`examples/web/app/config.py`) demonstrates using Pydantic's `BaseSettings`. This powerful feature allows your application to load configuration settings from environment variables (and `.env` files if configured). This makes your application highly adaptable to different environments without code changes, as settings are injected externally.

## Key Configuration Files

Several files in the project root and specific directories control its behavior, dependencies, and tooling.

*   **`pyproject.toml`:** This is a central configuration file for Python projects, based on PEP 518. In Catalyst Kit, it manages:
    *   **Project Metadata:** Name, version, description, authors, etc.
    *   **Dependencies:** Project dependencies are listed here and managed by `uv` (or `pip`/`pdm`/`poetry` if you adapt the template).
    *   **Build System:** Configuration for the build backend (e.g., `hatchling`).
    *   **Tool Configuration:** Settings for various development tools are often consolidated here:
        *   **Ruff:** Linter and formatter settings.
        *   **Mypy:** Static type checker settings.
        *   **Pytest:** Testing framework configuration.
        *   **Coverage.py:** Test coverage measurement settings.
        *   **Commitizen:** Conventional commit message formatting.

*   **`Taskfile.yml`:** This file is for the [Task](https://taskfile.dev) runner. It defines a series of tasks (scripts and commands) for common development operations such as:
    *   Initializing the project (`task init`).
    *   Running tests (`task test`).
    *   Linting and formatting code (`task lint`, `task format`).
    *   Building documentation (`task docs:serve`).
    *   Building and running Docker containers.
    You can customize this file to add your own project-specific tasks or modify existing ones.

*   **`mkdocs.yml`:** This file configures your project's documentation site, which is built using [MkDocs](https://www.mkdocs.org/) with the Material for MkDocs theme. Key settings include:
    *   `site_name`: The name displayed on your documentation site.
    *   `nav`: The navigation structure for your documentation pages.
    *   `theme`: Theme-specific settings, like palette, features, and logo.
    *   `plugins`: Configuration for any MkDocs plugins being used (e.g., for search, diagrams).

## Configuring Example Applications (Optional)

The example applications provided with Catalyst Kit (e.g., the FastAPI app in `examples/web/`) have their own internal configurations.

*   For instance, the FastAPI example in `examples/web/app/config.py` uses Pydantic for its settings, as mentioned earlier.
*   For details on running and potentially configuring these examples, please refer to the [Usage Guide](./usage.md) or the `README.md` files within their respective directories (e.g., `examples/web/README.md`).

## Customizing Core Library and Project Name

When you first set up a project from the Catalyst Kit template, you'll typically rename the placeholder core library (e.g., `your_core_library`) and adjust project name placeholders throughout the codebase.

*   These initial customizations are critical as they affect import paths, script configurations, and metadata in files like `pyproject.toml`, `Taskfile.yml`, and documentation.
*   For detailed instructions on performing this initial template customization, please refer to the guides:
    *   [Manual Setup Guide](./guides/manual_setup.md)
    *   [AI-Assisted Setup Guide](./guides/ai_assisted_setup.md) (if applicable)

By understanding these configuration aspects, you can effectively manage and adapt your Catalyst Kit-based project.
