from django.db import models
from accounts.models import User
from django.utils.timezone import now


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='', null=True)
    category = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-id']


class Task(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
    name = models.CharField(max_length=100, blank=False, null=False, default='', unique=True)
    description = models.TextField(max_length=1000, blank=False, null=False, default='')

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category

    class Meta:
        ordering = ['-created_at']
