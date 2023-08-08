# Generated by Django 4.2.4 on 2023-08-03 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentModel",
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
                ("first_name", models.CharField(default="", max_length=15)),
                ("last_name", models.CharField(default="", max_length=15)),
                ("phone", models.CharField(default="", max_length=13)),
                ("email", models.EmailField(max_length=254)),
                ("date_of_birth", models.DateField(default=datetime.datetime.now)),
            ],
            options={
                "db_table": "student",
            },
        ),
    ]
