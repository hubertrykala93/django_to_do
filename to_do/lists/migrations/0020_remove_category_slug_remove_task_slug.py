# Generated by Django 4.2.4 on 2023-09-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0019_category_slug_task_slug"),
    ]

    operations = [
        migrations.RemoveField(model_name="category", name="slug",),
        migrations.RemoveField(model_name="task", name="slug",),
    ]
