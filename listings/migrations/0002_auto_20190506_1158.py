# Generated by Django 2.1 on 2019-05-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='id_published',
            new_name='is_published',
        ),
    ]
