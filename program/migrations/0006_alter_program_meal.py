# Generated by Django 4.1.5 on 2023-01-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_program_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='meal',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=200, null=True),
        ),
    ]
