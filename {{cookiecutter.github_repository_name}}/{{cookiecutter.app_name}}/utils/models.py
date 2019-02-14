from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils.managers import SoftDeletableManager


class {{cookiecutter.app_name}}BaseManager(SoftDeletableManagerMixin, models.Manager):
    pass


class {{cookiecutter.app_name}}BaseModel(TimeStampedModel, SoftDeletableModel):
    class Meta:
        abstract = True
