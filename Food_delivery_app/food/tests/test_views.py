from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from foodapp.models import FoodModel, CustomModel, OrderModel

class TestViews(TestCase):

    # setup
    def setUp(self):
       self.client = Client()
       self.user = {
           'email':'testemail@gmail.com',
           'username':'username',
           'password':'password',
           'password2':'password',
           'fullname':'fullname',
       }

       self.adminloginpage_url = reverse('adminloginpage')
       self.adminhomepage_url = reverse('adminhomepage')
       self.homepageview_url = reverse('homepage')
       self.usersignuppage_url = reverse('usersignuppage')
       self.userloginview_url = reverse('userloginpage')
       self.customerwelcomeview_url = reverse('customerpage')
       self.userorders_url = reverse('userorders')
       self.adminorders_url = reverse('adminorders')
       self.usermanage_url = reverse('usermanage')
       self.adminlogs_url = reverse('adminlogs')
       self.userprofile_url = reverse('userprofile')
       self.supportpage_url = reverse('supportpage')
       self.contactpage_url = reverse('contactpage')
       self.cartepage_url = reverse('carte')


    def test_adminloginview_get(self):
        # test
        response = self.client.get(self.adminloginpage_url)
        # assertions
        self.assertEquals(response.status_code, 200) # can reach the page
        self.assertTemplateUsed(response, 'foodapp/adminlogin.html')

    
    def test_adminhomepageview_get_with_required_session_variable(self):
        # test
        session = self.client.session
        session['is_admin_logged_in'] = True
        session.save()
        response = self.client.get(self.adminhomepage_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/adminhomepage.html')


    def test_adminhomepageview_get_without_required_session_variable(self):
        # test
        response = self.client.get(self.adminhomepage_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_homepageview_get(self):
        # test
        response = self.client.get(self.homepageview_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/homepage.html')


    def test_signuppage_get(self):
        # test
        response = self.client.get(self.usersignuppage_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/usersignuppage.html')


    def test_can_sign_up(self):
        self.client.post(self.usersignuppage_url, self.user, format='text/html')
        response=self.client.post(self.usersignuppage_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


    def test_loginpage_get(self):
        # test
        response = self.client.get(self.userloginview_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/userlogin.html')

    
    def test_can_log_in(self):
        self.client.post(self.userloginview_url, self.user, format='text/html')
        response=self.client.post(self.userloginview_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)


    def test_1_user_creation(self):
        created_user = User.objects.create_user(self.user['username'], self.user['email'], self.user['password'])
        self.assertEqual(User.objects.count(), 1)


    def test_userorders_without_authenticated_user(self):
        # test
        response = self.client.get(self.userorders_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_adminorders_without_authenticated_admin(self):
        # test
        response = self.client.get(self.userorders_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_usermanage_without_authenticated_admin(self):
        # test
        response = self.client.get(self.usermanage_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_adminlogs_without_authenticated_admin(self):
        # test
        response = self.client.get(self.adminlogs_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_userprofile_without_authenticated_user(self):
        # test
        response = self.client.get(self.userprofile_url)
        # assertions
        self.assertEquals(response.status_code, 302)


    def test_supportpage_get(self):
        # test
        response = self.client.get(self.supportpage_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/contactandsupportpage.html')


    def test_contactpage_get(self):
        # test
        response = self.client.get(self.contactpage_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/contactandsupportpage.html')

    
    def test_cartepage_get(self):
        # test
        response = self.client.get(self.cartepage_url)
        # assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodapp/cartepage.html')