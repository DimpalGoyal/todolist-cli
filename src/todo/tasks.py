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

"""
def add_tasks():
    pass"""

"""
def mark_complete():
    pass  """