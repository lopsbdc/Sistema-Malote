# Generated by Django 4.1.4 on 2023-04-10 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recebimentos', '0002_alter_recebidos_data_recebimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recebidos',
            name='data_recebimento',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 14, 48, 26, 32915)),
        ),
    ]