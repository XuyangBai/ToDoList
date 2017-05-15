from django.test import TestCase
import datetime

# Create your tests here.
from .models import Task
from django.urls import reverse
from django.test import Client
from django.test.utils import setup_test_environment

class TaskMethodTests(TestCase):
    def Task_expire_time_early_than_created_time(self):
        task = Task(title='title',content='content',expire_date=datetime.date.today()-datetime.timedelta(10))
        self.assertIs(task.finished, 1)

class TaskViewTests(TestCase):
    def test_tasklist_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code,200)