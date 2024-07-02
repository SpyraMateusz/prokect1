from task_manager import TaskManager
from exceptions import TaskNotFoundException

def print_menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. Remove task")
    print("3. Edit task")
    print("4. View all tasks")
    print("5. Exit")

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            task_manager.add_task(title, description, priority)
            print("Task added successfully.")

        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to remove: "))
                task_manager.remove_task(task_id)
                print("Task removed successfully.")
            except TaskNotFoundException as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")

        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to edit: "))
                title = input("Enter new task title (leave empty to keep current): ")
                description = input("Enter new task description (leave empty to keep current): ")
                priority = input("Enter new task priority (leave empty to keep current): ")
                task_manager.edit_task(task_id, title, description, priority)
                print("Task edited successfully.")
            except TaskNotFoundException as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")

        elif choice == '4':
            tasks = task_manager.get_all_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()