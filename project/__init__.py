"""Top-level package for the example `project` package.

This package provides a tiny in-memory customer model and an application
module to demonstrate usage. It's intentionally small and dependency-free
so it's easy to test and extend.
"""

__all__ = ["app", "models"]

__version__ = "0.1.0"

from . import app  # noqa: F401
from . import models  # noqa: F401
