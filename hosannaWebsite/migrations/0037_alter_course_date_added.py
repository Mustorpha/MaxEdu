# Generated by Django 4.0.3 on 2022-03-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0036_alter_speech_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
