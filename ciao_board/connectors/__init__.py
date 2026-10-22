"""Connector abstractions for Ciao Board."""

from .base import BaseConnector
from .claude import ClaudeConnector


def get_connector(name: str, **kwargs):
    """Return a named connector implementation."""
    if name.lower() == "claude":
        return ClaudeConnector(**kwargs)
    raise ValueError(f"Unsupported connector: {name}")


__all__ = ["BaseConnector", "ClaudeConnector", "get_connector"]
