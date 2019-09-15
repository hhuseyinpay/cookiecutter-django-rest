from django.db import models
from django.dispatch import receiver
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils.managers import SoftDeletableManagerMixin
from simple_history.models import HistoricalRecords
from simple_history.signals import pre_create_historical_record


class {{cookiecutter.app_name}}BaseManager(SoftDeletableManagerMixin, models.Manager):
    pass


class IPAddressHistoricalModel(models.Model):
    """
    Abstract model for history models tracking the IP address.
    """
    ip_address = models.GenericIPAddressField('IP address')

    class Meta:
        abstract = True


class {{cookiecutter.app_name}}BaseModel(TimeStampedModel, SoftDeletableModel):
    objects = {{cookiecutter.app_name}}BaseManager()

    class Meta:
        abstract = True


@receiver(pre_create_historical_record)
def pre_create_historical_record_callback(sender, **kwargs):
    history_instance = kwargs.get('history_instance', None)
    # thread.request for use only when the simple_history middleware is on and enabled
    history_instance.ip_address = HistoricalRecords.thread.request.META['REMOTE_ADDR']
