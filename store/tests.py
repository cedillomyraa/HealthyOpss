from django.test import TestCase
#test view models imports
from unittest import skip
from django.contrib.auth.models import User
from store.models import Category, Product
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.deta1 = Category.objects.create(name='home', slug='home')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/type/field attributes

        """

        data = self.deta1
        self.assertTrue(isinstance(data,Category))#preforms the test if a = blank then work

    def test_category_model_entry(self):
        """
        Test Category model default name

        """
        data = self.deta1
        self.assertEqual(str(data), 'home')

#product testing models
class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='category', slug='category')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Roasted Cajun Chicken', created_by_id=1, slug= 'roasted cajun chicken', price='14.00', image= 'meal1')

    def test_category_model_entry(self):
        """
        Test product model data insertion/type/field attributes

        """

        data = self.data1 
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data), 'Roasted Cajun Chicken')

#test views

@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='Roasted Cajun Chicken', slug='roasted cajun chicken')
        Product.objects.create(category_id=1, title='Roasted Cajun Chicken', created_by_id=1,
                            slug='roasted cajun chicken', price='14.00', image='meal1')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('store:category_list', args=['roasted cajun chicken']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['roasted cajun chicken']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>HealthyOps</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
        Example: Using request factory
        """
        request = self.factory.get('/item')
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>HealthyOps</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)