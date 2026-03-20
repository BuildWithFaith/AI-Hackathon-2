class TodoError(Exception):
    """Base exception for all Todo errors."""

    pass


class NotFoundError(TodoError):
    """Raised when a task is not found."""

    pass


class ValidationError(TodoError):
    """Raised when task data is invalid."""

    pass
