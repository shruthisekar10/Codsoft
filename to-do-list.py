import json
import os

# Step 2: Basic Data Structure
tasks = []

# Step 3: Core Functions
def add_task(task):
    tasks.append({"task": task, "completed": False})

def list_tasks():
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx + 1}. {task['task']} - {status}")

def mark_task_as_complete(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
    else:
        print("Invalid task number")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number")

def save_tasks(filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename):
    global tasks
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []

# Step 4: User Interface
def print_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")

def main():
    load_tasks('tasks.json')  # Load tasks from file if any
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as complete: "))
            mark_task_as_complete(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '5':
            save_tasks('tasks.json')
        elif choice == '6':
            load_tasks('tasks.json')
        elif choice == '7':
            save_tasks('tasks.json')
            print("ExitiBuy groceriesng the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
