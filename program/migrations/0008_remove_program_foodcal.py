# Generated by Django 4.1.5 on 2023-01-06 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_program_foodcal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='foodcal',
        ),
    ]
