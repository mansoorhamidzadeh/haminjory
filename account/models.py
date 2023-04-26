from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class User(AbstractUser):
    is_author = models.BooleanField(default=False,)
    special_user = models.DateTimeField(default=timezone.now, )

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True