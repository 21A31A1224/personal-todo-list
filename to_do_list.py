import json
import shutil
import os

# Task class to represent each task
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed  # Add completed argument to constructor

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} - {self.category} - {status}\n{self.description}"

# Save tasks to a JSON file
def save_tasks(tasks, file_name='tasks.json'):
    with open(file_name, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from a JSON file
def load_tasks(file_name='tasks.json'):
    try:
        with open(file_name, 'r') as f:
            return [Task(**data) for data in json.load(f)]  # Loads completed status from file
    except FileNotFoundError:
        return []

# Display the list of tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    print("Task added!")
    save_tasks(tasks)  # Save after adding a task

# Mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1].mark_completed()
            print("Task marked as completed!")
            save_tasks(tasks)  # Save after marking a task as completed
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted!")
            save_tasks(tasks)  # Save after deleting a task
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Backup tasks to a separate file
def backup_tasks(original_file='tasks.json', backup_file='tasks_backup.json'):
    if os.path.exists(original_file):
        shutil.copy(original_file, backup_file)
        print("Backup created successfully!")
    else:
        print("No tasks to backup. Please add tasks first.")

# Edit a task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to edit: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            new_title = input(f"Enter new title (leave blank to keep '{task.title}'): ")
            new_description = input(f"Enter new description (leave blank to keep current description): ")
            new_category = input(f"Enter new category (leave blank to keep '{task.category}'): ")
            
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_category:
                task.category = new_category
            
            print("Task updated!")
            save_tasks(tasks)  # Save after editing the task
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Search tasks by title, category, or description
def search_task(tasks):
    query = input("Enter a keyword to search: ").lower()
    found_tasks = [task for task in tasks if query in task.title.lower() or query in task.description.lower() or query in task.category.lower()]

    if found_tasks:
        print("\nSearch results:")
        display_tasks(found_tasks)
    else:
        print("No tasks found matching the search criteria.")

# Main menu and program flow
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Backup Tasks")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            search_task(tasks)
        elif choice == '7':
            backup_tasks()
        elif choice == '8':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


