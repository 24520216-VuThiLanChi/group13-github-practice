from task_manager import (
    add_task,
    view_tasks,
    delete_task,
    search_task,
    mark_completed
)

from file_handler import load_tasks, save_tasks
from ui import show_menu

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task name: ")
        add_task(tasks, title)
        save_tasks(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        search_task(tasks, keyword)

    elif choice == "4":
        view_tasks(tasks)
        index = int(input("Enter task number to delete: "))
        delete_task(tasks, index)
        save_tasks(tasks)

    elif choice == "5":
        view_tasks(tasks)
        index = int(input("Enter task number to mark completed: "))
        mark_completed(tasks, index)
        save_tasks(tasks)

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")