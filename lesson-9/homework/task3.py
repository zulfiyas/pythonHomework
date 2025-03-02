import json
import os

default_tasks = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

def ensure_tasks_file(filename):
    """Creates tasks.json if it doesn't exist"""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump(default_tasks, file, indent=4)

def load_tasks(filename):
    """Loads tasks from a JSON file"""
    with open(filename, "r") as file:
        return json.load(file)

def save_tasks(filename, tasks):
    """Saves tasks to a JSON file"""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Displays all tasks"""
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_json_to_csv(json_filename, csv_filename):
    """Converts tasks.json to tasks.csv"""
    import csv
    tasks = load_tasks(json_filename)
    
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    
    print(f"Tasks have been saved to {csv_filename}")

tasks_filename = "tasks.json"
csv_filename = "tasks.csv"

ensure_tasks_file(tasks_filename)  
tasks = load_tasks(tasks_filename)  
display_tasks(tasks)  
calculate_task_stats(tasks)
convert_json_to_csv(tasks_filename, csv_filename) 