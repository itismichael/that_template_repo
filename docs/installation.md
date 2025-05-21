# Installation Guide

This guide explains how to set up and install a project that has been created using the Catalyst Kit template.

## Prerequisites

Before you begin, ensure you have the following tools installed on your system:

*   **Python:** Version 3.11 or higher is recommended.
*   **Git:** For version control and cloning the project.
*   **Task:** A task runner used for project automation (`taskfile.dev`).
*   **Docker and Docker Compose:** Recommended for full functionality, including running containerized services and ensuring consistent environments.

Please refer to the main project [README.md](https://github.com/{{GITHUB_USERNAME}}/{{PROJECT_SLUG}}/blob/main/README.md) for links and installation instructions for these tools.

## Setup Steps

Follow these steps to get your project up and running:

1.  **Initialize the Project:**
    The primary setup command is `task init`. Navigate to your project's root directory in your terminal and run:
    ```bash
    task init
    ```
    This command automates several setup processes:
    *   Creates a Python virtual environment (typically in a `.venv` directory).
    *   Installs all necessary project dependencies using `uv`, a fast Python package installer and resolver.
    *   Sets up pre-commit hooks to help maintain code quality and consistency.

2.  **Activate the Virtual Environment:**
    After `task init` completes, you need to activate the virtual environment to use the project-specific Python interpreter and installed packages. The command to activate it varies depending on your operating system and shell:

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
        .\.venv\Scripts\activate.bat
        ```

    *   **Windows (PowerShell):**
        ```bash
        .venv\Scripts\Activate.ps1
        ```
        (Note: If you encounter an error about script execution policy on PowerShell, you may need to run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` and then try again.)

    *   **Windows (Git Bash):**
        ```bash
        source .venv/Scripts/activate
        ```
    You should see the virtual environment's name (e.g., `(.venv)`) prepended to your shell prompt, indicating it's active.

3.  **Ready for Development:**
    With the virtual environment activated, your project is now ready for development. You can start running the example applications, executing tests, and working with the core library.

    For available project tasks and commands, you can usually list them by running:
    ```bash
    task --list
    ```

Happy coding!
