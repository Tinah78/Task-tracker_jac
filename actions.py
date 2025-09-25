from task import Task

def add_task(task_list, title, description):
    task = Task(title, description)
    task_list.append(task)
    print(f"Task '{title}' added!")

def show_tasks(task_list):
    if not task_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(task_list, 1):
            status = "✓" if task.completed else "✗"
            print(f"{i}. {task.title} [{status}] - {task.description}")

def complete_task(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index].mark_complete()
        print(f"Task '{task_list[index].title}' marked complete!")
    else:
        print("Invalid task number.")