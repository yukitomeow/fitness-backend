# Generated by Django 4.2.10 on 2024-02-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="cat",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]