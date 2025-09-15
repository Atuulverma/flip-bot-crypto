# app/observability/logging.py
import json
import logging
from typing import Any


def json_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def log_event(logger: logging.Logger, **kwargs: Any) -> None:
    # Accept any JSON-serializable payload; emit as a single line
    logger.info(json.dumps(kwargs))
