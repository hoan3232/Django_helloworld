# Generated by Django 4.0.6 on 2022-07-18 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_customer_date_alter_customer_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.AddField(
            model_name='customer',
            name='dates',
            field=models.DateField(default=datetime.datetime(2022, 7, 18, 15, 40, 11, 713123)),
        ),
    ]