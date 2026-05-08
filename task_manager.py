def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    print("Task added successfully!")
