class Task:
    def __init__(self, task_id, title, description, priority):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Task({self.id}, {self.title}, {self.description}, {self.priority})"