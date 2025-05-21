# Development Troubleshooting Guide

This guide collects common issues, specific error resolutions, and development best practices encountered while working with this project template.

## Dockerfile Best Practices & Troubleshooting

### `uv pip install` vs. `pip install --target` for Runtime Dependencies

When building Docker images, especially for Python applications, you might encounter different behaviors between `uv pip install` and the standard `pip install`, particularly when installing packages into a specific target directory.

**Issue Encountered:**
Using `uv pip install --target <directory> .` (e.g., `uv pip install --no-cache --target /opt/runtime_deps .`) to install project runtime dependencies into a specific folder inside a Docker image can lead to errors. As of `uv` version `0.1.20`, `uv pip install` does not fully support the `--target` option in the same way `pip` does. You might see errors like:
```
error: Failed to parse `--target`
  Caused by: Expected package name starting with an alphanumeric character, found '-'
--target
^
```
Even using `-- --target` to separate arguments might not resolve this, as the underlying installation mechanism in `uv` may not recognize the option.

**Solution:**
For installing packages into a specific target directory within a Dockerfile, it's more reliable to use the standard `pip install` command, which has well-established support for `--target`.

**Example `Dockerfile` snippet:**

```dockerfile
# In your builder stage, after building your project wheel:

# Create a clean installation directory for runtime dependencies.
ENV RUNTIME_DEPS_DIR=/opt/runtime_deps
RUN mkdir -p $RUNTIME_DEPS_DIR

# Install ONLY production/runtime dependencies into the target directory.
# Use pip for --target functionality.
RUN pip install --no-cache-dir --target $RUNTIME_DEPS_DIR .

# ... then in your runtime stage, copy from $RUNTIME_DEPS_DIR
# COPY --from=builder $RUNTIME_DEPS_DIR /opt/app_deps
# ENV PYTHONPATH=/opt/app_deps:$PYTHONPATH
```

This ensures that runtime dependencies are correctly isolated into the specified directory. While `uv` is excellent for many package management tasks (like installing build tools or managing virtual environments locally), `pip` remains a robust choice for this specific Docker layering pattern.

## Taskfile (Go-Task) Best Practices & Troubleshooting

### Ensuring Correct Parsing of Internal Task Calls

Go-Task's `Taskfile.yml` parser can sometimes be sensitive to minor syntax variations in how internal tasks are called (i.e., when one task executes another task defined in the same `Taskfile.yml`).

**Issue Encountered:**
You might encounter "executable file not found in $PATH" errors when a task tries to call another task, for example:
```yaml
# Potentially problematic
parent_task:
  cmds:
    - task:child_task_name # Missing space after colon
```
This can happen even if `child_task_name` is correctly defined.

**Solution:**
Consistently use a space after the colon when calling an internal task. This syntax has proven to be more robust for Go-Task's parser.

**Example:**
```yaml
# Corrected and more robust
parent_task:
  desc: "This task calls another task."
  cmds:
    - task: child_task_name # Note the space after 'task:'
  silent: true

child_task_name:
  desc: "This is the child task."
  cmds:
    - echo "Child task executed!"
  silent: true
```
This small adjustment can prevent frustrating parsing issues and ensure your tasks run reliably. Remember this also applies to task dependencies specified with `deps: [task: name]`.
