from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

tasks = [
    Task("Project Report", "2026-06-15", 1),
    Task("Assignment", "2026-06-10", 2),
    Task("Presentation", "2026-06-20", 3)
]

tasks.sort(key=lambda task: task.due_date)

print("Task Schedule")

for task in tasks:
    print(
        task.name,
        task.due_date.strftime("%Y-%m-%d"),
        "Priority:",
        task.priority
    )