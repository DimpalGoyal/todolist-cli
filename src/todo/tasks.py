from utils import load_tasks, save_tasks

def view_tasks():
    tasks = load_tasks()["tasks"]
    print()
    if not tasks:
        print("no task to display")
        return
    
    print("Your Do To List:")
    for idx, task in enumerate(tasks, start=1):
        status = "[completed]" if task["complete"] else "[pending]"
        print(f"{idx}. {task['description']} {status}")


def add_tasks():
    tasks = load_tasks()
    desc = input("enter a new task: ").strip()

    if not desc:
        print("task cannot be empty.")
        return    
    
    tasks["tasks"].append({"description": desc, "complete": False})
    save_tasks(tasks)
    print(f"task '{desc}' added successfully.")


def mark_complete():
    tasks_data = load_tasks()
    tasks = tasks_data["tasks"]

    if not tasks:
        print("no task to mark")
        return
    
    view_tasks()
    try:
        num = int(input("Enter the task number to mark complete: ").strip())
        if 1 <= num <= len(tasks):
            tasks[num - 1]["complete"] = True
            save_tasks(tasks_data)
            print(f'task {num} marked as complete.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task():
    tasks_data = load_tasks()
    tasks = tasks_data["tasks"]

    if not tasks:
        print("no task to remove")
        return
    
    view_tasks()
    try:
        num = int(input("Enter the task number to remove: ").strip())
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            save_tasks(tasks_data)
            print(f"Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")