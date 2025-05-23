# Generated by Django 4.0 on 2022-01-10 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosannaWebsite', '0016_course_purchase_link_outcome_level_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricing_table',
            options={'verbose_name_plural': 'Pricing Tables'},
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.course')),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosannaWebsite.curriculum'),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
