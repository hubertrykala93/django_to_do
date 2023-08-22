# Generated by Django 4.2.4 on 2023-08-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="province",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]