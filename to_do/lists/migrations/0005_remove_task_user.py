# Generated by Django 4.2.4 on 2023-09-16 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0004_task_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="user",),
    ]