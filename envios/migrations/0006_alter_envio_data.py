# Generated by Django 4.1.4 on 2023-04-10 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0005_alter_envio_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 14, 49, 23, 804554)),
        ),
    ]