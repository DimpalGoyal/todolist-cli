from src.todo.tasks import view_tasks, add_tasks, mark_complete

def main():
    while True:
        print("\n=== To-Do CLI ===")
        print("1. view tasks")
        print("2 Add task")
        print("3. Mark task complete")
        print("4. Exit")

        choice = int(input("Choose an option: ").strip())

        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_tasks()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("Invaild choice. Try again.")


if __name__ == "__main__":
    main()                                                                