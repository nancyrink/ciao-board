# ciao-board

A lightweight repository for Ciao Board with a Claude connector integration.

## Claude connector

This project includes a simple Anthropic Claude integration that can be used as a connector abstraction for board features and AI workflows.

### Install

```bash
pip install -r requirements.txt
```

### Configure

Copy `.env.example` to `.env` and provide your API key.

```bash
cp .env.example .env
```

### Usage

```python
from ciao_board.connectors import ClaudeConnector

connector = ClaudeConnector()
response = connector.generate("Summarize the latest project status.")
print(response)
```

### Environment variables

- `ANTHROPIC_API_KEY`: your Claude API key
- `CLAUDE_MODEL`: optional model override

The connector uses `claude-3-5-sonnet-latest` by default.
