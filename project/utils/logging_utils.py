"""Logging utility helpers for the `project` package.

Provide a small `get_logger` convenience function that configures a
logger with a stream handler (and optional file handler) and a sensible
formatter. The function is idempotent: calling it multiple times for the
same `name` will reuse existing handlers.
"""
from __future__ import annotations

import logging
from typing import Optional

_DEFAULT_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def get_logger(name: Optional[str] = None, level: int = logging.INFO, fmt: str | None = None, log_file: Optional[str] = None) -> logging.Logger:
    """Return a configured `logging.Logger`.

    - `name`: logger name (None -> root logger)
    - `level`: numeric logging level
    - `fmt`: optional format string (defaults to a timestamped format)
    - `log_file`: optional path to write file logs

    The function avoids adding duplicate handlers if called repeatedly.
    """
    fmt = fmt or _DEFAULT_FORMAT
    logger = logging.getLogger(name)

    # If logger already has handlers, just update level and return.
    if logger.handlers:
        logger.setLevel(level)
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter(fmt)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Prevent messages from being propagated to the root logger twice
    logger.propagate = False
    return logger
