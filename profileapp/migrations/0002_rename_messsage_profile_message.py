# Generated by Django 3.2.5 on 2021-08-10 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='messsage',
            new_name='message',
        ),
    ]
