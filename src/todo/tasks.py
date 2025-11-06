from src.todo.utils import load_tasks, save_tasks

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


"""
def mark_complete():
    pass  """