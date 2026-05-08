def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    print("\n===== TASK LIST =====")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['title']} [{status}]")


def delete_task(tasks, index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed['title']}")
    else:
        print("Invalid task number!")


def search_task(tasks, keyword):
    print("\n===== SEARCH RESULT =====")

    found = False

    for i, task in enumerate(tasks, start=1):
        if keyword.lower() in task["title"].lower():
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['title']} [{status}]")
            found = True

    if not found:
        print("No matching task found.")

def mark_completed(tasks, index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")