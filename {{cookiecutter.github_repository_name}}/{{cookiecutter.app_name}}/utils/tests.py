from django.urls import reverse
from rest_framework.test import APITestCase

from {{cookiecutter.app_name}}.users.models import User


class BaseTest(APITestCase):
    def create_user(self, username, password, user_type=User.VELI, login=True):
        user = User.objects.create(username=username, user_type=user_type)
        user.set_password(password)
        user.save()
        if login:
            self.client.login(username=username, password=password)
        return user

    @staticmethod
    def reverse(self, url_name, *args, **kwargs):
        return reverse(url_name, *args, **kwargs)
