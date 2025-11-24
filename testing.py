# ================================
#   SIMPLE TO-DO LIST APPLICATION
# ================================

todo_list = []


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("============================")


def add_task():
    task = input("Enter task to add: ")
    todo_list.append(task)
    print(f"Task added: {task}")


def view_tasks():
    if not todo_list:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")


def remove_task():
    if not todo_list:
        print("No tasks to remove!")
        return

    view_tasks()
    num_text = input("Enter task number to remove: ")

    try:
        num = int(num_text)
        removed = todo_list.pop(num - 1)
        print(f"Removed: {removed}")
    except ValueError:
        print("Invalid number!")


def clear_tasks():
    todo_list.clear()
    print("All tasks cleared!")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
