def display_menu():
    
    Displays the main menu options for the To-Do List application.
    
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Exit")
    print("-----------------------")

def view_tasks(tasks):
    
    Displays all tasks in the To-Do List.
    
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task["description"]}")
        print("-----------------------")

def add_task(tasks):
    
    Adds a new task to the To-Do List.
    
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    print(f"Task \"{description}\" added.")

def mark_task_complete(tasks):
    
    Marks a task as complete based on its number.
    
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task {task_num} marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def remove_task(tasks):
    
    Removes a task from the To-Do List based on its number.
    
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task \"{removed_task["description"]}\" removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
