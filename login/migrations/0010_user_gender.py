# Generated by Django 2.0 on 2021-05-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20210510_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='gender', max_length=20),
        ),
    ]
