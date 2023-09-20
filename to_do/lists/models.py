from django.db import models
from accounts.models import User


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']


class Task(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False, default='')
    description = models.TextField(max_length=1000, blank=False, null=False, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
