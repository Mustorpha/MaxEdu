# Generated by Django 4.0.3 on 2022-03-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0038_alter_course_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
