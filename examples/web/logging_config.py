import logging
import sys


def init_logging(log_level: str):
    """Initializes basic logging configuration."""
    # Determine the logging level
    level = getattr(logging, log_level.upper(), logging.INFO)

    # Basic configuration
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        handlers=[
            logging.StreamHandler(
                sys.stdout
            )  # Ensure logs go to stdout for container visibility
        ],
        force=True,
    )

    # You can add more handlers here, e.g., for file logging or structured logging
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized with level: {log_level.upper()}")
