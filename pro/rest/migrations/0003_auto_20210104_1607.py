# Generated by Django 3.1.2 on 2021-01-04 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_remove_user_conditionfortemp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
