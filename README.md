# Catalyst Kit: Your Universal Python Project Launchpad

[![Tests](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/ci.yml)
[![Docs](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/actions/workflows/docs.yml/badge.svg)](https://{{GITHUB_USERNAME}}.github.io/{{PROJECT_SLUG}}/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Kickstart **any** Python project—whether you’re building a CLI tool, data pipeline, ML experiment, or full-blown web service. Catalyst Kit provides a robust, production-ready foundation with modern tooling, allowing you to focus on your specific application logic from day one.

## Why Use Catalyst Kit?

*   **Unmatched Versatility:** Adapt Catalyst Kit for *any* Python project. Whether it's Web APIs (FastAPI), CLIs (Typer), Data Pipelines, ML models, or background services, start with a strong foundation and tailor it to your specific needs.
*   **Go Production-Ready, Instantly:** Launch with confidence. Benefit from pre-configured testing, linting, formatting, security scanning, Docker containerization, GitHub Actions CI/CD, and efficient `uv` dependency management from day one.
*   **Streamlined Developer Experience:** Work smarter, not harder. Catalyst Kit integrates cutting-edge tools like `uv`, `FastAPI`, `Typer`, `Ruff`, `Task`, `pytest`, and `MkDocs` for maximum efficiency and a delightful development workflow.
*   **Accelerate Your Development:** Focus on features, not boilerplate. With a well-defined structure and pre-configured tooling, you can skip the setup grind and start building your application immediately.
*   **Effortless Customization & Clear Guidance:** Make it your own, easily. Comprehensive instructions (including an AI-assisted setup guide) help you rename, configure, and extend the template to perfectly match your project's requirements.

**Quick Links:**
*   🚀 **[Initializing Your Project from This Template](#initializing-your-project-from-this-template)**: The essential setup steps.
*   🤖 **[AI-Assisted Setup Guide](./docs/ai_assisted_setup.md)**: Let an AI guide you through customization (Recommended!).
*   🤔 **[Design Philosophy & FAQ](./docs/design_philosophy.md)**: Understand the choices made in this template.

## Core Technologies & Key Features

This template integrates a suite of modern tools and practices to provide a robust starting point:

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

## Initializing Your Project from This Template

> **IMPORTANT:** The very first step after using this template is to replace all placeholder values (like `your_core_library`, `your-project-name`, `{{GITHUB_USERNAME}}`, `{{PROJECT_SLUG}}`, etc.) with your actual project details. These placeholders are present in multiple files and locations, including directory names (e.g., `src/your_core_library`), configuration files (e.g., `pyproject.toml`, `Taskfile.yml`), documentation, and CI/CD workflows. It is crucial to perform a project-wide search and replace to ensure all instances are updated.

While this template provides a ready-to-run starting point, you'll want to customize it for your own project. We **strongly recommend** using the **[AI-Assisted Setup Guide](./docs/ai_assisted_setup.md)** for the most efficient way to rename and configure everything.

Alternatively, you can follow the **[Manual Setup Guide](./docs/guides/manual_setup.md)** for detailed step-by-step instructions.

### Prerequisites

Before you begin, ensure you have the following tools installed on your system:

*   **Python:** Version 3.11 or newer. This is required to run the project code and its dependencies. You can download it from [python.org](https://www.python.org/).
*   **Git:** Required for cloning the project template from GitHub and for version control. You can download it from [git-scm.com](https://git-scm.com/).
*   **Task:** This project uses Task as a task runner. You'll need it to execute commands defined in `Taskfile.yml` (like `task init`). Installation instructions can be found at [taskfile.dev](https://taskfile.dev/installation/).

**Recommended for Full Functionality:**

*   **Docker and Docker Compose:** While not strictly required for basic local development of all examples, Docker is used for containerizing applications and ensuring a consistent development environment. It's highly recommended for leveraging all features of this template, especially for building and running services in a production-like manner.
    *   Install Docker from [docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
    *   Docker Compose is typically included with Docker Desktop. For Linux, you might need to install it separately: [docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

The `task init` command will handle the setup of the Python virtual environment and the installation of project-specific dependencies (including `uv`) using `uv` under the hood. You do not need to install `uv` manually beforehand.

## Local Development Setup

Getting your local development environment set up involves two main steps:

1.  **Initialize Your Project:**
    ```bash
    task init
    ```
    This is the primary command to get your project ready. It performs several key actions:
    *   Creates a Python virtual environment in a `.venv` directory (if one doesn't already exist).
    *   Installs all necessary dependencies, including those for production and development (e.g., `pytest`, `ruff`).
    *   Sets up pre-commit hooks, which automatically run checks (like linting and formatting) before you make a commit. This helps maintain code quality.

    *Alternatively, you can run the setup steps individually:*
    *   `task setup`: Creates the virtual environment and installs dependencies.
    *   `task precommit:install`: Installs the pre-commit hooks.
    Running `task init` is generally recommended as it covers both.

2.  **Activate the Virtual Environment:**
    Once the virtual environment is created, you need to activate it in your current shell session. This isolates your project's dependencies from other Python projects on your system.

    *   **Linux/macOS (bash/zsh):**
        ```bash
        source .venv/bin/activate
        ```
    *   **Linux/macOS (fish):**
        ```bash
        source .venv/bin/activate.fish
        ```
    *   **Windows (Command Prompt):**
        ```bash
        .venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```bash
        .venv\Scripts\Activate.ps1
        ```
    *   **Windows (Git Bash):**
        ```bash
        source .venv/Scripts/activate
        ```
    After activation, your shell prompt will usually change to indicate that you are working inside the virtual environment (e.g., `(.venv) your-prompt$`). For more information on virtual environment activation, refer to the official Python `venv` documentation.

3.  **Start Developing:**
    With the environment initialized and activated, you're ready to:
    *   Make your code changes in `src/your_core_library/`.
    *   Add or modify example applications in the `examples/` directory.
    *   Run tests, linters, and other development tasks using `task <task-name>`.

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

## Committing, Versioning, and Releasing

This project uses Conventional Commits and Commitizen for standardized commit messages and automated version bumping. Pre-commit hooks are in place to ensure code quality.

For detailed information on the recommended commit workflow, how to handle pre-commit hooks, and the steps for versioning and releasing, please see the **[Releasing and Versioning Guide](./docs/guides/releasing_and_versioning.md)**.

## Testing

This project uses `pytest` for running tests. Test execution also generates coverage data using `pytest-cov`.

Run all tests and generate basic coverage data:
```bash
task test
```
This command runs all tests defined in the `tests/` directory. It produces:
*   A `coverage.xml` report (useful for tools like Codecov).
*   A `.coverage` data file (used for generating HTML reports).

### HTML Coverage Report

For a more detailed and browsable view of test coverage:

1.  **Generate the report:**
    *   Run `task coverage`: This executes all tests and then automatically generates the HTML report in the `htmlcov/` directory.
    *   Alternatively, if tests have already been run (and a `.coverage` file exists), generate only the HTML report by running: `task coverage:html`
2.  **Open the report:**
    Open `htmlcov/index.html` in your web browser. This report provides an interactive way to see which lines of code are covered by tests.

### CI Coverage Reports

The GitHub Actions workflow also automatically runs tests and generates coverage reports. An HTML report is uploaded as a downloadable artifact for each workflow run, accessible from the run's summary page on GitHub.

## Linting and Formatting

This project uses a combination of powerful tools to ensure code quality, consistency, and security. These are typically run via `Task` commands and are also integrated into pre-commit hooks.

*   **`task lint`**: This is the primary command to check your code. It runs:
    *   **Ruff:** An extremely fast Python linter that checks for a wide array of errors and style issues. It also handles import sorting.
    *   **Bandit:** A tool designed to find common security issues in Python code.
    *   **pip-audit:** Scans your installed Python packages for known vulnerabilities.
        *   **Note on pip-audit artifacts:** When `pip-audit` runs (e.g., via `task lint` or `task security:scan`), it may generate files such as `columns` or `pip-audit-report.*`. These files are used for its internal processing or reporting. They are automatically ignored by Git (as specified in `.gitignore`), are safe to delete, and can be removed by running `task clean`.

*   **`task format`**: This command automatically formats your code using Ruff's built-in formatter, ensuring a consistent code style throughout the project.

*   **Pre-commit Hooks:** The project is configured with pre-commit hooks that automatically run linters and formatters (primarily Ruff) on staged files before each commit. This helps catch issues early and maintain consistency without manual intervention. You can set these up by running `task precommit:install` (which is also part of `task init`).

Regularly running these commands and ensuring your pre-commit hooks are active will help maintain a high-quality and secure codebase.

## Future Improvements / TODO

This Catalyst Kit template is actively maintained, and we envision several enhancements for future releases. Contributions and suggestions are welcome! Here are some ideas currently on our radar:

*   **Expand Example Use-Cases:** Introduce more diverse examples, such as a basic Machine Learning model training structure, a simple background worker setup, or integration with a common database.
*   **Advanced Configuration Guide:** Develop a dedicated document detailing advanced configuration options for `pyproject.toml` (Hatch build settings, tool configurations like Ruff/pytest), `Taskfile.yml` customization, and deeper `uv` usage.
*   **Detailed Docker Guidance:** Enhance documentation on advanced Docker topics, including optimizing multi-stage builds for production, best practices for image security, and more complex `docker-compose` scenarios.
*   **Troubleshooting Guide:** Compile a "Troubleshooting Common Issues" page in the main documentation, addressing potential setup problems, tool conflicts, or frequently asked questions.
*   **Benefits of `uv`:** Add a section or link to resources explaining the advantages of `uv` (speed, dependency resolution) for users who may be unfamiliar with it compared to traditional tools like `pip` and `venv`.
*   **Interactive Project Initializer:** Explore the possibility of a more interactive `cookiecutter`-like CLI tool or script to help users customize project names, select examples, and configure initial settings more easily.
*   **Integration with More Services:** Provide examples or guides for integrating with other common services, such as Celery for task queues or different cloud provider SDKs.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project template is licensed under the MIT License. See [LICENSE.md](./LICENSE.md) for details.
