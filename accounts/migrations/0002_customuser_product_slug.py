# Generated by Django 4.1.5 on 2023-01-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='product_slug',
            field=models.SlugField(blank=True, db_column='slug', error_messages={'required': 'Enter the slug field'}, help_text='slug', null=True, unique=True, verbose_name='slug'),
        ),
    ]
