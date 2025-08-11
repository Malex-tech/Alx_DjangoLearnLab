from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass1234')
        self.other = User.objects.create_user(username='other', password='pass1234')
        self.post = Post.objects.create(title='Test', content='Content', author=self.user)

    def test_create_requires_login(self):
        c = Client()
        resp = c.get(reverse('blog:post-create'))
        self.assertEqual(resp.status_code, 302)  # redirect to login

    def test_author_can_edit(self):
        c = Client()
        c.login(username='author', password='pass1234')
        resp = c.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_non_author_cannot_edit(self):
        c = Client()
        c.login(username='other', password='pass1234')
        resp = c.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 403)  # or 302 if you redirect
