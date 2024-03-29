# Generated by Django 4.2.10 on 2024-02-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meal",
            name="meal",
        ),
        migrations.AddField(
            model_name="meal",
            name="meal_type",
            field=models.CharField(
                choices=[
                    ("Breakfast", "Breakfast"),
                    ("Morning Snack", "Morning Snack"),
                    ("Lunch", "Lunch"),
                    ("Afternoon Snack", "Afternoon Snack"),
                    ("Dinner", "Dinner"),
                    ("Evening Snack", "Evening Snack"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
