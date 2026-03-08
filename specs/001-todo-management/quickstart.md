# Quickstart: Phase I — CLI Todo App

This document provides instructions on how to run Phase I of the "Evolution of Todo" project.
The Phase I deliverable is a pure in-memory Python Console Todo App.

## Prerequisites
- Python 3.11+
- `uv` or `pip`

## Setup Instructions

1. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

## Running the Application

### 1. Interactive Mode
If no commands are provided, the application will enter an interactive shell that persists data within that session.

```bash
python -m src.cli.main
```

Usage inside interactive mode:
```text
todo> help
todo> create "Buy milk" --notes "Get 2%"
todo> list
todo> complete <task_id>
todo> list --status completed
todo> get <task_id>
todo> update <task_id> --title "Buy soy milk"
todo> delete <task_id>
todo> exit
```

### 2. Single-Command Execution
You can pass arguments directly. *Note: Data is not persisted across multiple single-command invocations because Phase I strictly uses an in-memory datastore.*

```bash
python -m src.cli.main create "Review PRs"
python -m src.cli.main list
```

## Running Tests
To verify the core engine and CLI behavior, run:
```bash
PYTHONPATH=. pytest tests/
```
