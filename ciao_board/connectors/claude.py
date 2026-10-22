from __future__ import annotations

import os
from typing import Any, Dict, Optional, Sequence

try:
    import anthropic
except ImportError:  # pragma: no cover - optional dependency
    anthropic = None

from .base import BaseConnector


class ClaudeConnector(BaseConnector):
    """Anthropic Claude connector implementation."""

    name = "claude"

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model or os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-latest")
        self.client = None
        if anthropic is not None and self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)

    def _ensure_client(self):
        if anthropic is None:
            raise RuntimeError(
                "The 'anthropic' package is required. Run: pip install -r requirements.txt"
            )
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY is not set. Provide api_key or set the environment variable.")
        if self.client is None:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        return self.client

    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 1024,
        **kwargs: Any,
    ) -> str:
        """Generate a response using Claude."""
        client = self._ensure_client()

        payload: Dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            payload["system"] = system

        response = client.messages.create(**payload)
        return "".join(
            block.text
            for block in getattr(response, "content", [])
            if getattr(block, "type", None) == "text"
        )

    def chat(
        self,
        messages: Sequence[Dict[str, str]],
        system: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 1024,
        **kwargs: Any,
    ) -> str:
        """Send a full message list to Claude."""
        client = self._ensure_client()

        payload: Dict[str, Any] = {
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": list(messages),
        }
        if system:
            payload["system"] = system

        response = client.messages.create(**payload)
        return "".join(
            block.text
            for block in getattr(response, "content", [])
            if getattr(block, "type", None) == "text"
        )
