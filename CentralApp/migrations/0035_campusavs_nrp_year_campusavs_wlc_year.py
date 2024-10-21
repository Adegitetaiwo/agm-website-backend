# Generated by Django 5.0.7 on 2024-08-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0034_campusavs_flyer2_alter_campusavs_flyer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="campusavs",
            name="nrp_year",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="NRP Year"
            ),
        ),
        migrations.AddField(
            model_name="campusavs",
            name="wlc_year",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name="Welcome Program Year",
            ),
        ),
    ]