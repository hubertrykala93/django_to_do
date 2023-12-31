# Generated by Django 4.2.4 on 2023-09-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0022_remove_profile_last_name_user_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_of_birth",
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
