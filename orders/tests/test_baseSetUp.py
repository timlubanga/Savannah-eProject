from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from authentication.models import UserAccount

User = UserAccount


class OrderBaseTestCase(APITestCase):
    def setUp(self):
        self.userData = {
            "email": "test1@gmail.com",
            "username": "testuser1",
            "password": "1234567",
            "confirm_password": "1234567"
        }

        self.order = {
            "item": "milk",
            "quantity": 20
        }

        self.orderwrongDataType = {
            "item": False,
            "quantity": "three"
        }
        self.orderdataempty = {

        }
        self.data = {"phone_number": "123456789"}
        self.datacustomerid = {"customer_id": "122334555666"}
        self.dataBlank = {}
        self.createlistUrl = reverse("createandlistorders")
        self.retrievedeleteUrl = reverse(
            "retrieveanddeleteorders", kwargs={"pk": 1})
        self.customerDetail = reverse("customerDetails")
        self.signupUrl = reverse("emailregister")
        self.res = self.client.post(
            self.signupUrl, self.userData, format="json")
        self.token = self.res.data["tokens"]["access"]

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_urls(self):
        self.assertEqual(self.createlistUrl, "/orders/createlist/")
        self.assertEqual(self.retrievedeleteUrl,
                         "/orders/retrievedelete/1/")
        print(self.retrievedeleteUrl)
