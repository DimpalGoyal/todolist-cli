import json
import os

FILE_NAME = "todo.json"

def load_tasks():
    """load tasks from json file or return an empty structure if file not found"""
    if not os.path.exists(FILE_NAME):
        return {"tasks": []}
    try:
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: corrupted JSON file, starting fresh.")
        return {"tasks": []}
    
def save_tasks(tasks):
    """save task list to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)    
