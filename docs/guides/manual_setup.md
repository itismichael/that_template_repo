# Manual Project Setup Guide

This guide provides detailed manual steps for initializing a new project from the template. For a potentially faster and more automated approach, consider using the [AI-Assisted Setup Guide](../ai_assisted_setup.md).

## Setup Steps

1.  **Set Your Project Name & Core Library Name:**
    *   **Distribution Package Name:** The primary place to define your project's *distribution package name* (how it's known on PyPI, for example) is in `pyproject.toml`. Open it and update the `name` field under `[project]`:
        ```toml
        [project]
        name = "your-new-distribution-name" # e.g., my-awesome-package
        # ... other settings
        ```
    *   **Core Library (Python Import Package) Name:** This template includes a core library in `src/your_core_library/`. This is the name you'll use in Python import statements (e.g., `import your_core_library`). If you change the `name` in `pyproject.toml` (the distribution name) to something different from `your_core_library`, or simply wish to rename the default importable package, you should also:
        1.  Rename the directory: `src/your_core_library/` to `src/your_new_python_package_name/` (e.g., `src/my_awesome_lib/`).
        2.  Update all import statements throughout the project. Key areas include: `examples/web/app/main.py`, `examples/cli.py`, `examples/data_pipeline.py`, and their corresponding tests in `tests/examples/`. For example, change `from your_core_library.data_handler import ...` to `from your_new_python_package_name.data_handler import ...`.
        3.  Update configuration in `pyproject.toml`:
            *   `[tool.hatch.build.targets.wheel]`: Change `packages = ["src/your_core_library"]` to `packages = ["src/your_new_python_package_name"]`.
            *   `[tool.ruff.lint]`: If `your_core_library` is listed in `extend-select` or other Ruff settings, update it to `your_new_python_package_name`.
            *   `[tool.mypy]`: If your package name is listed under `mypy` settings (e.g. in `packages` or explicit module lists), update it there.
            *   `[tool.coverage.run]`: Update source paths if they explicitly mention `src/your_core_library`.
        *   **Tip:** Use your IDE's "Find and Replace in Files" feature to update import statements and configurations across the codebase. Search for `your_core_library`.

2.  **Replace General Placeholders:**
    *   Search globally in the project for `{{GITHUB_USERNAME}}` (e.g., in `README.md`, `mkdocs.yml`) and replace it with your actual GitHub username or organization name.
    *   Search globally for `{{PROJECT_SLUG}}` (this is often used for the repository name or display name, distinct from the Python package name, e.g., in `README.md`, `mkdocs.yml`) and replace it with your chosen project/repository name.
    *   **Tip:** Use your IDE's "Find and Replace in Files" feature for efficient global replacement of these placeholders.
    *   **Key files and areas to check for these placeholders and other initial setup details:**
        *   `README.md`: Update project title, description, and any URLs.
        *   `pyproject.toml`:
            *   `[project]`: Besides `name`, review and update `version`, `description`, `authors` (name and email: `authors = [{ name = "Your Name", email = "your@email.com" }]`), `keywords`, `classifiers`.
            *   `[project.urls]`: Update URLs like "Homepage", "Repository", "Documentation".
        *   `mkdocs.yml`: `site_name`, `site_url`, `repo_url`.
        *   `.github/workflows/*.yml`: Check for any specific naming if you've customized workflow triggers or job names extensively. Usually, these are generic.
        *   `CONTRIBUTING.md`: If it contains links back to the repository using placeholders, ensure they are updated.

3.  **Update Documentation Settings (`mkdocs.yml`):**
    *   Open `mkdocs.yml`.
    *   Set `site_name` to your project's display name (this is often derived from `{{PROJECT_SLUG}}` or a more descriptive title).
    *   Update `site_url` and `repo_url` to point to your project's documentation site (e.g., on GitHub Pages) and repository URL, respectively, once they are known.

4.  **Docker Image Name (Optional - if publishing images):**
    *   The default `Dockerfile` and the `task docker:build` command are configured for the FastAPI web application in `examples/web/`. If you intend to containerize a different application (e.g., the CLI tool, data pipeline, or your own custom app), you will need to adapt the `Dockerfile` and potentially the `Taskfile.yml`'s `docker:build` command.
    *   The `Taskfile.yml` uses `your-app-image` for local Docker builds (`task docker:build`).
    *   If you plan to publish Docker images to a registry (like Docker Hub, GHCR), you'll need to tag your image appropriately (e.g., `yourusername/your-project-name:latest`).
    *   You might want to customize the `CMD` in `tasks docker:build` in `Taskfile.yml` or add a dedicated `docker:push` task that uses your desired image name.
    *   See the [Container Registry Guide](./container_registry.md) for more guidance.

5.  **Review and Customize:**
    *   **Example Applications:** The template includes example applications in the `examples/` directory (FastAPI web app in `examples/web/`, Typer CLI in `examples/cli.py`, and a data pipeline script in `examples/data_pipeline.py`) and corresponding tests in `tests/examples/`. Review these examples. You may want to:
        *   Use them as a starting point.
        *   Modify them for your needs.
        *   Remove any examples that are not relevant to your project.
        *   If you remove or significantly alter examples, remember to update:
            *   `pyproject.toml`: Adjust `[tool.pytest.ini_options] testpaths` and `[tool.coverage.run] source` (and potentially `[tool.mypy]` configurations) to reflect the changes.
            *   `Taskfile.yml`: Remove or modify corresponding run tasks (e.g., `serve:web`, `run:cli`, `run:pipeline`).
            *   The `Dockerfile` if you remove or rename the `examples/web/` application or change its structure.
    *   Review the main `README.md` and remove or adapt sections (like the original template's setup guide, features list) to fit your actual project.
    *   Update `LICENSE.md` if you choose a different license (the default is MIT).
    *   Explore the `docs/` directory and adapt the existing guides or add your own project-specific documentation. Remove or update links to guides you might have deleted (e.g., if you remove the AI-assisted setup).

Once these steps are done, your project should be well-configured and ready for development!
