# Generated by Django 4.1.4 on 2023-04-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0018_alter_codigopostagem_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigopostagem',
            name='postagem',
            field=models.CharField(max_length=50),
        ),
    ]
