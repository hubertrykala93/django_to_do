# Generated by Django 4.2.4 on 2023-09-16 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0008_alter_task_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]