# Generated by Django 4.0 on 2022-03-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0025_event_delete_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hosannaWebsite.event'),
        ),
        migrations.AddField(
            model_name='event',
            name='assesments',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
    ]
