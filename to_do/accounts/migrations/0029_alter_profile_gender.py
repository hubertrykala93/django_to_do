# Generated by Django 4.2.4 on 2023-09-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0028_remove_user_first_name_remove_user_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                choices=[
                    ("Not Defined", "Not Defined"),
                    ("Male", "Male"),
                    ("Female", "Female"),
                ],
                default="",
                max_length=20,
            ),
        ),
    ]
