# Generated by Django 4.1.4 on 2023-05-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficios', '0005_alter_beneficios_brinde_alter_beneficios_saude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficios',
            name='observacao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='beneficios',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]