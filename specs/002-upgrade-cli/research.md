# Research: Interactive CLI Error Handling

## Problem
Currently, when `argparse.ArgumentParser.parse_args()` encounters an error (e.g. unrecognized command or missing arguments), it automatically calls `sys.exit(2)`, which terminates the entire Python process. This breaks the interactive loop requirement.

## Decision
Create a custom subclass of `argparse.ArgumentParser` that overrides the `error(self, message)` and `exit(self, status=0, message=None)` methods so that instead of exiting, it prints the error and raises a custom exception (e.g., `ArgumentParseError`). The interactive loop can then catch this exception, print the usage, and prompt the user again.

## Rationale
Using the standard library `argparse` is simpler than introducing heavy dependencies like `cmd2` or `prompt_toolkit`. Overriding the exit behavior is a well-known Python pattern for using `argparse` in a REPL environment.

## Alternatives Considered
- **`cmd` module**: Standard library, but would require rewriting the entire command parsing logic from `argparse` to `cmd` structure.
- **`click` library**: Powerful, but requires adding a new dependency and rewriting the entire CLI tier. For minimal viable implementation, adapting `argparse` is simpler.
