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

    show_menu()
    choice = input("Enter your choice: ")

  