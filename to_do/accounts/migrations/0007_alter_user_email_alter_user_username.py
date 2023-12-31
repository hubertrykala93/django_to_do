# Generated by Django 4.2.4 on 2023-08-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_remove_user_city_remove_user_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True,
                default="",
                max_length=254,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                default="",
                max_length=50,
                unique=True,
            ),
        ),
    ]
