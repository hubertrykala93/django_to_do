# Generated by Django 4.2.4 on 2023-09-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0005_remove_task_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="category",),
        migrations.AddField(
            model_name="task",
            name="category",
            field=models.ManyToManyField(to="lists.category"),
        ),
    ]
