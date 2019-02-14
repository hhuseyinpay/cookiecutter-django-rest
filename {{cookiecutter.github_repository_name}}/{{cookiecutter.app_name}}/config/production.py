import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import Common


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn", )

    #sentry_sdk.init(
    #    dsn="**SENTRY URL**",
    #    integrations=[DjangoIntegration()]
    #)
