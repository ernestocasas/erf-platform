import logging
import sys
from pythonjsonlogger import jsonlogger


def configure_json_logging(service_name: str, log_level: str = "INFO") -> None:
    """Configure JSON logging to stdout.

    This keeps logs ready for Docker / Kubernetes aggregation.
    """

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    # Remove default handlers
    for h in list(logger.handlers):
        logger.removeHandler(h)

    handler = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s %(service)s"
    formatter = jsonlogger.JsonFormatter(fmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Add service field via a filter
    class _ServiceFilter(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:
            setattr(record, "service", service_name)
            return True

    logger.addFilter(_ServiceFilter())
