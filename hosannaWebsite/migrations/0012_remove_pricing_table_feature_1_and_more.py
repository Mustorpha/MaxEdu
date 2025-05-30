# Generated by Django 4.0 on 2021-12-15 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0011_course_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_1',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_2',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_3',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_4',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_5',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_6',
        ),
        migrations.RemoveField(
            model_name='pricing_table',
            name='feature_7',
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=128)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.pricing_table')),
            ],
        ),
    ]
