# Generated by Django 4.2.4 on 2023-09-18 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0013_alter_task_name"),
    ]

    operations = [
        migrations.AlterModelOptions(name="category", options={"ordering": ["-id"]},),
        migrations.AlterModelOptions(name="task", options={"ordering": ["-id"]},),
    ]