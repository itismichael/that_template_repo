# Contributing to [Your Project Name]

We welcome contributions to [Your Project Name]! Please follow these guidelines to help us manage the process effectively.

## Getting Started

- Ensure you have Python 3.11 or higher installed.
- Ensure you have `task` (Go Task runner) installed. See https://taskfile.dev/installation/
- Clone the repository:
  ```bash
  git clone <repository-url>
  cd [Your Project Name]
  ```
- Initialize the project environment and install dependencies:
  ```bash
  task init
  ```
- Ensure you have an up-to-date main branch:
  ```bash
  git checkout main
  git pull origin main
  ```
- Create a new branch for your changes:
  ```bash
  git checkout -b your-feature-or-bugfix-branch-name
  ```

## Making Changes

- Follow the coding style and conventions used in the project (see linting/formatting tasks).
- Ensure your changes pass all tests (`task test`).
- Add new tests for new features or bug fixes.
- Update documentation if necessary.
- Commit your changes with a clear and descriptive commit message. For detailed instructions on the commit process, including how to work with pre-commit hooks and Commitizen, please see the [Releasing and Versioning Guide](./docs/guides/releasing_and_versioning.md).

## Submitting a Pull Request

- Push your branch to your fork on GitHub.
- Create a Pull Request against the `main` branch of the upstream repository.
- Provide a clear description of the changes in your PR.
- Link to any relevant issues.
- Ensure your PR passes all CI checks.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

Thank you for contributing!
