from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Sample Task")

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Sample Task")
        self.assertFalse(self.task.completed)  # default should be False

    def test_task_str_method(self):
        self.assertEqual(str(self.task), self.task.title)

    def test_task_toggle_complete(self):
        self.task.completed = True
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertTrue(updated_task.completed)

    # def test_task_default_fields(self):
    #     self.assertIsNotNone(self.task.created_at)
    #     self.assertIsNotNone(self.task.updated_at)

    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)
