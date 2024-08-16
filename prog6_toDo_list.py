import json
from datetime import datetime

class Task:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        due_date = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        return f"[{status}] {self.title} (Due: {due_date}) - Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task '{self.tasks[index].title}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' deleted.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, default=str, indent=4)
        print(f"Tasks saved to {filename}.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [self._task_from_dict(task) for task in tasks_data]
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"No saved tasks found in {filename}.")
        except json.JSONDecodeError:
            print("Error decoding JSON file.")

    def _task_from_dict(self, task_dict):
        task = Task(task_dict["title"])
        task.due_date = datetime.strptime(task_dict["due_date"], "%Y-%m-%d") if task_dict["due_date"] else None
        task.created_at = datetime.strptime(task_dict["created_at"], "%Y-%m-%d %H:%M:%S")
        task.completed = task_dict["completed"]
        return task

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Save tasks")
        print("6. Load tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d") if due_date_input else None
            todo_list.add_task(title, due_date)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            todo_list.list_tasks()
            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.list_tasks()
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            filename = input("Enter filename to save tasks (default: tasks.json): ")
            todo_list.save_tasks(filename if filename else "tasks.json")
        elif choice == "6":
            filename = input("Enter filename to load tasks (default: tasks.json): ")
            todo_list.load_tasks(filename if filename else "tasks.json")
        elif choice == "7":
            todo_list.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
