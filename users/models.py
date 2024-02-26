import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from django.db.models import Q, UniqueConstraint
from django.utils import timezone


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exist."),
        },
    )


    email = models.EmailField(
        _('email'),
        error_messages={
            'unique': "A user with this email already exist.",
        },
        null=True, blank=True,
    )

    image = models.ImageField(null=True, blank=True)


    @property
    def get_display_name(self):
        return self.get_full_name() or self.username or self.email

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


    def __str__(self):
        return self.get_display_name

