# Generated by Django 4.0.3 on 2022-04-02 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0077_applications_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='Address',
            new_name='address',
        ),
    ]
