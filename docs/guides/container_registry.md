# Using Different Container Registries

This project template includes a `Dockerfile` and a `task docker:build` command, primarily configured for building an image of the FastAPI web application example (`examples/web/`). This guide explains how to use this setup and push your built image to various container registries.

To containerize other applications from the `examples/` directory (such as the CLI or data pipeline) or your custom applications based on this template, you will typically need to:
1.  Adapt the existing `Dockerfile` or create a new one tailored to your application.
2.  Adjust the `task docker:build` command in `Taskfile.yml` or add new tasks if you create new Dockerfiles.

## Local Docker Build Configuration

The `Taskfile.yml` defines variables for local builds:
*   `IMAGE_NAME_LOCAL`: Defaults to `"your-app-image"`. This is the name used for the image built locally.
*   `TAG`: Defaults to `"latest"`. This is the tag used for the image built locally.

Both `IMAGE_NAME_LOCAL` and `TAG` are used by the `task docker:build` command (e.g., `docker build -t {{.IMAGE_NAME_LOCAL}}:{{.TAG}} ...`). You can override these by setting them in a `.env` file at the project root or by passing them as command-line variables:
`task docker:build IMAGE_NAME_LOCAL=my-custom-image TAG=v1.0.0`

## Building the Local Image

To build your local image using the settings in `Taskfile.yml` (primarily for the `examples/web/` app):
```bash
task docker:build
```
This command, by default, executes `docker build -t your-app-image:latest . ...`, resulting in an image named `your-app-image` with the tag `latest`.

## Pushing to a Remote Container Registry

The `Taskfile.yml` does **not** include a pre-configured `task docker:push` for pushing to a remote registry. You will need to manually tag your locally built image and then use `docker push`.

### 1. Choose Your Image Name for the Registry

Select an image name and tag appropriate for your chosen registry. Examples:

*   **Docker Hub:** `YOUR_DOCKERHUB_USERNAME/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `mydockeruser/my-awesome-app:v1.0.0`
*   **GitHub Container Registry (GHCR):** `ghcr.io/YOUR_GITHUB_USERNAME/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `ghcr.io/mygithubuser/my-awesome-app:v1.0.0`
*   **Google Artifact Registry (GAR):** `LOCATION-docker.pkg.dev/YOUR_GCP_PROJECT_ID/YOUR_REPOSITORY_NAME/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `us-central1-docker.pkg.dev/my-gcp-project/my-app-repo/my-awesome-app:v1.0.0`
*   **Google Container Registry (GCR - Legacy):** `gcr.io/YOUR_GCP_PROJECT_ID/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `gcr.io/my-gcp-project/my-awesome-app:v1.0.0`
*   **Amazon Elastic Container Registry (ECR):** `YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_AWS_REGION.amazonaws.com/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `123456789012.dkr.ecr.us-east-1.amazonaws.com/my-awesome-app:v1.0.0`
*   **Azure Container Registry (ACR):** `YOUR_ACR_REGISTRY_NAME.azurecr.io/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `myprojectacr.azurecr.io/my-awesome-app:v1.0.0`

### 2. Authenticate to Your Registry

Before you can push, authenticate your Docker client to your chosen registry. This is a one-time setup or may require periodic re-authentication.

Common authentication methods:

*   **Docker Hub:** `docker login`
*   **GHCR:** `docker login ghcr.io -u YOUR_GITHUB_USERNAME -p YOUR_PERSONAL_ACCESS_TOKEN` (Replace `YOUR_GITHUB_USERNAME` with your actual username and use a PAT with `write:packages` scope)
*   **GAR/GCR:** `gcloud auth configure-docker YOUR_LOCATION-docker.pkg.dev` (for GAR, e.g., `us-central1-docker.pkg.dev`) or `gcloud auth configure-docker` (for GCR, which configures for registries like `gcr.io`, `us.gcr.io`, etc.)
*   **ECR:** `aws ecr get-login-password --region YOUR_AWS_REGION | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_AWS_REGION.amazonaws.com`
*   **ACR:** `az acr login --name YOUR_ACR_REGISTRY_NAME`

Refer to your specific registry's documentation for the most up-to-date instructions.

### 3. Tag and Push the Image

After building the local image (e.g., `your-app-image:latest` via `task docker:build`):

1.  **Tag the local image** with your full remote repository name and desired tag:
    ```bash
    # Replace with your actual local image name if different, and your remote name/tag
    docker tag your-app-image:latest ghcr.io/mygithubuser/my-awesome-app:v1.0.0
    ```

2.  **Push the tagged image:**
    ```bash
    docker push ghcr.io/mygithubuser/my-awesome-app:v1.0.0
    ```

### Optional: Automating Push with Taskfile.yml

If you frequently push images, consider adding a custom `docker:push` task to your `Taskfile.yml`. You could define variables like `IMAGE_NAME_REMOTE` and `TAG_REMOTE` (potentially loaded from an `.env` file) for this task.

Example of a custom task (add to `Taskfile.yml`):
```yaml
# In Taskfile.yml
# vars:
#   IMAGE_NAME_REMOTE: "ghcr.io/{{.GITHUB_USERNAME}}/{{.PROJECT_SLUG}}" # Example, needs GITHUB_USERNAME and PROJECT_SLUG defined, e.g. in .env
#   TAG_REMOTE: "latest" # Or perhaps a more specific version tag

# tasks:
#   docker:push:
#     desc: "Tags the locally built Docker image and pushes it to the remote registry."
#     requires:
#       vars: [IMAGE_NAME_REMOTE, TAG_REMOTE] # Ensure these are set
#     env:
#       # Load GITHUB_USERNAME, PROJECT_SLUG from .env if defined there for IMAGE_NAME_REMOTE
#       # Ensure IMAGE_NAME_LOCAL and TAG (for the source image) are consistent with your build
#       LOCAL_IMAGE_FULL: "{{.IMAGE_NAME_LOCAL | default "your-app-image"}}:{{.TAG | default "latest"}}"
#       REMOTE_IMAGE_FULL: "{{.IMAGE_NAME_REMOTE}}:{{.TAG_REMOTE}}"
#     cmds:
#       - echo "Tagging {{.LOCAL_IMAGE_FULL}} as {{.REMOTE_IMAGE_FULL}}"
#       - docker tag {{.LOCAL_IMAGE_FULL}} {{.REMOTE_IMAGE_FULL}}
#       - echo "Pushing {{.REMOTE_IMAGE_FULL}}"
#       - docker push {{.REMOTE_IMAGE_FULL}}
#     silent: true
```
# **Note:** The example above is a starting point.
# - You'll need to ensure variables like `GITHUB_USERNAME` and `PROJECT_SLUG` (if used in `IMAGE_NAME_REMOTE`) are available to the task (e.g., loaded from `.env` or defined directly in `vars`).
# - The source image `{{.IMAGE_NAME_LOCAL | default "your-app-image"}}:{{.TAG | default "latest"}}` must match the image built by `task docker:build`.
# - You might want to add a `task docker:build` as a dependency to this push task.
