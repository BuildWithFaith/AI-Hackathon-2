# Quickstart: Interactive CLI Upgrades

## Running the Application

1. **Activate Virtual Environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Start Interactive Mode:**
   ```bash
   python -m src.cli.main
   ```
   
   *New Behavior:*
   - Pending tasks are displayed automatically immediately upon startup.
   - If you make a typo or forget an argument, the CLI will display an error instead of exiting.
   - Use `Ctrl+C` or `exit` to close the application safely.

## Running Tests

To verify the robust interactive loop and commands:
```bash
PYTHONPATH=. pytest tests/
```
