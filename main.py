import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task_name, assigned_to):
    tasks = load_tasks()
    task = {"name": task_name, "assigned_to": assigned_to, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_name}' assigned to {assigned_to} added!")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available!")
        return

    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['name']} - Assigned to: {task['assigned_to']} - Status: {status}")

# Mark task as completed
def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['name']}' marked as completed!")
    else:
        print("Invalid task index!")

# Main menu
def main():
    while True:
        print("\n--- Team Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            assigned_to = input("Enter team member name: ")
            add_task(task_name, assigned_to)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            task_index = int(input("Enter task number to complete: ")) - 1
            complete_task(task_index)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
