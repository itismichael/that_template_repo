# AI-Assisted Project Setup Guide

Welcome! This guide provides a comprehensive prompt you can use with an AI coding assistant (like GitHub Copilot Chat, Cascade, Claude, ChatGPT, etc.) to quickly customize this project template for your own needs.

## How to Use

1.  Copy the prompt below.
2.  Start a new chat session with your preferred AI coding assistant within your IDE, ensuring it has access to the entire cloned project directory.
3.  Paste the prompt and provide the requested information when the AI asks for it.
4.  **Crucially, carefully review all changes** made by the AI assistant to ensure they are correct and complete. You may need to guide the AI or perform some steps manually if it encounters difficulties, especially with complex refactoring like directory renaming.

## Master Prompt for AI Assistant

```
Hello! I've just cloned this universal Python project template and I need your help to customize it for my new project. Please guide me through the following steps. For each step, explain what you're going to do, perform the action, and then wait for my confirmation or further instructions before moving to the next.

**My Project Details (I will provide these when you ask):**
- My New Project Name (e.g., "Awesome API Service"):
- My Desired Core Library Name (e.g., "awesome_core_logic" - use snake_case):
- My GitHub Username (e.g., "myusername"):
- My Full Name (for pyproject.toml author):
- My Email (for pyproject.toml author):

**Customization Steps:**

1.  Gather My Project Details:
    - Ask me for "My New Project Name," "My Desired Core Library Name," "My GitHub Username," "My Full Name," and "My Email."

2.  Replace Project Name Placeholders:
    - Globally search for the placeholder `{{YOUR_PROJECT_NAME}}` and replace it with "My New Project Name" (the value I provide).
    - Files to pay close attention to include (but are not limited to):
        - `README.md`
        - `mkdocs.yml` (site_name, site_url, repo_url, repo_name)
        - `pyproject.toml` (project.name, project.description - you can use the new project name for the description initially)
        - `.github/workflows/ci.yml` (if any placeholders exist there)
        - Also, in `mkdocs.yml`, replace the default `site_name: "My Project Documentation"` with "My New Project Name Documentation".

3.  Replace GitHub Username Placeholders:
    - Globally search for the placeholder `{{YOUR_GITHUB_USERNAME}}` and replace it with "My GitHub Username" (the value I provide).
    - Files to pay close attention to include:
        - `README.md`
        - `mkdocs.yml` (site_url, repo_url, repo_name)

4.  Rename Core Library:
    - This is a critical step. The current core library is named `your_core_library` (located at `src/your_core_library`).
    - Rename the directory `src/your_core_library` to `src/‹My Desired Core Library Name›`.
    - Globally search for the string `your_core_library` and replace it with "My Desired Core Library Name" (the value I provide). This will affect:
        - Import statements in Python files (e.g., `from your_core_library.data_handler import DataHandler` should become `from ‹My Desired Core Library Name›.data_handler import DataHandler`). Check files in `examples/` (especially `examples/web/main.py`, `examples/cli.py`, `examples/data_pipeline.py`) and `tests/` (across all subdirectories like `tests/your_core_library/`, `tests/examples/web/`, `tests/examples/cli/`, `tests/examples/data_pipeline.py`).
        - `pyproject.toml` (e.g., in `[tool.hatch.build.targets.wheel] packages`, `[tool.ruff.lint.per-file-ignores]`, `[tool.coverage.run] source`, `[tool.mypy] mypy_path`).
        - `Taskfile.yml` (e.g., in `pytest` commands, `mypy` commands).
        - Test paths and discovery patterns if they explicitly use the name.
        - Any documentation that refers to it.

5.  Update `pyproject.toml` Metadata:
    - Set `project.authors` to `[{name = "My Full Name", email = "My Email"}]`.
    - You can also update `project.description` to something more specific if I provide it, or use "My New Project Name" as a default.

5b. (Optional) Review and Customize Example Applications:
    - This template now includes several examples in the `examples/` directory: a FastAPI web application (`examples/web/`), a Typer CLI application (`examples/cli.py`), and a data pipeline script (`examples/data_pipeline.py`). Corresponding tests are in `tests/examples/`.
    - Ask me if I want to keep all these examples. If not, you can help me remove specific examples and their corresponding test files/directories. For example, if I only want to build a CLI tool, we can remove `examples/web/`, `examples/data_pipeline.py`, `tests/examples/web/`, and `tests/examples/test_data_pipeline.py`.
    - Also, ask if I want to rename any of the examples to better suit my project's initial focus (e.g., renaming `examples/web/` to `examples/my_api_service/`). If so, ensure all relevant paths and configurations (e.g., in `Taskfile.yml`, `pyproject.toml` for coverage/test paths, `Dockerfile` if `examples/web` is renamed) are updated.
    - Remind me that if I remove examples, I should also update `pyproject.toml` (e.g., `tool.coverage.run.source`, `tool.pytest.ini_options.testpaths`) and `Taskfile.yml` (e.g., `serve:web`, `run:cli`, `run:pipeline` tasks) to reflect these changes.

5c. (Optional) Configure Docker for Examples/Custom Apps:
    - Inform me that the default `Dockerfile` in the project root is tailored for the FastAPI web application example located at `examples/web/`.
    - Ask if my primary goal for containerization involves this `examples/web/` app, another example (CLI, data pipeline), or a new custom application I plan to build using the template.
    - If I plan to containerize something other than `examples/web/`:
        - Explain that the existing `Dockerfile` will likely need to be adapted, or a new `Dockerfile` created (e.g., `Dockerfile.cli`, `Dockerfile.pipeline`).
        - Explain that `Taskfile.yml`'s `docker:build` command might need to be adjusted (e.g., to use a different `-f Dockerfile.custom` flag) or new dedicated build tasks created (e.g., `docker:build:cli`).
        - Offer to help create or adapt a `Dockerfile` for my chosen application and update/add `Taskfile.yml` commands.
    - Inform me that `Taskfile.yml` includes `task docker:build` (which uses the root `Dockerfile` by default) but does **not** include a `task docker:push` for pushing images to a remote registry.
    - Ask if I need to push my image to a container registry.
        - If yes, offer to guide me through the manual `docker tag` and `docker push` process after building the image.
        - Alternatively, offer to help me create a new `task docker:push` in `Taskfile.yml`, potentially using variables for the remote image name and tag. I can refer to the `docs/guides/container_registry.md` file for patterns and examples of how such a task could be structured and how to manage remote image names (e.g., using `.env` files).

6.  Final Review Reminder:
    - Remind me that I should thoroughly review all changes, commit them to version control, and then try running `task setup`, `task lint`, and `task test` to ensure everything is working correctly.
    - Suggest I might also want to manually review the `Taskfile.yml` for any path adjustments related to the core library name or removed/renamed examples that might have been missed.

Please proceed step-by-step.
```

## Important Considerations

- **AI Capabilities Vary:** Some AI assistants might handle file renaming and widespread refactoring better than others.
- **Review, Review, Review:** Automated changes can sometimes have unintended consequences. Always use `git diff` or your IDE's change tracking to review every modification before committing.
- **Iterative Process:** You might need to provide clarifications or break down complex steps further for the AI.
- **Manual Fallback:** If the AI struggles with a particular step (like directory renaming and updating all imports), you might need to perform that step manually.

Good luck, and happy coding!
