# Generated by Django 4.2.4 on 2023-09-20 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0017_alter_task_options_task_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task", options={"ordering": ["-created_at"]},
        ),
    ]
