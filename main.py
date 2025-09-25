from actions import add_task, show_tasks, complete_task
from ai import suggest_task

def main():
    tasks = []

    print("=== Welcome to Gemini Task Assistant ===")

    while True:
        print("\nOptions: [1] Add task [2] Show tasks [3] Complete task [4] AI Suggest [5] Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task title: ")
            description = input("Task description: ")
            add_task(tasks, title, description)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == "4":
            suggest_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()