# Generated by Django 4.1.5 on 2023-01-06 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
        ('program', '0002_program_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='foods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foods.foods'),
        ),
    ]
