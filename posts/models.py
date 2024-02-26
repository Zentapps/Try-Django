
import uuid
from django.db import models
from django.db.models import Max
from django.utils import timezone
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime

from blogs.middlewares import RequestMiddleware


def basedata(self, request):
    # Check is create
    if self._state.adding:
        self.auto_id = (self.__class__.objects.aggregate(max_auto_id=Max('auto_id')).get('max_auto_id') or 0) + 1
        if request.user.is_authenticated:
            self.creator = request.user

    # If updating
    if request.user.is_authenticated:
        self.updater = request.user
    self.date_updated = timezone.now()

from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True,editable=False)
    creator = models.ForeignKey(get_user_model(), null=True, blank=True, related_name="creator_%(class)s_objects", limit_choices_to={'is_active': True}, on_delete=models.CASCADE,editable=False)
    updater = models.ForeignKey(get_user_model(), null=True, blank=True, related_name="updater_%(class)s_objects", limit_choices_to={'is_active': True}, on_delete=models.CASCADE,editable=False)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True,editable=False)
    date_updated = models.DateTimeField(auto_now_add=True,editable=False)
    is_deleted = models.BooleanField(default=False,editable=False)

    class Meta:
        abstract = True



class Post(BaseModel):
    title = models.CharField(max_length=255,)
    content = RichTextField(config_name='minimum')
    publication_date = models.DateField()
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # First we need create an instance of that and later get the current_request assigned
        request = RequestMiddleware(get_response=None)
        if hasattr(request.thread_local, "current_request"):
            request = request.thread_local.current_request
            basedata(self, request)

        self.full_clean()

        return super().save(*args, **kwargs)