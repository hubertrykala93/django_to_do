# Generated by Django 4.2.4 on 2023-08-14 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_first_name_user_last_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="city",),
        migrations.RemoveField(model_name="user", name="country",),
        migrations.RemoveField(model_name="user", name="first_name",),
        migrations.RemoveField(model_name="user", name="last_name",),
        migrations.RemoveField(model_name="user", name="province",),
    ]
