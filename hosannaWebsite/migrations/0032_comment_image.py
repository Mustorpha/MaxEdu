# Generated by Django 4.0.3 on 2022-03-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0031_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='comment/default.jpg', upload_to='comment'),
        ),
    ]
