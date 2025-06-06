import json
import os
from datetime import datetime

# Constants
DATA_FILE = "tasks.json"

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["due_date"], data["completed"])

    def __str__(self):
        status = "✓" if self.completed else "✗"
        due = f"(Due: {self.due_date})" if self.due_date else ""
        return f"[{status}] {self.title} {due}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]

    def save_tasks(self):
        with open(DATA_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)
        print("Task added.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed: {removed.title}")
        else:
            print("Invalid index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid index.")

    def list_tasks(self, show_all=True):
        print("\n--- To-Do List ---")
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks):
            if show_all or not task.completed:
                print(f"{i + 1}. {task}")
        print()

    def list_completed_tasks(self):
        completed = [t for t in self.tasks if t.completed]
        if not completed:
            print("No completed tasks.")
            return
        print("\n--- Completed Tasks ---")
        for i, task in enumerate(completed):
            print(f"{i + 1}. {task}")
        print()

def get_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nOperation canceled.")
        return None

def main_menu():
    print("\nTo-Do List Manager")
    print("------------------")
    print("1. View All Tasks")
    print("2. View Pending Tasks")
    print("3. View Completed Tasks")
    print("4. Add New Task")
    print("5. Remove Task")
    print("6. Mark Task as Complete")
    print("7. Exit")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        main_menu()
        choice = get_input("Enter your choice (1-7): ")

        if choice == "1":
            todo_list.list_tasks()
        elif choice == "2":
            print("\n--- Pending Tasks ---")
            for i, task in enumerate(todo_list.tasks):
                if not task.completed:
                    print(f"{i + 1}. {task}")
            print()
        elif choice == "3":
            todo_list.list_completed_tasks()
        elif choice == "4":
            title = get_input("Enter task title: ")
            if not title:
                continue
            due_date = get_input("Enter due date (optional, YYYY-MM-DD): ")
            if due_date:
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format.")
                    continue
            else:
                due_date = None
            todo_list.add_task(title, due_date)
        elif choice == "5":
            todo_list.list_tasks()
            index = get_input("Enter task number to remove: ")
            if index and index.isdigit():
                todo_list.remove_task(int(index) - 1)
        elif choice == "6":
            todo_list.list_tasks()
            index = get_input("Enter task number to mark complete: ")
            if index and index.isdigit():
                todo_list.complete_task(int(index) - 1)
        elif choice == "7":
            todo_list.save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
