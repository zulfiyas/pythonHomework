import csv
import json
import os

class Task:
    
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }


class StorageStrategy:

    def save_tasks(self, tasks):
        raise NotImplementedError

    def load_tasks(self):
        raise NotImplementedError


class CSVStorage(StorageStrategy):
    
    FILE_NAME = "tasks.csv"

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])  # Header
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        print("Tasks saved to CSV successfully.")

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(row["Task ID"], row["Title"], row["Description"], row["Due Date"], row["Status"]))
        return tasks


class JSONStorage(StorageStrategy):
    
    FILE_NAME = "tasks.json"

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, mode="w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
        print("Tasks saved to JSON successfully.")

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, mode="r") as file:
                data = json.load(file)
                for item in data:
                    tasks.append(Task(item["task_id"], item["title"], item["description"], item["due_date"], item["status"]))
        return tasks


class TaskManager:
    
    def __init__(self, storage_strategy):
        self.tasks = storage_strategy.load_tasks()
        self.storage_strategy = storage_strategy

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        if any(task.task_id == task_id for task in self.tasks):
            print("Error: Task ID already exists.")
            return

        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()
        due_date = input("Enter Due Date (YYYY-MM-DD, press enter if not applicable): ").strip() or None
        status = input("Enter Status (Pending/In Progress/Completed): ").strip()

        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\nTasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        task = next((task for task in self.tasks if task.task_id == task_id), None)

        if not task:
            print("Task not found.")
            return

        task.title = input(f"Enter new Title (Current: {task.title}): ").strip() or task.title
        task.description = input(f"Enter new Description (Current: {task.description}): ").strip() or task.description
        task.due_date = input(f"Enter new Due Date (Current: {task.due_date}, press enter to keep): ").strip() or task.due_date
        task.status = input(f"Enter new Status (Current: {task.status}): ").strip() or task.status

        print("Task updated successfully!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ").strip()
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]

        if not filtered_tasks:
            print("No tasks found with this status.")
        else:
            print("\nFiltered Tasks:")
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        self.storage_strategy.save_tasks(self.tasks)

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    print("Select Storage Format:")
    print("1. CSV")
    print("2. JSON")
    storage_choice = input("Enter choice: ").strip()

    if storage_choice == "1":
        storage = CSVStorage()
    elif storage_choice == "2":
        storage = JSONStorage()
    else:
        print("Invalid choice. Defaulting to JSON storage.")
        storage = JSONStorage()

    manager = TaskManager(storage)
    manager.menu()