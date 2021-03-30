from authentication.tests.test_SetUp import BaseTestSetup
from authentication.models import UserAccount
import json


class TestViews(BaseTestSetup):

    def test_user_cannot_register_without_required_data(self):
        res = self.client.post(self.signupUrl)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(str(res.data["email"][0]), "This field is required.")
        self.assertEqual(
            str(res.data["password"][0]), "This field is required.")
        self.assertEqual(
            str(res.data["username"][0]), "This field is required.")
        self.assertEqual(
            str(res.data["confirm_password"][0]), "This field is required.")

    def test_user_cannotregister_with_unmatching_passwords(self):
        res = self.client.post(
            self.signupUrl, self.userUnmatchedPasswords, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            str(res.data["non_field_errors"][0]), 'please ensure the passwords match')

    def test_user_can_successfully_signup_in_with_required_data(self):
        res = self.client.post(self.signupUrl, self.userData, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["email"], self.userData["email"])
        self.assertEqual(res.data["username"], self.userData["username"])

    def test_user_cannot_sigup_again_with_existing_username_and_email(self):
        res = self.client.post(self.signupUrl, self.userData, format="json")
        response = self.client.post(
            self.signupUrl, self.userData, format="json")
        self.assertEqual(
            str(response.data["email"][0]), "user account with this email already exists.")
        self.assertNotEqual(response.status_code, 201)

    def test_user_can_successfully_login_in_with_required_data(self):
        self.client.post(self.signupUrl, self.userData)
        response = self.client.post(
            self.loginUrl, self.userCorrectlogin, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"],
                         self.userCorrectlogin["username"])

    def test_user_cannnot_login_with_wrong_credentials(self):
        self.client.post(self.signupUrl, self.userData)
        response = self.client.post(
            self.loginUrl, self.userUsername, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data[0]),
                         "Please provide correct username or password")

    def test_user_cannnot_login_without_credentials(self):
        response = self.client.post(
            self.loginUrl, self.nullCredentials, format="json")
        self.assertEqual(response.status_code, 400)

        self.assertEqual(str(response.data[
                         "username"][0]), "This field may not be blank.")
        self.assertEqual(str(response.data[
                         "password"][0]), "This field may not be blank.")

    def test_user_cannnot_login_with_no_body(self):
        response = self.client.post(
            self.loginUrl, self.noUserbody, format="json")
        self.assertEqual(response.status_code, 400)

        self.assertEqual(str(response.data[
                         "username"][0]), "This field is required.")
        self.assertEqual(str(response.data[
                         "password"][0]), "This field is required.")

    def test_user_uses_unallowed_get_method_to_login(self):
        response = self.client.get(
            self.loginUrl, self.userCorrectlogin, format="json")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(str(response.data[
                         "detail"]), 'Method "GET" not allowed.')

    def test_user_unnallowed_uses_patch_method_to_login(self):
        response = self.client.patch(
            self.loginUrl, self.userCorrectlogin, format="json")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(str(response.data[
                         "detail"]), 'Method "PATCH" not allowed.')

    def test_user_uses_unnallowed_put_method_to_login(self):
        response = self.client.put(
            self.loginUrl, self.userCorrectlogin, format="json")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(str(response.data[
                         "detail"]), 'Method "PUT" not allowed.')

    def test_user_uses_unallowed_delete_method_to_login(self):
        response = self.client.delete(
            self.loginUrl, self.userCorrectlogin, format="json")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(str(response.data[
                         "detail"]), 'Method "DELETE" not allowed.')
