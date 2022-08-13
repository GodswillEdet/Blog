from curses import reset_prog_mode
import email
from turtle import title
from urllib import response
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            title = 'a good title',
            body = 'a nice content',
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title='a good title')
        self.assertEquals(str(post), post.title)

    def test_post_content(self):
        self.assertEquals(f'{self.post.title}', 'a good title')
        self.assertEquals(f'{self.post.author}', 'testuser')
        self.assertEquals(f'{self.post.body}', 'a nice content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'a nice content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_details_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(no_response.status_code, 404)
        self.assertContains(response, 'a nice content')
        self.assertTemplateUsed(response, 'post_detail.html')
