from exceptions import TaskNotFoundException
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description, priority):
        task = Task(self.next_id, title, description, priority)
        self.tasks[self.next_id] = task
        self.next_id += 1

    def remove_task(self, task_id):
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with id {task_id} not found")
        del self.tasks[task_id]

    def edit_task(self, task_id, title=None, description=None, priority=None):
        if task_id not in self.tasks:
            raise TaskNotFoundException(f"Task with id {task_id} not found")
        task = self.tasks[task_id]
        if title:
            task.title = title
        if description:
            task.description = description
        if priority:
            task.priority = priority

    def get_all_tasks(self):
        return list(self.tasks.values())