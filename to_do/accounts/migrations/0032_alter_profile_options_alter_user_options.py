# Generated by Django 4.2.6 on 2023-10-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0031_alter_profile_city_alter_profile_country_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile", options={"verbose_name_plural": "Profiles"},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "User", "verbose_name_plural": "Accounts"},
        ),
    ]