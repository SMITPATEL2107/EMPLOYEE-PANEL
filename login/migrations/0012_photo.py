# Generated by Django 2.0 on 2021-05-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20210510_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pics', models.ImageField(default='abc.jpg', upload_to='img/')),
            ],
        ),
    ]
