# Generated by Django 2.0 on 2021-05-10 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210506_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
    ]
