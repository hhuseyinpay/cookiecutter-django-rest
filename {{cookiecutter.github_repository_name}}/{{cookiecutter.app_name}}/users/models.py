import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from simple_history.models import HistoricalRecords

from {{cookiecutter.app_name}}.utils.models import {{cookiecutter.app_name}}BaseModel, {{cookiecutter.app_name}}BaseManager, IPAddressHistoricalModel


class CustomUserManager({{cookiecutter.app_name}}BaseManager, UserManager):
    pass


class User({{cookiecutter.app_name}}BaseModel, AbstractUser):
    ADMIN = 1
    EDITOR = 2
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (EDITOR, 'Editor'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    telefon_no = models.CharField(max_length=11, blank=True)
    dogum_tarihi = models.DateField(null=True, blank=True)

    history = HistoricalRecords(table_name='user_history', bases=[IPAddressHistoricalModel, ], inherit=True)
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
