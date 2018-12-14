from django.test import TestCase ,Client
from django.contrib.auth import get_user_model
import unittest 
from django.urls import reverse


# Create your tests here.
class SimpleTestCase(TestCase):

    def setup(self):
        self.client= Client()
       
    def test_home_view(self):
        response=self.client.get('/')
        usingTemplateName=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('home.html')
        self.assertEqual(usingTemplateName.status_code,200)

class TestingUserSignIn(TestCase):

    def setUp(self):
        self.user =get_user_model().objects.create(username='bot',email='bot@demo.com')

    def test_signup_form(self):
        query_All_Elements_In_Model=get_user_model().objects.all()
        getNumberOfUsers=query_All_Elements_In_Model.count()
        self.assertEquals(getNumberOfUsers,1)
        self.assertNotEqual(getNumberOfUsers,2)
        self.assertEqual(query_All_Elements_In_Model.first().username,self.user.username)
        self.assertEqual(query_All_Elements_In_Model.first().email,self.user.email)
  
    def testing_sign_up_page(self):
        response=self.client.get('/users/signup/')
        useTemplateName=self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('signup.html')
        self.assertEqual(useTemplateName.status_code,200)

 