# Generated by Django 4.2.5 on 2023-11-08 03:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userlocation", "0007_profile_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]