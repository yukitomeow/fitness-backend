# Generated by Django 4.2.10 on 2024-03-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meal", "0005_remove_fooditem_meal"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="foods",
            field=models.ManyToManyField(to="meal.fooditem"),
        ),
    ]
