# Generated by Django 4.0 on 2021-12-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0003_course_section_delete_slider_course_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='feature_image',
            field=models.ImageField(default='default.jpg', upload_to='course'),
        ),
    ]
