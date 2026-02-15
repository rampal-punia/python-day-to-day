"""
CLI Todo List Manager — with File Persistence
================================================
A practical beginner project demonstrating file I/O, 
JSON handling, and clean CLI design.

Author: @rampal-punia
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional


TODO_FILE = Path(__file__).parent / "todo_data.json"


class TodoManager:
    """Manages a persistent todo list stored as JSON."""

    def __init__(self, filepath: Path = TODO_FILE):
        self.filepath = filepath
        self.todos: list[dict] = self._load()

    def _load(self) -> list[dict]:
        """Load todos from JSON file."""
        if self.filepath.exists():
            with open(self.filepath, "r") as f:
                return json.load(f)
        return []

    def _save(self) -> None:
        """Save todos to JSON file."""
        with open(self.filepath, "w") as f:
            json.dump(self.todos, f, indent=2, default=str)

    def _next_id(self) -> int:
        return max((t["id"] for t in self.todos), default=0) + 1

    def add(self, title: str, priority: str = "medium") -> dict:
        """Add a new todo item."""
        todo = {
            "id": self._next_id(),
            "title": title,
            "priority": priority,  # low, medium, high
            "done": False,
            "created": datetime.now().isoformat(),
            "completed_at": None,
        }
        self.todos.append(todo)
        self._save()
        return todo

    def complete(self, todo_id: int) -> Optional[dict]:
        """Mark a todo as completed."""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                todo["completed_at"] = datetime.now().isoformat()
                self._save()
                return todo
        return None

    def delete(self, todo_id: int) -> bool:
        """Delete a todo by ID."""
        original_len = len(self.todos)
        self.todos = [t for t in self.todos if t["id"] != todo_id]
        if len(self.todos) < original_len:
            self._save()
            return True
        return False

    def list_all(self, show_done: bool = True) -> list[dict]:
        """Get all todos, optionally filtering completed ones."""
        if show_done:
            return self.todos
        return [t for t in self.todos if not t["done"]]

    def search(self, query: str) -> list[dict]:
        """Search todos by title."""
        query = query.lower()
        return [t for t in self.todos if query in t["title"].lower()]

    def stats(self) -> dict:
        """Get todo statistics."""
        total = len(self.todos)
        done = sum(1 for t in self.todos if t["done"])
        by_priority = {}
        for t in self.todos:
            p = t["priority"]
            by_priority[p] = by_priority.get(p, 0) + 1
        return {
            "total": total,
            "completed": done,
            "pending": total - done,
            "completion_rate": f"{done/total*100:.0f}%" if total else "N/A",
            "by_priority": by_priority,
        }


def format_todo(todo: dict) -> str:
    """Format a single todo for display."""
    status = "✅" if todo["done"] else "⬜"
    priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    icon = priority_icons.get(todo["priority"], "⚪")
    return f"  {status} [{todo['id']:>3}] {icon} {todo['title']}"


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    # Use in-memory for demo (won't create file)
    manager = TodoManager.__new__(TodoManager)
    manager.filepath = None
    manager.todos = []
    manager._save = lambda: None  # no-op for demo
    manager._next_id = lambda: max((t["id"] for t in manager.todos), default=0) + 1

    print("=" * 55)
    print("📋 Todo List Manager — Demo")
    print("=" * 55)

    # Add some tasks
    tasks = [
        ("Learn Python decorators", "high"),
        ("Read Clean Code book", "medium"),
        ("Set up CI/CD pipeline", "high"),
        ("Write unit tests", "medium"),
        ("Update documentation", "low"),
        ("Review pull requests", "medium"),
    ]

    print("\n  ➕ Adding tasks...")
    for title, priority in tasks:
        todo = manager.add(title, priority)
        print(format_todo(todo))

    # Complete some tasks
    print("\n  ✅ Completing tasks 1 and 4...")
    manager.complete(1)
    manager.complete(4)

    # Display all
    print("\n  📋 All Tasks:")
    print("  " + "-" * 45)
    for todo in manager.list_all():
        print(format_todo(todo))

    # Show pending only
    print("\n  ⏳ Pending Tasks:")
    print("  " + "-" * 45)
    for todo in manager.list_all(show_done=False):
        print(format_todo(todo))

    # Search
    print("\n  🔍 Search 'python':")
    for todo in manager.search("python"):
        print(format_todo(todo))

    # Stats
    print("\n  📊 Statistics:")
    stats = manager.stats()
    print(f"    Total     : {stats['total']}")
    print(f"    Completed : {stats['completed']}")
    print(f"    Pending   : {stats['pending']}")
    print(f"    Done rate : {stats['completion_rate']}")
    print(f"    Priority  : {stats['by_priority']}")

    # Delete
    print("\n  🗑️  Deleting task 3...")
    manager.delete(3)

    print("\n  📋 Final State:")
    print("  " + "-" * 45)
    for todo in manager.list_all():
        print(format_todo(todo))
