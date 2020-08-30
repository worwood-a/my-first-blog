from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .models import EducationItem, TechnicalItem, WorkItem, OtherItem

'''
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_can_save_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/')

        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items =Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

'''

class CVPageTest(TestCase):

    def test_cv_page_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv.html')

    def test_displays_all_items(self):
        EducationItem.objects.create(name='Test School 1', start_year=2011, end_year=2012, description='Test Description')
        EducationItem.objects.create(name='Test School 2', start_year=2013, end_year=2014, description='Test Description')
        response = self.client.get('/cv/')
        self.assertIn('Test School 1: 2011 - 2012', response.content.decode())
        self.assertIn('Test School 2: 2013 - 2014', response.content.decode())

        TechnicalItem.objects.create(title='Test Tech 1', content='Test Content')
        TechnicalItem.objects.create(title='Test Tech 2', content='Test Content')
        response = self.client.get('/cv/')
        self.assertIn('Test Tech 1', response.content.decode())
        self.assertIn('Test Tech 2', response.content.decode())

        WorkItem.objects.create(title='Test Job 1', start_year=2015, end_year=2016, description='Test Description')
        WorkItem.objects.create(title='Test Job 2', start_year=2017, end_year=2018, description='Test Description')
        response = self.client.get('/cv/')
        self.assertIn('Test Job 1: 2015 - 2016', response.content.decode())
        self.assertIn('Test Job 2: 2017 - 2018', response.content.decode())

        OtherItem.objects.create(name='Test Interest 1', content='Test Content')
        OtherItem.objects.create(name='Test Interest 2', content='Test Content')
        response = self.client.get('/cv/')
        self.assertIn('Test Interest 1', response.content.decode())
        self.assertIn('Test Interest 2', response.content.decode())

    def test_only_saves_items_when_necessary(self):
        response = self.client.get('/cv/')
        self.assertEqual(EducationItem.objects.count(), 0)
        self.assertEqual(TechnicalItem.objects.count(), 0)
        self.assertEqual(WorkItem.objects.count(), 0)
        self.assertEqual(OtherItem.objects.count(), 0)

class FormPageTest(TestCase):

    def test_form_page_returns_correct_html(self):
        response = self.client.get('/cv/edit/New Education/')
        self.assertTemplateUsed(response, 'blog/cv_new.html')
        self.assertIn('New Education', response.content.decode())

        response = self.client.get('/cv/edit/New Technical Skill/')
        self.assertTemplateUsed(response, 'blog/cv_new.html')
        self.assertIn('New Technical Skill', response.content.decode())

        response = self.client.get('/cv/edit/New Work Experience/')
        self.assertTemplateUsed(response, 'blog/cv_new.html')
        self.assertIn('New Work Experience', response.content.decode())

        response = self.client.get('/cv/edit/New Interest Or Skill/')
        self.assertTemplateUsed(response, 'blog/cv_new.html')
        self.assertIn('New Interest Or Skill', response.content.decode())

        response = self.client.get('/cv/edit/Fake Page/')
        self.assertTemplateUsed(response, 'blog/cv_new.html')
        self.assertIn('New Interest Or Skill', response.content.decode(), 'I think this means the Fake Page Test Failed')

    def test_form_page_saves_POST_request(self):
        response = self.client.post('/cv/edit/New Education/', data={'name': 'Test School', 'start_year': 2011, 'end_year': 2012, 'description': 'This is a test post'})
        self.assertEqual(EducationItem.objects.count(), 1)
        new_e_item = EducationItem.objects.first()
        self.assertEqual(new_e_item.name, 'Test School')
        self.assertEqual(new_e_item.start_year, 2011)
        self.assertEqual(new_e_item.end_year, 2012)
        self.assertEqual(new_e_item.description, 'This is a test post')

        response = self.client.post('/cv/edit/New Technical Skill/', data={'title': 'Test Tech Skill', 'content': 'This is a test post'})
        self.assertEqual(TechnicalItem.objects.count(), 1)
        new_t_item = TechnicalItem.objects.first()
        self.assertEqual(new_t_item.title, 'Test Tech Skill')
        self.assertEqual(new_t_item.content, 'This is a test post')

        response = self.client.post('/cv/edit/New Work Experience/', data={'title': 'Test Work', 'start_year': 2013, 'end_year': 2014, 'description': 'This is a test post'})
        self.assertEqual(WorkItem.objects.count(), 1)
        new_w_item = WorkItem.objects.first()
        self.assertEqual(new_w_item.title, 'Test Work')
        self.assertEqual(new_w_item.start_year, 2013)
        self.assertEqual(new_w_item.end_year, 2014)
        self.assertEqual(new_w_item.description, 'This is a test post')

        response = self.client.post('/cv/edit/New Skill Or Interest/', data={'name': 'Test Interest', 'content': 'This is a test post'})
        self.assertEqual(OtherItem.objects.count(), 1)
        new_o_item = OtherItem.objects.first()
        self.assertEqual(new_o_item.name, 'Test Interest')
        self.assertEqual(new_o_item.content, 'This is a test post')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/edit/New Education/', data={'name': 'Test School', 'start_year': 2011, 'end_year': 2012, 'description': 'This is a test post'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

        response = self.client.post('/cv/edit/New Technical Skill/', data={'title': 'Test Tech Skill', 'content': 'This is a test post'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

        response = self.client.post('/cv/edit/New Work Experience/', data={'title': 'Test Work', 'start_year': 2013, 'end_year': 2014, 'description': 'This is a test post'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

        response = self.client.post('/cv/edit/New Skill Or Interest/', data={'name': 'Test Interest', 'content': 'This is a test post'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

class ItemModelsTest(TestCase):

    def test_save_and_retrieve_e_item(self):
        e_item_one = EducationItem()
        e_item_two = EducationItem()

        e_item_one.name = "School"
        e_item_one.start_year = 2000
        e_item_one.end_year = 2001
        e_item_one.description = "Item 1"
        e_item_one.save()

        e_item_two.name = "University"
        e_item_two.start_year = 2002
        e_item_two.end_year = 2003
        e_item_two.description = "Item 2"
        e_item_two.save()

        saved_items = EducationItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item_one = saved_items[0]
        saved_item_two = saved_items[1]
        self.assertEqual(saved_item_one.name, "School")
        self.assertEqual(saved_item_one.start_year, 2000)
        self.assertEqual(saved_item_one.end_year, 2001)
        self.assertEqual(saved_item_one.description, "Item 1")
        self.assertEqual(saved_item_two.name, "University")
        self.assertEqual(saved_item_two.start_year, 2002)
        self.assertEqual(saved_item_two.end_year, 2003)
        self.assertEqual(saved_item_two.description, "Item 2")

    def test_save_and_retrieve_t_item(self):
        t_item_one = TechnicalItem()
        t_item_two = TechnicalItem()

        t_item_one.title = "Juggling"
        t_item_one.content = "Like a clown"
        t_item_one.save()

        t_item_two.title = "Skipping"
        t_item_two.content = "With a rope"
        t_item_two.save()

        saved_items = TechnicalItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item_one = saved_items[0]
        saved_item_two = saved_items[1]
        self.assertEqual(saved_item_one.title, "Juggling")
        self.assertEqual(saved_item_one.content, "Like a clown")
        self.assertEqual(saved_item_two.title, "Skipping")
        self.assertEqual(saved_item_two.content, "With a rope")

    def test_save_and_retrieve_w_item(self):
        w_item_one = WorkItem()
        w_item_two = WorkItem()

        w_item_one.title = "Job"
        w_item_one.start_year = 2000
        w_item_one.end_year = 2001
        w_item_one.description = "Item 1"
        w_item_one.save()

        w_item_two.title = "Intern"
        w_item_two.start_year = 2002
        w_item_two.end_year = 2003
        w_item_two.description = "Item 2"
        w_item_two.save()

        saved_items = WorkItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item_one = saved_items[0]
        saved_item_two = saved_items[1]
        self.assertEqual(saved_item_one.title, "Job")
        self.assertEqual(saved_item_one.start_year, 2000)
        self.assertEqual(saved_item_one.end_year, 2001)
        self.assertEqual(saved_item_one.description, "Item 1")
        self.assertEqual(saved_item_two.title, "Intern")
        self.assertEqual(saved_item_two.start_year, 2002)
        self.assertEqual(saved_item_two.end_year, 2003)
        self.assertEqual(saved_item_two.description, "Item 2")

    def test_save_and_retrieve_o_item(self):
        o_item_one = OtherItem()
        o_item_two = OtherItem()

        o_item_one.name = "Photography"
        o_item_one.content = "With cameras"
        o_item_one.save()

        o_item_two.name = "Painting"
        o_item_two.content = "With brushes"
        o_item_two.save()

        saved_items = OtherItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_item_one = saved_items[0]
        saved_item_two = saved_items[1]
        self.assertEqual(saved_item_one.name, "Photography")
        self.assertEqual(saved_item_one.content, "With cameras")
        self.assertEqual(saved_item_two.name, "Painting")
        self.assertEqual(saved_item_two.content, "With brushes")