# Generated by Django 4.0.3 on 2022-03-08 17:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0029_alter_event_event_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
