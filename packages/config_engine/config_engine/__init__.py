"""Configuration engine (scaffold).

Responsible for loading JSON/YAML configuration, validating schemas, and providing
runtime configuration to ERF services.
"""

from .loader import load_config

__all__ = ["load_config"]
