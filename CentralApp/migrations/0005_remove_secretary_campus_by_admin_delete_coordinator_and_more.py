# Generated by Django 4.0.5 on 2024-07-10 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CentralApp', '0004_alter_campusavs_campusorschoolacronym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretary',
            name='campus_by_admin',
        ),
        migrations.DeleteModel(
            name='Coordinator',
        ),
        migrations.DeleteModel(
            name='Secretary',
        ),
    ]