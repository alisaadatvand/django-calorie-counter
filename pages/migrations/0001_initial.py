# Generated by Django 4.1.5 on 2023-01-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('weight', models.FloatField(help_text='Kg', null=True)),
                ('height', models.FloatField(help_text='m', null=True)),
            ],
        ),
    ]