# Generated by Django 5.1.2 on 2024-10-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plant",
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
                ("name", models.CharField(max_length=255)),
                ("species", models.CharField(max_length=255)),
                ("watering_frequency_days", models.IntegerField()),
                ("last_watered_date", models.DateField()),
            ],
            options={
                "ordering": ["-last_watered_date"],
            },
        ),
    ]
