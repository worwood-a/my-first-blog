from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import home_page

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        self.assertTemplateUsed(response, 'blog/home.html')