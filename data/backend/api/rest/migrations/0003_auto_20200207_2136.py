# Generated by Django 3.0.3 on 2020-02-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20200207_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female')], max_length=1),
        ),
    ]
