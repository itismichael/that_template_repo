# Releasing New Versions & Changelog Management

This project uses a streamlined approach to versioning, tagging, and changelog generation, powered by [Commitizen](https://commitizen-tools.github.io/commitizen/) and [Conventional Commits](https://www.conventionalcommits.org/). This guide makes it easy to release new versions of your project.

## Core Concepts

*   **Semantic Versioning (SemVer):** Versions are in the format `MAJOR.MINOR.PATCH` (e.g., `1.2.3`).
    *   `MAJOR` version when you make incompatible API changes.
    *   `MINOR` version when you add functionality in a backward-compatible manner.
    *   `PATCH` version when you make backward-compatible bug fixes.
    (Note: For `0.x.y` versions, even minor changes or breaking changes often increment the `MINOR` version, as per the `major_version_zero = true` setting in `pyproject.toml`.)

*   **Conventional Commits:** Your commit messages follow a standard format (e.g., `feat: add new login endpoint`, `fix: resolve issue with user lookup`). These structured messages allow Commitizen to automatically determine the correct SemVer bump and update the changelog. You create these using `task cz:commit`.

*   **Changelog:** `CHANGELOG.md` is automatically updated by Commitizen during the release process. You should manually curate the notes for the `[Unreleased]` section before making a release.

## Understanding the Commit Workflow: Pre-commit Hooks and Staging

This project uses [pre-commit hooks](https://pre-commit.com/) to automatically check and format your code *before* it's committed. Sometimes, these hooks will modify your files (e.g., to fix formatting). It's crucial to handle this correctly to ensure your commit includes these automated changes and you don't lose your interactively entered commit message from Commitizen.

**Always follow this workflow for every commit:**

1.  **Make your code changes and stage them:**
    ```bash
    # ...make your changes...
    git add <your-changed-files>
    # or, to stage all changes:
    git add .
    ```

2.  **(Recommended) Run pre-commit hooks manually first:**
    This step is optional but highly recommended, especially if you suspect files might be modified by formatters. It allows you to see and review any automatic modifications *before* attempting to use Commitizen.
    ```bash
    task precommit:run
    ```

3.  **Review and re-stage any modifications made by hooks:**
    If the previous step (or the commit attempt in step 4) shows that pre-commit hooks modified any files, those files will be in a modified state but potentially no longer fully staged for the commit (because they were changed after your last `git add`). You **must** review these automated changes and stage them again:
    ```bash
    # See what the hooks changed (optional, but good practice)
    git diff <files-modified-by-hooks>

    # Stage the changes made by the hooks
    git add <files-modified-by-hooks>
    # or, if you're sure all unstaged changes are from hooks and are desired:
    git add .
    ```

4.  **Create your commit using Commitizen:**
    Now that all files are staged and conform to project standards (i.e., pre-commit hooks should make no further changes), use the Commitizen task. This ensures your commit message adheres to the [Conventional Commits](https://www.conventionalcommits.org/) specification.
    ```bash
    task cz:commit
    ```
    Follow the interactive prompts to describe your changes. If pre-commit hooks pass without further modifications, your commit will be successful.

    *If pre-commit hooks still fail at this stage (i.e., exit with an error after you've re-staged their changes), it means there's an issue that wasn't auto-fixable (e.g., a critical linting error or a security vulnerability). You'll need to address this manually before you can commit.*

## The Release Workflow

This workflow assumes you are on your main branch (e.g., `main` or `master`) and it's ready for a release.

**1. Day-to-Day Development:**

*   Make your code changes.
*   Stage your changes (`git add .`).
*   Commit your changes using `task cz:commit`. This will guide you through creating a Conventional Commit message.
*   Push your commits regularly (`git push`).

**2. Preparing for a Release:**

When you're ready to publish a new version:

   a.  **Ensure `main` Branch is Up-to-Date:**
       Make sure your local `main` branch has all the latest changes from your remote repository and that all desired features/fixes are merged.
       ```bash
       git checkout main
       git pull origin main
       ```

   b.  **Curate `[Unreleased]` Changelog Section (Important!):**
       Open `CHANGELOG.md`. Review the `## [Unreleased]` section. Add, edit, or remove entries to ensure they are clear, user-friendly release notes for the upcoming version. These notes will be automatically moved under the new version heading by Commitizen.
       Commit these changes to `CHANGELOG.md` using the Commitizen task:
       ```bash
       git add CHANGELOG.md
       task cz:commit # Use type 'docs', scope 'changelog', e.g., "docs(changelog): Prepare release notes for vX.Y.Z"
       git push
       ```

   c.  **Dry Run the Version Bump (Optional but Recommended):**
       See what Commitizen plans to do without making any changes:
       ```bash
       task cz:bump
       ```
       This will tell you the current version, the next version it calculated based on your commits, and what files it would change.

   d.  **Perform the Version Bump & Create Tag:**
       This is the core release step. It will:
       *   Automatically determine the new version based on your conventional commits since the last tag.
       *   Update the version in `pyproject.toml`.
       *   Update `CHANGELOG.md` (moves entries from `[Unreleased]` to the new version).
       *   Commit these version and changelog updates with a "chore(release): bump version..." message.
       *   Create a Git tag for the new version (e.g., `0.2.0`).
       ```bash
       task cz:bump -- --no-dry-run
       ```
       *(Note the `--` which is required by `go-task` to pass flags to the underlying command.)*

   e.  **Push Changes and Tag to Remote:**
       Push the bump commit (created in the previous step) and the new tag (and any other tags) to your remote repository (e.g., GitHub):
       ```bash
       task release:push
       ```
       This task typically pushes the current branch and all tags (`git push origin <branch_name> --tags`).

### Troubleshooting a Failed Version Bump

Sometimes, a version bump might not go as planned (e.g., an incorrect version is tagged, or the process fails midway). If you need to correct a bump:

1.  **Primarily rely on `cz bump` (or `task cz:bump`) for versioning and tagging.** Avoid manual edits to version numbers in `pyproject.toml` or manual `git tag` commands if you intend to use the automated bump process, as this can lead to conflicts.
2.  **If a bump goes wrong:**
    *   Reset your local branch to the commit *before* the incorrect bump. You can find the commit hash using `git log`:
        ```bash
        git reset --hard <commit_hash_before_bad_bump>
        ```
    *   Delete the incorrect local Git tag:
        ```bash
        git tag -d <incorrect_tag_name>
        ```
    *   If the incorrect tag or bump commit was pushed to the remote repository:
        *   Delete the remote tag: `git push --delete origin <incorrect_tag_name>`
        *   If the erroneous bump commit was pushed, you'll need to ensure your local branch is correct, then push it, potentially with force (`git push --force origin <branch_name>`). **Caution:** Force-pushing can be disruptive if others have pulled the incorrect commit. Communicate with your team if this is a shared branch.
    *   Make any necessary code corrections or changelog adjustments.
    *   Commit these changes using `task cz:commit`.
    *   Run the bump process again:
        ```bash
        task cz:bump -- --no-dry-run
        task release:push
        ```

And that's it! Your new version is released and tagged.

## Handling the Very First Release (e.g., `0.1.0`)

For the *very first release* of your project (e.g., `0.1.0` after initializing from this template), the process is slightly more manual because there are no previous tags for Commitizen to compare against:

1.  **Initial Commits:** Make your initial project setup commits (these should also be conventional commits, e.g., using `task cz:commit`).
2.  **Finalize `CHANGELOG.md`:** Manually edit `CHANGELOG.md`. Move all relevant changes from the `[Unreleased]` section to a new `## [0.1.0] - YYYY-MM-DD` section. Commit this changelog update using `task cz:commit` (e.g., `docs(changelog): Finalize changelog for v0.1.0`).
3.  **Manually Tag:** Tag the commit that includes the finalized changelog and version-ready code:
    ```bash
    git tag 0.1.0
    ```
4.  **Push Commits and Tag:**
    ```bash
    git push origin main # Or your default branch
    git push origin 0.1.0
    ```
From this point on, you can use the automated `task cz:bump -- --no-dry-run` and `task release:push` workflow described above for all subsequent releases.

## Relevant Tasks Summary

*   `task cz:commit`: Interactively create a conventional commit message.
*   `task cz:bump`: (Dry run) Show what version bump would occur and what files would change.
*   `task cz:bump -- --no-dry-run`: Perform the actual version bump, update changelog, commit, and tag.
*   `task release:push`: Push the current branch and all tags to the remote repository.
*   `task cz:changelog`: (Optional) Manually regenerate or update the changelog. Usually not needed if `cz:bump` is used.
