# Generated by Django 4.0.6 on 2022-08-19 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
