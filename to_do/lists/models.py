from django.db import models
from accounts.models import User
from django.utils.timezone import now


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='', null=False, db_column='user_username')
    category = models.CharField(max_length=100, unique=False, blank=False, null=False, db_column='user_category')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.category


class Task(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, db_column='task_category')
    created_at = models.DateTimeField(default=now, db_column='task_created_at')
    name = models.CharField(max_length=100, blank=True, null=False, default='', unique=False, db_column='task_name')
    description = models.TextField(max_length=1000, blank=True, null=False, default='', unique=False,
                                   db_column='task_description')

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category

    class Meta:
        ordering = ['-created_at']
