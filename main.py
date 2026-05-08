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

  