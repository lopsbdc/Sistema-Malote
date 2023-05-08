# Generated by Django 4.1.4 on 2023-05-03 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_colaborador', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(max_length=50)),
                ('vt', models.BooleanField(blank=True, null=True)),
                ('va', models.BooleanField(blank=True, null=True)),
                ('saude', models.BooleanField(blank=True, null=True)),
                ('brinde', models.BooleanField(blank=True, null=True)),
                ('data_recebimento', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('data_att', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=50)),
                ('observação', models.CharField(max_length=50)),
            ],
        ),
    ]