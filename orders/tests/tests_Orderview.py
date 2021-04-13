from orders.tests.test_baseSetUp import OrderBaseTestCase


class OrderTesCase(OrderBaseTestCase):

    def test_user_can_succeffully_create_orders_after_authentication(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["customer"], "test1@gmail.com")
        self.assertEqual(response.data["quantity"], 20)
        self.assertEqual(response.data["item"], "milk")

    def test_user_cannot_create_orders_without_authentication(self):
        response = self.client.get(
            self.createlistUrl, data=self.order)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            str(response.data["detail"]), 'Authentication credentials were not provided.')

    def test_user_not_create_orders_with_no_data(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.orderdataempty)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data["item"][0]), "This field is required.")
        self.assertEqual(
            str(response.data["quantity"][0]), "This field is required.")

    def test_user_not_create_orders_with_no_wrong_datatypes(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.orderwrongDataType)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(response.data["quantity"][0]), "A valid integer is required.")

    def test_user_can_retrieve_an_order(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)

        id = response.data["id"]

        retrieveurl = self.retrievedeleteUrl.replace('1', str(id))
        print(retrieveurl)
        response = self.client.get(
            retrieveurl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token))
        self.assertEqual(response.data["customer"], "test1@gmail.com")
        self.assertEqual(response.data["quantity"], 20)
        self.assertEqual(response.data["item"], "milk")
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_retrieve_an_order_with_wrongid(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)

        retrieveurl = self.retrievedeleteUrl.replace('1', str(200))
        response = self.client.get(
            retrieveurl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token))

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_retrieve_an_order_using_wrong_method(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)

        retrieveurl = self.retrievedeleteUrl.replace('1', str(200))
        response = self.client.post(
            retrieveurl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token))

        self.assertEqual(response.status_code, 405)
        self.assertEqual(
            str(response.data['detail']), 'Method "POST" not allowed.')

    def test_user_can_delete_an_order(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)
        id = response.data["id"]
        retrieveurl = self.retrievedeleteUrl.replace('1', str(id))
        response = self.client.delete(
            retrieveurl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token))

        self.assertEqual(response.status_code, 204)

    def test_user_can_delete_an_order_using_PATCH(self):
        response = self.client.post(
            self.createlistUrl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token), data=self.order)
        id = response.data["id"]
        retrieveurl = self.retrievedeleteUrl.replace('1', str(id))
        response = self.client.patch(
            retrieveurl, HTTP_AUTHORIZATION='Bearer {token}'.format(
                token=self.token))

        self.assertEqual(response.status_code, 405)

        self.assertEqual(
            str(response.data['detail']), 'Method "PATCH" not allowed.')
