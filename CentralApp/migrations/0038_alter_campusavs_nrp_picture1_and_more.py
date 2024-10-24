# Generated by Django 5.0.7 on 2024-08-14 19:31

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0037_campusavs_nrp_totalattendance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture1",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (1)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture2",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (2)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture3",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (3)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture4",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (4)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture5",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (5)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture6",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (6)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture7",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (7)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_picture8",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (8)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture1",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (1)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture2",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (2)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture3",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (3)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture4",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (4)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture5",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (5)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture6",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (6)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture7",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (7)",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_picture8",
            field=models.FileField(
                blank=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="report_images/",
                verbose_name="Picture (8)",
            ),
        ),
    ]
