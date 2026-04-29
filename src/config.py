import sys
import tomllib
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass


class Settings(BaseModel):
    """
    Defines the application's configuration structure using Pydantic.
    This ensures that all configuration values are of the correct type.
    """
    api_key: str = Field(..., description="The API key for the primary service.")
    timeout: int = Field(
        default=30, gt=0, description="Default timeout for API requests in seconds."
    )
    log_level: str = Field(
        default="INFO",
        pattern=r"^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$",
        description="Logging level (e.g., DEBUG, INFO, WARNING).",
    )
    database_url: Optional[str] = Field(
        default=None, description="Optional database connection URL."
    )


def load_config(config_path: Path = Path("config.toml")) -> Settings:
    """
    Loads and validates configuration from a TOML file.

    This function is designed to provide clear, actionable error messages
    to help users fix configuration issues quickly.

    Args:
        config_path: The path to the configuration file.

    Returns:
        A validated Settings object.

    Raises:
        ConfigError: If the file is not found, cannot be parsed, or fails validation.
    """
    # Pain Point 1: The configuration file doesn't exist.
    # The error should be explicit about what's missing and where we looked.
    if not config_path.is_file():
        raise ConfigError(
            f"Configuration file not found at '{config_path}'.\n"
            "Hint: Make sure the file exists. You might need to create one from an "
            "example template like 'config.example.toml'."
        )

    # Pain Point 2: The file exists but is malformed (e.g., invalid TOML).
    # We'll catch the specific parsing error and provide context.
    try:
        with open(config_path, "rb") as f:
            config_data = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        raise ConfigError(
            f"Error parsing '{config_path}':\n"
            f"  {e}\n"
            "Hint: Check the file for syntax errors like missing quotes, "
            "incorrect formatting, or invalid characters."
        )
    except OSError as e:
        # Also handle cases where the file can't be read due to permissions.
        raise ConfigError(f"Could not read configuration file '{config_path}': {e}")

    # Pain Points 3 & 4: Missing required keys or values of the wrong type.
    # Pydantic handles this validation, but we can format its error for clarity.
    try:
        return Settings(**config_data)
    except ValidationError as e:
        # Pydantic's default error is good, but we can make it more user-friendly
        # by formatting it as a clear, readable list.
        error_messages = []
        for error in e.errors():
            field = " -> ".join(map(str, error["loc"]))
            message = error["msg"]
            error_messages.append(f"  - Field '{field}': {message}")

        formatted_errors = "\n".join(error_messages)
        raise ConfigError(
            f"Configuration in '{config_path}' is invalid:\n"
            f"{formatted_errors}\n"
            "Hint: Please check the values in your configuration file and ensure they "
            "match the expected types and requirements."
        )