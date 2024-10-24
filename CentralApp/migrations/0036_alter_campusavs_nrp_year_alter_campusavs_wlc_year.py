# Generated by Django 5.0.7 on 2024-08-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0035_campusavs_nrp_year_campusavs_wlc_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campusavs",
            name="nrp_year",
            field=models.CharField(
                blank=True,
                help_text="When (year) was your latest NRP held?",
                max_length=10,
                null=True,
                verbose_name="NRP Year",
            ),
        ),
        migrations.AlterField(
            model_name="campusavs",
            name="wlc_year",
            field=models.CharField(
                blank=True,
                help_text="When (year) was your latest Welcome Program held?",
                max_length=10,
                null=True,
                verbose_name="Welcome Program Year",
            ),
        ),
    ]
