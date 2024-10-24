# Generated by Django 4.0.5 on 2024-07-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralApp', '0012_rename_picture5_campusavsreport_picture3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusavsreport',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='campusOrSchoolAcronym',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture1',
            field=models.ImageField(blank=True, upload_to='report_images/'),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture2',
            field=models.ImageField(blank=True, upload_to='report_images/'),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture3',
            field=models.ImageField(blank=True, upload_to='report_images/'),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='picture4',
            field=models.ImageField(blank=True, upload_to='report_images/'),
        ),
        migrations.AlterField(
            model_name='campusavsreport',
            name='program_type',
            field=models.CharField(max_length=50),
        ),
    ]
