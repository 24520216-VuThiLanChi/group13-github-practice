# ui.py - Phụ trách: Thiên Lộc
def show_menu():
    print("\n" + "=" * 35)
    print("         TO-DO LIST APP")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("0. Exit")
    print("=" * 35)

def show_task_list(tasks):
    print("\n" + "-" * 35)
    if not tasks:
        print("  (No tasks yet)")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task.get("done") else " "
            print(f"  {i}. [{status}] {task['title']}")
    print("-" * 35)

def show_search_result(results):
    print("\n--- Search Results ---")
    if not results:
        print("  No tasks found.")
    else:
        for task in results:
            status = "✓" if task.get("done") else " "
            print(f"  [{status}] {task['title']}")

def prompt_input(message):
    return input(f"  >> {message}: ").strip()

def show_message(msg, success=True):
    icon = "✅" if success else "❌"
    print(f"\n  {icon} {msg}")

def show_welcome():
    print("\n" + "=" * 35)
    print("   Welcome to To-Do List App!")
    print("   Manage your tasks easily.")
    print("=" * 35)

def show_delete_confirm(title):
    print(f"\n  ⚠️  Delete task: '{title}' ?")
    confirm = input("  >> Confirm (y/n): ").strip().lower()
    return confirm == "y"