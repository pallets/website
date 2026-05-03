import sys
from typing import Any


class ConfigError(Exception):
    """A custom exception for user-facing configuration errors."""

    pass


def validate_config(config: dict[str, Any]) -> dict[str, Any]:
    """
    Validates a configuration dictionary, raising ConfigError with actionable
    advice if any checks fail.
    """
    _check_for_required_keys(config)
    _check_api_key(config)
    _check_timeout(config)
    _check_mode(config)

    return config


def _check_for_required_keys(config: dict[str, Any]):
    """Ensure all mandatory keys are present."""
    required_keys = ["api_key", "timeout", "mode"]
    missing_keys = [key for key in required_keys if key not in config]

    if missing_keys:
        key_str = ", ".join(f"'{key}'" for key in missing_keys)
        raise ConfigError(
            f"Configuration error: Missing required key(s): {key_str}.\n"
            f"  > Please add the missing key(s) to your configuration file."
        )


def _check_api_key(config: dict[str, Any]):
    """Validate the 'api_key' is a non-empty string."""
    api_key = config.get("api_key")
    if not isinstance(api_key, str) or not api_key:
        # A common mistake is an empty string or forgetting quotes in YAML.
        # This message helps diagnose both.
        raise ConfigError(
            "Configuration error: The 'api_key' must be a non-empty string.\n"
            f"  > We found a value of type '{type(api_key).__name__}'.\n"
            '  > Please ensure your config looks like: api_key: "your_secret_key"'
        )


def _check_timeout(config: dict[str, Any]):
    """Validate the 'timeout' is a positive integer."""
    timeout = config.get("timeout")
    if not isinstance(timeout, int) or timeout <= 0:
        # Guide the user on the expected type and a valid range.
        raise ConfigError(
            "Configuration error: The 'timeout' must be a positive integer.\n"
            f"  > We found '{timeout}', which is a '{type(timeout).__name__}'.\n"
            "  > Please use a whole number greater than zero, like: timeout: 30"
        )


def _check_mode(config: dict[str, Any]):
    """Validate the 'mode' is one of the allowed values."""
    mode = config.get("mode")
    valid_modes = ["fast", "balanced", "high_quality"]
    if mode not in valid_modes:
        # Show the user the exact value they provided and list the valid options.
        # This prevents typos and guesswork.
        raise ConfigError(
            f"Configuration error: Invalid value for 'mode'.\n"
            f"  > We received '{mode}', but the only allowed values are: {valid_modes}.\n"
            f"  > Please update 'mode' in your configuration file."
        )


def run_with_config(config_name: str, config_data: dict[str, Any]):
    """A helper to simulate running the app with a given configuration."""
    print(f"--- Attempting to load '{config_name}' ---")
    try:
        validate_config(config_data)
        print("✅ Configuration is valid and loaded successfully.\n")
    except ConfigError as e:
        # This is where the user sees our improved, actionable error message.
        # Printing to stderr is standard practice for errors.
        print(f"❌ {e}\n", file=sys.stderr)


def main():
    """
    Demonstrates configuration validation with user-friendly error messages
    by running through several common invalid configuration scenarios.
    """
    # A valid configuration to show the success case.
    valid_config = {"api_key": "sk-12345abcde", "timeout": 30, "mode": "balanced"}

    # --- Example Error Cases ---

    # 1. Missing a required key ('api_key')
    config_missing_key = {"timeout": 60, "mode": "fast"}

    # 2. Incorrect data type for 'timeout' (string instead of int)
    config_wrong_type = {
        "api_key": "sk-12345abcde",
        "timeout": "30",  # Should be an integer
        "mode": "fast",
    }

    # 3. Invalid value for 'mode'
    config_invalid_value = {
        "api_key": "sk-12345abcde",
        "timeout": 15,
        "mode": "quick",  # Not a valid mode
    }

    # 4. Empty string for 'api_key'
    config_empty_key = {"api_key": "", "timeout": 15, "mode": "high_quality"}

    run_with_config("Valid Config", valid_config)
    run_with_config("Config Missing Key", config_missing_key)
    run_with_config("Config Wrong Type", config_wrong_type)
    run_with_config("Config Invalid Value", config_invalid_value)
    run_with_config("Config Empty Key", config_empty_key)


if __name__ == "__main__":
    main()
