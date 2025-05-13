# Security Best Practices & Secret Management

Properly managing application configuration and secrets is critical, especially when moving from local development to staging, production, or any shared cloud development environment.

This guide outlines best practices and how this project template facilitates them.

## The Role of `.env` Files

In this project template, `.env` files (generated from `.env.example`) serve a specific purpose:

- **Local Development Convenience:** They allow developers to easily set environment variables for their local Docker Compose setup (`docker-compose.yml` uses `env_file`) or for direct local execution if the application is configured to load them (e.g., via Pydantic's `Settings` if `python-dotenv` is used).
- **Simulation:** They help simulate an environment where configuration is passed via environment variables, which is the standard for most deployed applications.

**IMPORTANT:** `.env` files containing actual secrets or environment-specific configurations **MUST NOT** be committed to version control. Ensure `.env` is listed in your `.gitignore` file (it is by default in this template).

## Why `.env` Files Are Not for Production/Staging

Directly using `.env` files in production or staging environments is generally discouraged due to several risks:

- **Security Risks:**
    - **Accidental Exposure:** If deployed with application code, they could be inadvertently exposed through web server misconfigurations or if the application code itself is compromised.
    - **Version Control Mistakes:** Even with `.gitignore`, there's always a risk of accidental commits if not handled carefully across a team.
- **Operational Overhead:** Managing different `.env` files for various environments and ensuring they are securely distributed to servers is cumbersome and error-prone.
- **Lack of Auditability & Control:** `.env` files don't offer features like access control, versioning of secrets, or audit trails that dedicated secret management systems provide.

## Recommended Practices for Deployed Environments

### 1. True Environment Variables (12-Factor App Principles)

Store configuration directly in the environment where the application runs.

- **How:** Set environment variables on your host machine, CI/CD system, PaaS (Platform as a Service), CaaS (Containers as a Service like Kubernetes), or FaaS (Functions as a Service like AWS Lambda).
- **Pros:** Language-agnostic, clear separation of config from code, widely supported.
- **Template Support:**
    - The FastAPI application's settings (via `app/config.py` using Pydantic's `BaseSettings`) are designed to automatically load values from environment variables.
    - `docker-compose.yml` also respects environment variables set in its execution environment, which can override or supplement values from the `env_file`.
    - The `Dockerfile` uses `ENV` for build-time and runtime environment variables that don't change often.

### 2. Secret Management Systems

For sensitive data like API keys, database credentials, and encryption keys, use a dedicated secret management system.

- **Examples:**
    - [HashiCorp Vault](https://www.vaultproject.io/)
    - [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
    - [Google Secret Manager](https://cloud.google.com/secret-manager)
    - [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
    - [Doppler](https://doppler.com/)
- **How:** These systems securely store secrets. Your application fetches them at startup or runtime via their SDKs or APIs. Some integrate directly with container orchestrators or CI/CD systems.
- **Pros:** Enhanced security (encryption, access control, audit logs), secret versioning and rotation capabilities.

### 3. Platform-Specific Configuration & Secrets

Leverage the native configuration and secret management features of your deployment platform.

- **Examples:**
    - **Kubernetes:** `ConfigMaps` (for non-sensitive config) and `Secrets` (for sensitive data).
    - **Heroku:** Config Vars.
    - **AWS ECS/EKS/Lambda:** Environment variables, integration with AWS Secrets Manager or Parameter Store.
    - **Google Cloud Run/GKE:** Environment variables, integration with Google Secret Manager.
    - **Azure App Service/AKS:** Application settings, integration with Azure Key Vault.

## How This Template Supports Secure Configuration

- **Pydantic Settings (e.g., as shown in `examples/web/app/config.py`):** The pattern of using Pydantic's `BaseSettings` (demonstrated in the FastAPI example's `config.py`) allows your application to automatically load configuration values from environment variables first. This makes it seamless to transition from local `.env` (if used for populating local env vars) to production environment variables. This is a recommended pattern for any Python application needing robust settings management.
    ```python
    # Example (similar to examples/web/app/config.py)
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        APP_NAME: str = "My FastAPI App"
        API_KEY: str # This will be read from an environment variable
        # Add other configurations here

        class Config:
            # If you had a .env file and python-dotenv installed,
            # Pydantic could load it too for local dev, but environment
            # variables take precedence.
            # env_file = ".env"
            # extra = "ignore"
            pass

    settings = Settings()
    ```
- **`.gitignore`:** Includes `.env` to prevent accidental commits.
- **`Dockerfile`:** Avoids copying `.env` files into the image.

By adhering to these practices, you can ensure that your application's configuration and secrets are managed securely and efficiently across all environments.
