# Generated by Django 5.1.3 on 2024-12-23 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dictionary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TodayWord",
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
                ("date", models.DateField(auto_now_add=True)),
                ("today_word", models.CharField(max_length=100)),
                (
                    "today_pronunciation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("today_meaning", models.TextField(blank=True, null=True)),
                ("priority", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "dictionary",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dictionary.dictionary",
                    ),
                ),
            ],
        ),
    ]