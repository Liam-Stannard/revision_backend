from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker


class BaseUserManagementTestCase(TestCase):
    def setUp(self):
        faker = Faker()
        username = faker.user_name()
        self.password = faker.password()

        self.user = User.objects.create_user(username=username)
        self.user.set_password(self.password)
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()
