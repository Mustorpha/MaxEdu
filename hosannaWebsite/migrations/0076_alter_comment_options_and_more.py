# Generated by Django 4.0.3 on 2022-04-02 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0075_applications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='applications',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='applications',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
