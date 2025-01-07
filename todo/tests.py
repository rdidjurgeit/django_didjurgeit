from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from .models import Task
from .forms import TaskForm, UserRegisterForm


class TestTaskForm(TestCase):

    def test_form_is_valid(self):
        task_form = TaskForm({
            'title': 'This is a great task',
            'content': 'This is a great task',
            'status': 'not_started',
        })
        self.assertTrue(task_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid_with_blank_title(self):
        task_form = TaskForm({
            'title': '',
            'content': 'This is a great task',
            'status': 'not_started',
        })
        self.assertFalse(task_form.is_valid(), msg="Form is valid")


class TestUserRegisterForm(TestCase):

    def test_form_is_valid(self):
        reg_form = UserRegisterForm({
            'username': 'rapha',
            'email': 'rapha@example.org',
            'password1': 'askdjk2kjdlksdf1234',
            'password2': 'askdjk2kjdlksdf1234',
        })
        self.assertTrue(reg_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid_with_common_password(self):
        reg_form = UserRegisterForm({
            'username': 'rapha',
            'email': 'rapha@example.org',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(reg_form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_with_different_passwords(self):
        reg_form = UserRegisterForm({
            'username': 'rapha',
            'email': 'rapha@example.org',
            'password1': 'askdjk2kjdlksdf1234',
            'password2': 'askdjk2kjdlksdf12345',
        })
        self.assertFalse(reg_form.is_valid(), msg="Form is valid")


class TestTaskViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.task1 = Task(
            title="Task title 1",
            user=self.user,
            content="Task content 1",
            status='not_started'
        )
        self.task1.save()
        self.task2 = Task(
            title="Task title 2",
            user=self.user,
            content="Task content 2",
            status='not_started'
        )
        self.task2.save()

    def test_render_task_list(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task To-Do List", response.content)
        self.assertIn(b"Task title 1", response.content)
        self.assertIn(b"Task content 1", response.content)
        self.assertIn(b"Task title 2", response.content)
        self.assertIn(b"Task content 2", response.content)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_render_task_list_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('Location', response.headers)
        self.assertIn('/accounts/login', response.headers['Location'])
