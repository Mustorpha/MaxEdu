# Generated by Django 4.0.3 on 2022-03-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0066_rename_test_lesson_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
