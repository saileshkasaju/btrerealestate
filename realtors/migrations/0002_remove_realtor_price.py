# Generated by Django 2.1 on 2019-05-04 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='price',
        ),
    ]