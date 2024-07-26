# Generated by Django 4.0.3 on 2022-04-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0081_application_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='application_form',
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Engr', 'Engr'), ('Dr', 'Dr')], default='Mr', max_length=5),
        ),
    ]
