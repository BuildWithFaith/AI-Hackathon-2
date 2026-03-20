import argparse
import sys


class ArgumentParseError(Exception):
    pass


class SafeArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParseError(message)

    def exit(self, status=0, message=None):
        if status != 0:
            raise ArgumentParseError(message or "Exit called")


def process_command(engine, args):
    if args.command == "create":
        try:
            task = engine.create_task(args.title, args.notes)
            print(f"Task created: [{task.id}] {task.title}")
        except Exception as e:
            print(f"Error: {e}")
    elif args.command == "list":
        tasks = engine.list_tasks(getattr(args, "status", None))
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            print(f"{status} {task.id} - {task.title}")
    elif args.command == "complete":
        try:
            task = engine.complete_task(args.id)
            print(f"Task {task.id} marked as complete.")
        except Exception as e:
            print(f"Error: {e}")
    elif args.command == "delete":
        try:
            engine.delete_task(args.id)
            print(f"Task {args.id} deleted.")
        except Exception as e:
            print(f"Error: {e}")
    elif args.command == "get":
        task = engine.get_task(args.id)
        if task:
            print(
                f"ID: {task.id}\nTitle: {task.title}\nStatus: {'Completed' if task.completed else 'Pending'}"
            )
            if task.notes:
                print(f"Notes: {task.notes}")
        else:
            print(f"Error: Task with id {args.id} not found")
    elif args.command == "update":
        try:
            task = engine.update_task(args.id, title=args.title, notes=args.notes)
            print(f"Task {task.id} updated.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Command '{args.command}' not implemented yet.")


def main():
    parser = SafeArgumentParser(description="Core Todo Management System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new task")
    create_parser.add_argument("title", help="Task title")
    create_parser.add_argument("--notes", help="Task notes", default=None)

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="List all tasks")
    list_parser.add_argument(
        "--status", choices=["pending", "completed", "all"], default="pending"
    )

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", help="Task ID to complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", help="Task ID to delete")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get task details")
    get_parser.add_argument("id", help="Task ID to get")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update task details")
    update_parser.add_argument("id", help="Task ID to update")
    update_parser.add_argument("--title", help="New title for the task (optional)")
    update_parser.add_argument("--notes", help="New notes for the task (optional)")

    args = None
    try:
        args = parser.parse_args()
    except ArgumentParseError as e:
        if len(sys.argv) > 1:
            print(f"Error: {e}")
            parser.print_help()
            sys.exit(2)

    from src.core.engine import InMemoryTodoEngine

    engine = InMemoryTodoEngine()

    if len(sys.argv) == 1:
        print("Starting interactive mode. Type 'help' for commands, 'exit' to quit.")

        pending_tasks = engine.list_tasks("pending")
        if pending_tasks:
            print(f"\n--- {len(pending_tasks)} pending tasks ---")
            for task in pending_tasks:
                print(f"[ ] {task.id} - {task.title}")
            print("------------------------\n")
        else:
            print("\nNo pending tasks. You're all caught up!\n")

        import shlex

        while True:
            try:
                cmd_line = input("todo> ").strip()
                if cmd_line in ("exit", "quit"):
                    break
                if not cmd_line:
                    continue
                cmd_args = parser.parse_args(shlex.split(cmd_line))
                if getattr(cmd_args, "command", None):
                    process_command(engine, cmd_args)
                else:
                    parser.print_help()
            except ArgumentParseError as e:
                print(f"Error parsing command: {e}")
                parser.print_help()
            except EOFError:
                print("\nExiting...")
                break
            except KeyboardInterrupt:
                print("\nUse 'exit' or 'quit' to exit, or Ctrl+D.")
                continue
            except Exception as e:
                print(f"Unexpected error: {e}")
    else:
        if args and args.command:
            process_command(engine, args)


if __name__ == "__main__":
    main()
