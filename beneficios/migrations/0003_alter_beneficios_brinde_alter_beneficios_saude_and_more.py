# Generated by Django 4.1.4 on 2023-05-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficios', '0002_rename_observação_beneficios_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficios',
            name='brinde',
            field=models.BooleanField(blank=True, choices=[(False, 'Não'), (None, 'Não'), (True, 'Sim')], null=True),
        ),
        migrations.AlterField(
            model_name='beneficios',
            name='saude',
            field=models.BooleanField(blank=True, choices=[(False, 'Não'), (None, 'Não'), (True, 'Sim')], null=True),
        ),
        migrations.AlterField(
            model_name='beneficios',
            name='va',
            field=models.BooleanField(blank=True, choices=[(False, 'Não'), (None, 'Não'), (True, 'Sim')], null=True),
        ),
        migrations.AlterField(
            model_name='beneficios',
            name='vt',
            field=models.BooleanField(blank=True, choices=[(False, 'Não'), (None, 'Não'), (True, 'Sim')], null=True),
        ),
    ]
