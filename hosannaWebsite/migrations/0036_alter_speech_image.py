# Generated by Django 4.0.3 on 2022-03-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0035_alter_speech_speech_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speech',
            name='image',
            field=models.ImageField(default='comment/avatar.jpg', upload_to='comment'),
        ),
    ]
