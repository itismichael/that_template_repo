from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "My Awesome App built with 'your_core_library'"
    APP_VERSION: str = (
        "0.1.0"  # Could also be derived from your_core_library.__version__
    )
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # FastAPI server settings (if running directly, Docker CMD overrides these for container)
    APP_HOST: str = "0.0.0.0"  # nosec B104 # Allows binding to all interfaces, common for Docker
    APP_PORT: int = 8000

    # Example of a more specific setting
    # CORE_LIBRARY_API_KEY: str = None

    # To load from a .env file, Pydantic-Settings does this automatically.
    # You can specify the .env file path if it's not in the default location.
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Create a single instance of the settings to be used throughout the application
settings = Settings()
