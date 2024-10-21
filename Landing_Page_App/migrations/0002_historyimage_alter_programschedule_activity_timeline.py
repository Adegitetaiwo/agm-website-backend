# Generated by Django 5.0.7 on 2024-10-02 11:54

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Landing_Page_App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoryImage",
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
                ("campusOrSchoolAcronym", models.CharField(max_length=50)),
                (
                    "picture",
                    models.FileField(
                        storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                        upload_to="history_images/",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Campus AVS Historical Pictures",
            },
        ),
        migrations.AlterField(
            model_name="programschedule",
            name="activity_timeline",
            field=models.CharField(
                max_length=50,
                unique=True,
                verbose_name="Timeline of Activity (e.g 10:00 - 12:00 am GMT+1)",
            ),
        ),
    ]