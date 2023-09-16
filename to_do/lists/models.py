from django.db import models
from accounts.models import User
from django.utils.timezone import now


class Category(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category


class Task(models.Model):
    category = models.OneToOneField(to=Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    content = models.CharField(max_length=1000, unique=False, blank=False, null=False)

    def __str__(self):
        return self.content
