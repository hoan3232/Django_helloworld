# Generated by Django 4.0.6 on 2022-07-18 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateField(default=datetime.datetime.today, verbose_name=datetime.datetime.today),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
