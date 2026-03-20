# Phase 1: Core Todo Management System CLI

This is the first phase of the Hackathon 2 project: a Core Todo Management System CLI written in Python. It features a custom `InMemoryTodoEngine` and uses Python's standard `argparse` library.

## Features

- **Store Tasks In-Memory**: Uses a lightweight dictionary-based memory store. 
- **Interactive Mode**: Launch the CLI without arguments to enter a persistent, interactive session.
- **Full CRUD Support**: Create, Read, Update, and Delete your tasks.
- **Task Statuses**: Easily mark tasks as pending or completed.

## Requirements

- Python 3.11+

## Project Structure

```text
phase1/
├── src/           # Application source code
│   ├── cli/       # Command-line interface logic
│   └── core/      # Core logic (Engine, Models, Exceptions)
├── tests/         # Unit and Integration tests
└── CLAUDE.md      # Development guidelines and notes
```

## Usage

You can run the application directly by executing the `main.py` file:

```bash
python -m src.cli.main [COMMAND] [OPTIONS]
```

### Interactive Mode

Run without any commands to start an interactive shell:

```bash
python -m src.cli.main
```
This mode lets you continuously enter commands like `create`, `list`, `complete`, etc., without restarting the script. Type `exit` or `quit` to leave.

### Available Commands

- **Create a task:**
  ```bash
  python -m src.cli.main create "Buy Groceries" --notes "Milk, Eggs, Bread"
  ```
- **List tasks:**
  ```bash
  python -m src.cli.main list
  python -m src.cli.main list --all
  python -m src.cli.main list --status completed
  ```
- **Mark a task as complete:**
  ```bash
  python -m src.cli.main complete <task_id>
  ```
- **Get task details:**
  ```bash
  python -m src.cli.main get <task_id>
  ```
- **Update a task:**
  ```bash
  python -m src.cli.main update <task_id> --title "New Title" --notes "New Notes"
  ```
- **Delete a task:**
  ```bash
  python -m src.cli.main delete <task_id>
  ```

## Development

Run tests using `pytest`:

```bash
pytest
```

Run linter checks using `ruff`:

```bash
ruff check .
```
