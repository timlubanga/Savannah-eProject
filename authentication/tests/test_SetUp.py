from rest_framework.test import APITestCase
from django.urls import reverse


class BaseTestSetup(APITestCase):
    def setUp(self):
        self.loginUrl = reverse('emaillogin')
        self.signupUrl = reverse("emailregister")\

        self.userData = {
            "email": "test1@gmail.com",
            "username": "testuser1",
            "password": "1234567",
            "confirm_password": "1234567"
        }

        self.userUnmatchedPasswords = {
            "email": "test1@gmail.com",
            "username": "testuser1",
            "password": "12345670",
            "confirm_password": "1234567"
        }

        self.userCorrectlogin = {
            "username": "test1@gmail.com",
            "password": "1234567",

        }

        self.userUsername = {
            "username": "test11@gmail.com",
            "password": "1234567",

        }

        self.nullCredentials = {
            "username": "",
            "password": "",

        }

        self.noUserbody = {


        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
