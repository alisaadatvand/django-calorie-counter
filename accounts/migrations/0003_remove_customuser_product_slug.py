# Generated by Django 4.1.5 on 2023-01-07 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='product_slug',
        ),
    ]