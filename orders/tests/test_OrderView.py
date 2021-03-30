from orders.tests.test_baseSetUp import OrderBaseTestCase

from authentication.models import UserAccount


class CustomerTestCase(OrderBaseTestCase):
    def test_user_cannot_access_own_data_without_authentication(self):
        response = self.client.get(self.createlistUrl)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            str(response.data["detail"]), "Authentication credentials were not provided.")

    def test_user_can_succeffully_access_own_data_after_authentication(self):
        # self.client = self.client.credentials(
        #     HTTP_AUTHORIZATION='Bearer {token}'.format(token=self.token))

        response = self.client.get(
            self.customerDetail, HTTP_AUTHORIZATION='Bearer {token}'.format(token=self.token))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["account"]
                         ["username"], self.userData["username"])

    def test_user_cannot_use_post_to_retrieve_own_data(self):
        response = self.client.post(
            self.customerDetail, HTTP_AUTHORIZATION='Bearer {token}'.format(token=self.token))
        self.assertEqual(response.status_code, 405)

    def test_user_can_update_phone_numbers(self):
        response = self.client.patch(
            self.customerDetail, data=self.data, HTTP_AUTHORIZATION='Bearer {token}'.format(token=self.token))
        self.assertEqual(response.status_code, 202)
        self.assertEqual(
            response.data["phone_number"], self.data["phone_number"])

    def test_user_cannot_provide_phone_blank_data(self):

        response = self.client.patch(self.customerDetail,
                                     data=self.dataBlank, HTTP_AUTHORIZATION='Bearer {token}'.format(token=self.token))
        self.assertEqual(str(response.data[0]),
                         "please provide data to be updated")
        self.assertEqual(response.status_code, 400)
