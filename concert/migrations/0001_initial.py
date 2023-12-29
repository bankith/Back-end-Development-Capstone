# Generated by Django 4.2.8 on 2023-12-29 08:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("pic_url", models.CharField(max_length=1000)),
                ("event_country", models.CharField(max_length=255)),
                ("event_state", models.CharField(max_length=255)),
                ("event_city", models.CharField(max_length=255)),
                ("event_date", models.DateField(default=datetime.datetime.now)),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("lyrics", models.TextField()),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Concert",
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
                ("concert_name", models.CharField(max_length=255)),
                ("duration", models.IntegerField()),
                ("city", models.CharField(max_length=255)),
                ("date", models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name="ConcertAttending",
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
                (
                    "attending",
                    models.CharField(
                        choices=[
                            ("-", "-"),
                            ("Not Attending", "Not Attending"),
                            ("Attending", "Attending"),
                        ],
                        default="-",
                        max_length=100,
                    ),
                ),
                (
                    "concert",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendee",
                        to="concert.concert",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("concert", "user")},
            },
        ),
    ]
