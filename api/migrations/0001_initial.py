# Generated by Django 5.0.6 on 2024-07-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_name", models.CharField(max_length=150)),
                ("desc", models.CharField(max_length=500)),
                ("idOfUser_fk", models.IntegerField(default=1)),
            ],
        ),
    ]
