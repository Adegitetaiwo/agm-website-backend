# Generated by Django 5.0.7 on 2024-10-05 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CentralApp", "0043_alter_historyimage_options_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ReportImage",
            new_name="ReportsImage",
        ),
    ]
