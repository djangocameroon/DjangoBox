from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topic, Feedback
from .forms import FeedbackForm


class TopicModelTest(TestCase):
    def test_topic_creation(self):
        topic = Topic.objects.create(name="Test Topic")
        self.assertEqual(str(topic), "Test Topic")
        self.assertEqual(topic.name, "Test Topic")


class FeedbackModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")

    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            user_name="Test User",
            topic=self.topic,
            content="This is a test feedback"
        )
        self.assertEqual(str(feedback), "Feedback by Test User on Test Topic")
        self.assertEqual(feedback.user_name, "Test User")
        self.assertEqual(feedback.topic, self.topic)
        self.assertEqual(feedback.content, "This is a test feedback")


class FeedbackFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'user_name': 'Test User',
            'topic_name': 'Test Topic',
            'content': 'This is test content'
        }
        form = FeedbackForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'user_name': '',
            'topic_name': '',
            'content': ''
        }
        form = FeedbackForm(data=form_data)
        self.assertFalse(form.is_valid())


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.topic = Topic.objects.create(name="Test Topic")
        self.feedback = Feedback.objects.create(
            user_name="Test User",
            topic=self.topic,
            content="Test feedback content"
        )

    def test_feedback_view_get(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'DjangoBox Community Feedback')
        self.assertContains(response, 'Test User')

    def test_feedback_view_post_valid(self):
        form_data = {
            'user_name': 'New User',
            'topic_name': 'New Topic',
            'content': 'New feedback content'
        }
        response = self.client.post(reverse('core:home'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST
        self.assertTrue(Feedback.objects.filter(user_name='New User').exists())

    def test_feedback_view_post_ajax(self):
        form_data = {
            'user_name': 'AJAX User',
            'topic_name': 'AJAX Topic',
            'content': 'AJAX feedback content'
        }
        response = self.client.post(
            reverse('core:home'),
            data=form_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Feedback.objects.filter(user_name='AJAX User').exists())

    def test_pagination(self):
        # Create multiple feedbacks to test pagination
        for i in range(15):
            Feedback.objects.create(
                user_name=f'User {i}',
                topic=self.topic,
                content=f'Feedback content {i}'
            )
        
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        self.assertEqual(len(response.context['page_obj']), 10)  # First page should have 10 items
