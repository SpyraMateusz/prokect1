import unittest
from task_manager import TaskManager
from task import Task
from exceptions import TaskNotFoundException

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test Task", "This is a test task.", "High")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[1].title, "Test Task")
        self.assertEqual(self.manager.tasks[1].description, "This is a test task.")
        self.assertEqual(self.manager.tasks[1].priority, "High")

    def test_remove_task(self):
        self.manager.add_task("Test Task", "This is a test task.", "High")
        self.manager.remove_task(1)
        self.assertEqual(len(self.manager.tasks), 0)
        with self.assertRaises(TaskNotFoundException):
            self.manager.remove_task(1)

    def test_edit_task(self):
        self.manager.add_task("Test Task", "This is a test task.", "High")
        self.manager.edit_task(1, title="Updated Task", description="Updated description.", priority="Low")
        self.assertEqual(self.manager.tasks[1].title, "Updated Task")
        self.assertEqual(self.manager.tasks[1].description, "Updated description.")
        self.assertEqual(self.manager.tasks[1].priority, "Low")

    def test_view_tasks(self):
        self.manager.add_task("Task 1", "Description 1", "High")
        self.manager.add_task("Task 2", "Description 2", "Medium")
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

if __name__ == '__main__':
    unittest.main()