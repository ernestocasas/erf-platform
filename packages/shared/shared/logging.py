from __future__ import annotations

import logging
from pythonjsonlogger import jsonlogger


def configure_logging(service_name: str, level: str = "INFO") -> None:
    """Configure JSON logging suitable for cloud and container environments."""
    root = logging.getLogger()
    root.setLevel(level)

    # Clear existing handlers (safe for local dev)
    for h in list(root.handlers):
        root.removeHandler(h)

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(service)s"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)

    logging.getLogger(__name__).info("logging_configured", extra={"service": service_name})
