def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nNo tasks in your to-do list.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(todo_list, start=1):
        status = "✔ Done" if task["completed"] else "✘ Not Done"
        print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ").strip()
    if title:
        todo_list.append({"title": title, "completed": False})
        print("Task added.")
    else:
        print("Task title cannot be empty.")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    main()