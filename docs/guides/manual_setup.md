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
    *   **Core Library (Python Package) Name:** This template includes a core library in `src/your_core_library/`. If you change the `name` in `pyproject.toml` to something other than `your_core_library` (or simply wish to rename the default core library), you should also:
        1.  Rename the directory `src/your_core_library/` to `src/your_new_python_package_name/` (e.g., `src/my_awesome_lib/`).
        2.  Update all import statements throughout the project. Key areas include: `examples/web/main.py`, `examples/cli.py`, `examples/data_pipeline.py`, and their corresponding tests in `tests/examples/`. For example, change `from your_core_library.data_handler import ...` to `from your_new_python_package_name.data_handler import ...`.
        3.  Crucially, update the `packages` path in `pyproject.toml` under `[tool.hatch.build.targets.wheel]` to point to your new package directory. For example, if you renamed `src/your_core_library` to `src/my_new_lib`, it should look like:
            ```toml
            [tool.hatch.build.targets.wheel]
            packages = ["src/my_new_lib"]
            ```
            The default is `packages = ["src/your_core_library"]`.
        *   **Tip:** Use your IDE's "Find and Replace in Files" feature to update import statements across the codebase. Look for `from your_core_library` and `import your_core_library`.

2.  **Replace General Placeholders:**
    *   Search globally in the project for `{{GITHUB_USERNAME}}` (e.g., in `README.md`, `mkdocs.yml`) and replace it with your actual GitHub username or organization name.
    *   Search globally for `{{PROJECT_SLUG}}` (this is often used for the repository name or display name, distinct from the Python package name, e.g., in `README.md`, `mkdocs.yml`) and replace it with your chosen project/repository name.
    *   **Tip:** Use your IDE's "Find and Replace in Files" feature for efficient global replacement of these placeholders.
    *   **Key files to check for these placeholders:**
        *   `README.md`
        *   `pyproject.toml` (`[project.urls]`, `project.name` if you want it to match `{{PROJECT_SLUG}}`)
        *   `mkdocs.yml` (`site_name`, `site_url`, `repo_url`)
        *   `.github/workflows/ci.yml` (if any specific naming is used, though it's mostly generic)

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
            *   `pyproject.toml`: Adjust `[tool.pytest.ini_options] testpaths` and `[tool.coverage.run] source` to reflect the changes.
            *   `Taskfile.yml`: Remove or modify corresponding run tasks (e.g., `serve:web`, `run:cli`, `run:pipeline`).
            *   The `Dockerfile` if you remove or rename the `examples/web/` application.
    *   Review the main `README.md` and remove or adapt sections (like the original setup guide) to fit your project.
    *   Update `LICENSE.md` if you choose a different license (the default is MIT).
    *   Explore the `docs/` directory and adapt the existing guides or add your own project-specific documentation.

Once these steps are done, your project should be well-configured and ready for development!
