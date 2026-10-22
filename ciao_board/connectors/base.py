from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Sequence


class BaseConnector(ABC):
    """Abstract base class for board integrations."""

    name = "base"

    def __init__(self, **kwargs: Any):
        self.config = kwargs

    @abstractmethod
    def generate(self, prompt: str, **kwargs: Any) -> str:
        """Generate a response for a prompt."""

    def chat(self, messages: Sequence[Dict[str, str]], **kwargs: Any) -> str:
        """Convert a list of role/content chat messages into text prompt."""
        prompt = "\n".join(
            f"{message.get('role', 'user').title()}: {message.get('content', '')}"
            for message in messages
        )
        return self.generate(prompt, **kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
