# Using Different Container Registries

This project template provides a `Dockerfile` and a `task docker:build` command primarily configured for building an image for the FastAPI web application example found in `examples/web/`. This guide explains how to work with this setup and how to push your image to various container registries.

If you wish to containerize other applications from the `examples/` directory (like the CLI or data pipeline) or your own custom applications based on this template, you will need to:
1.  Adapt the existing `Dockerfile` or create a new one tailored to your application.
2.  Adjust the `task docker:build` command in `Taskfile.yml` or add new tasks if you create new Dockerfiles.

## Local Docker Build Configuration

The `Taskfile.yml` defines variables for local builds:
*   `IMAGE_NAME_LOCAL`: Defaults to `"your-app-image"`. This is the name used when building the image locally.
*   `TAG`: Defaults to `"latest"`. Note: the current `task docker:build` command builds the image as `your-app-image:latest` implicitly, as it doesn't explicitly use the `TAG` variable in the `docker build -t` command.

You can override `IMAGE_NAME_LOCAL` by setting it in a `.env` file at the project root (which `Taskfile.yml` can be configured to load) or by passing it as a command-line variable:
`task docker:build IMAGE_NAME_LOCAL=my-custom-local-image-name`

## Building the Local Image

To build your local image using the settings in `Taskfile.yml` (primarily for the `examples/web/` app):
```bash
task docker:build
```
This command executes `docker build -t {{.IMAGE_NAME_LOCAL | default "your-app-image"}} .`, resulting in an image like `your-app-image:latest`.

## Pushing to a Remote Container Registry

The `Taskfile.yml` does **not** include a pre-configured `task docker:push` for pushing to a remote registry. You will need to manually tag your locally built image and then use `docker push`.

### 1. Choose Your Image Name for the Registry

Select an image name and tag appropriate for your chosen registry. Examples:

*   **Docker Hub:** `YOUR_DOCKERHUB_USERNAME/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `mydockeruser/my-awesome-app:v1.0.0`
*   **GitHub Container Registry (GHCR):** `ghcr.io/YOUR_GITHUB_USERNAME/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `ghcr.io/mygithubuser/my-awesome-app:v1.0.0`
*   **Google Artifact Registry (GAR):** `LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `us-central1-docker.pkg.dev/my-gcp-project/my-app-repo/my-awesome-app:v1.0.0`
*   **Google Container Registry (GCR - Legacy):** `gcr.io/PROJECT-ID/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `gcr.io/my-gcp-project/my-awesome-app:v1.0.0`
*   **Amazon Elastic Container Registry (ECR):** `ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `123456789012.dkr.ecr.us-east-1.amazonaws.com/my-awesome-app:v1.0.0`
*   **Azure Container Registry (ACR):** `REGISTRY_NAME.azurecr.io/YOUR_PROJECT_SLUG:YOUR_TAG`
    *   Example: `myprojectacr.azurecr.io/my-awesome-app:v1.0.0`

### 2. Authenticate to Your Registry

Before you can push, authenticate your Docker client to your chosen registry. This is a one-time setup or may require periodic re-authentication.

Common authentication methods:

*   **Docker Hub:** `docker login`
*   **GHCR:** `docker login ghcr.io -u {{GITHUB_USERNAME}} -p YOUR_PERSONAL_ACCESS_TOKEN` (Replace `{{GITHUB_USERNAME}}` with your actual username)
*   **GAR/GCR:** `gcloud auth configure-docker LOCATION-docker.pkg.dev` (for GAR) or `gcloud auth configure-docker` (for GCR)
*   **ECR:** `aws ecr get-login-password --region YOUR_REGION | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com`
*   **ACR:** `az acr login --name YOUR_REGISTRY_NAME`

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
#   IMAGE_NAME_REMOTE: "ghcr.io/{{.GITHUB_USERNAME}}/{{.PROJECT_SLUG}}" # Example, needs GITHUB_USERNAME and PROJECT_SLUG defined
#   TAG_REMOTE: "latest"

# tasks:
#   docker:push:
#     desc: "Tags the local Docker image and pushes it to the remote registry."
#     env:
#       # Load GITHUB_USERNAME, PROJECT_SLUG from .env if defined there
#       # Ensure IMAGE_NAME_REMOTE and TAG_REMOTE are set, e.g., via .env or direct vars
#     cmds:
#       - docker tag {{.IMAGE_NAME_LOCAL | default "your-app-image"}}:{{.TAG | default "latest"}} {{.IMAGE_NAME_REMOTE}}:{{.TAG_REMOTE}}
#       - docker push {{.IMAGE_NAME_REMOTE}}:{{.TAG_REMOTE}}
#     silent: true
```
**Note:** The example above is a starting point. You'll need to ensure variables like `GITHUB_USERNAME` and `PROJECT_SLUG` are available to the task (e.g., from `.env` or defined directly in `vars`). The local tag used (`{{.TAG | default "latest"}}`) should match how `task docker:build` actually tags the image.
