# Catalyst Kit: Your Universal Python Project Launchpad

[![Tests](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/ci.yml)
[![Docs](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/docs.yml/badge.svg)](https://{{GITHUB_USERNAME}}.github.io/{{PROJECT_SLUG}}/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Kickstart **any** Python project—whether you’re building a CLI tool, data pipeline, ML experiment, or full-blown web service. Catalyst Kit provides a robust, production-ready foundation with modern tooling, allowing you to focus on your specific application logic from day one.

## Why Use Catalyst Kit?

*   **Versatile Foundation:** Designed for flexibility. Start with examples for Web APIs (FastAPI), Command-Line Apps (Typer), or Data Pipelines, or easily adapt for data science, background jobs, and more.
*   **Production Ready:** Includes sensible defaults for testing, linting, formatting, security scanning, containerization (Docker), CI/CD (GitHub Actions), and dependency management (uv).
*   **Modern Tooling:** Leverages best-in-class tools like `uv`, `FastAPI`, `Typer`, `Ruff`, `Task`, `pytest`, and `MkDocs` for a smooth developer experience.
*   **Rapid Development:** Get straight to building features. The core structure, boilerplate, and essential tooling configurations are already in place.
*   **Easy Customization:** Designed to be easily adapted. Clear instructions guide you through renaming, configuring, and extending the template for your specific needs.

**Quick Links:**
*   🚀 **[Initializing Your Project from This Template](#initializing-your-project-from-this-template)**: The essential setup steps.
*   🤖 **[AI-Assisted Setup Guide](./docs/ai_assisted_setup.md)**: Let an AI guide you through customization (Recommended!).
*   🤔 **[Design Philosophy & FAQ](./docs/design_philosophy.md)**: Understand the choices made in this template.

## Core Technologies & Key Features

*   **Python Version:** 3.11+
*   **Dependency Management:** [`uv`](https://github.com/astral-sh/uv) (for virtual environment creation and lightning-fast dependency resolution)
*   **Build System:** [`hatchling`](https://hatch.pypa.io/latest/config/build/)
*   **Task Runner:** [`Task`](https://taskfile.dev/) (a simpler Make/Just alternative written in Go)
*   **Web Framework Example:** [`FastAPI`](https://fastapi.tiangolo.com/) (High-performance API development)
*   **CLI Framework Example:** [`Typer`](https://typer.tiangolo.com/) (Intuitive CLI creation, built on Click)
*   **Linting & Formatting:** [`Ruff`](https://github.com/astral-sh/ruff) (Extremely fast Python linter and formatter), [`Bandit`](https://bandit.readthedocs.io/en/latest/) (Security analysis), [`pip-audit`](https://pypi.org/project/pip-audit/) (Dependency vulnerability scanning)
*   **Testing:** [`pytest`](https://docs.pytest.org/) (Rich testing framework), [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/) (Coverage reporting)
*   **Containerization:** [`Docker`](https://www.docker.com/) & `docker-compose` (Multi-stage builds, development environment). See [Container Registry Guide](./docs/guides/container_registry.md) for details on pushing images.
*   **CI/CD:** [`GitHub Actions`](https://github.com/features/actions) (Automated testing, linting, security scans, documentation deployment)
*   **Documentation:** [`MkDocs`](https://www.mkdocs.org/) with the [`Material for MkDocs`](https://squidfunk.github.io/mkdocs-material/) theme
*   **Pre-commit Hooks:** Automated checks before commits (linting, formatting)
*   **Core Library Structure:** Centralized location (`src/your_core_library/`) for your reusable project logic. **Remember to rename this directory and update corresponding references!**
*   **Example Applications:** Demonstrations for common use cases (Web API, CLI, Data Pipeline).
*   **`.env` File Support:** Easy configuration management for environment variables.
*   **VS Code Integration:** Recommended extensions and settings.

### Code Coverage

Test coverage reports are generated using `pytest-cov`.

*   **Local HTML Report:** Run `task coverage` to execute tests and generate an interactive HTML report in the `htmlcov/` directory.
*   **CI Reports:** The GitHub Actions workflow automatically runs tests and generates coverage reports. An HTML report is uploaded as a downloadable artifact for each workflow run, accessible from the run's summary page on GitHub.

## Initializing Your Project from This Template

**IMPORTANT:** The very first step after using this template is to replace all placeholder values (like `your_core_library`, `your-project-name`, `{{GITHUB_USERNAME}}`, `{{PROJECT_SLUG}}`, etc.) with your actual project details. This includes directory names, configuration files (`pyproject.toml`, `Taskfile.yml`), and documentation links.

While this template provides a ready-to-run starting point, you'll want to customize it for your own project. We **strongly recommend** using the **[AI-Assisted Setup Guide](./docs/ai_assisted_setup.md)** for the most efficient way to rename and configure everything.

Alternatively, you can follow the **[Manual Setup Guide](./docs/guides/manual_setup.md)** for detailed step-by-step instructions.

### Prerequisites
{{ ... }}
## Local Development Setup

1.  **Initialize:** Run `task init` (or `task setup` followed by `task precommit:install`). This creates the virtual environment, installs dependencies, and sets up pre-commit hooks.
2.  **Activate Environment:** `source .venv/bin/activate` (or use your shell's equivalent).
3.  **Develop:** Make your code changes in `src/your_core_library/` and add/modify examples in `examples/`.

### Running the Examples

*   **Web Server (FastAPI):**
    ```bash
    task serve:web
    ```
    This starts the FastAPI example server (usually at `http://localhost:8000`).

*   **Command-Line Interface (Typer):**
    ```bash
    # Show help message
    task run:cli -- --help

    # Run with default options
    task run:cli

    # Run with custom options
    task run:cli -- --name "Your Name"
    ```

*   **Data Pipeline (Script):**
    ```bash
    task run:pipeline
    ```

### Visual Overview

```mermaid
graph TD
    subgraph "Template Structure"
        A["src/your_core_library/"] --> B("Core Library Logic"); # Placeholder!
        C["examples/"] --> D{"Example Types"};
        D --> E["web/ (FastAPI)"];
        D --> F["cli/ (Typer)"];
        D --> G["data_pipeline.py"];
        H["Taskfile.yml"] --> I["Build/Test/Lint Tasks"];
        H --> J["Example Runners (web, cli, pipeline)"];
        K["Dockerfile"] --> L["Container Image Build"];
        M["GitHub Actions"] --> N["CI/CD Pipeline"];
        O["uv / pyproject.toml"] --> P["Dependency Mgmt"];
        Q["MkDocs / docs/"] --> R["Project Documentation"];
        S["Testing (pytest)"] --> A;
        S --> E;
        S --> F;
        S --> G;
        T["Linting (Ruff)"] --> A;
        T --> E;
        T --> F;
        T --> G;
    end
```
*Note: This diagram uses Mermaid syntax. You can edit it directly or replace it with a standard image tag (`<img src="...">`) if preferred.*

{{ ... }}

## Committing, Versioning, and Releasing

This project uses Conventional Commits and Commitizen for standardized commit messages and automated version bumping. Pre-commit hooks are in place to ensure code quality.

For detailed information on the recommended commit workflow, how to handle pre-commit hooks, and the steps for versioning and releasing, please see the **[Releasing and Versioning Guide](./docs/guides/releasing_and_versioning.md)**.

## Testing

Run all tests:
```bash
task test
```

This command runs all tests defined in the `tests/` directory using `pytest`. It also generates a `coverage.xml` report (for tools like Codecov) and a `.coverage` data file.

### Viewing Test Coverage

To view a detailed HTML report of test coverage:

1.  **Generate the report:**
    *   Run `task coverage`: This will run all tests and then automatically generate the HTML report.
    *   Alternatively, if tests have already been run (and a `.coverage` file exists), you can generate only the HTML report by running: `task coverage:html`
2.  **Open the report:**
    Open the `htmlcov/index.html` file in your web browser.

This report provides an interactive way to see which lines of code are covered by tests and which are not.

## Linting and Formatting
{{ ... }}

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project template is licensed under the MIT License. See [LICENSE.md](./LICENSE.md) for details.
