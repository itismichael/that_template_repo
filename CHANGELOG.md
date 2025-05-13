# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.3.2 (2025-05-13)

### Fix

- **typing**: configure mypy and address initial type errors
- **tasks**: resolve cyclic dependency for precommit:install and adjust setup

## 0.3.1 (2025-05-13)

### Fix

- **ci**: improve docker image secrity and ci configurations

## 0.3.0 (2025-05-13)

### Feat

- **versioning**: update bump task, use script to ask for user confirmation on the bump

### Refactor

- don't track .task/

## 0.2.1 (2025-05-13)

### Fix

- small change to test updated bump functionality

## 0.2.0 (2025-05-13)

### Feat

- **taskfile.yml**: refine setup, release, and commit tasks

### Fix

- **taskfile.yml**: update cz:bump command
- **taskfile.yml**: update commitizen bump task

### Refactor

- **.windsurf**: remove ide local folder that stores workflows, rules, etc

## [0.1.0] - 2025-05-13

### Added
- Initial project structure and template setup.
- Core library (`your_core_library`) and FastAPI app (`app`) separation.
- Docker support for containerization.
- `Taskfile.yml` for task automation.
- Basic linting, formatting, and testing setup.
- Commitizen setup for conventional commits and changelog generation.
- Pre-commit hooks for automated checks.
- GitHub Actions CI workflow placeholder.
- Comprehensive `.gitignore` and editor configurations.
- Example applications (web, CLI, data pipeline).
- MkDocs documentation structure with initial content and guides.
