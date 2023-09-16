# Generated by Django 4.2.4 on 2023-09-16 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0006_remove_task_category_task_category"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="category",),
        migrations.AddField(
            model_name="task",
            name="category",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="lists.category",
            ),
        ),
    ]