# Generated by Django 4.1.4 on 2023-04-12 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recebimentos', '0017_alter_recebidos_rastreio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='recebidos',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recebimentos.setores'),
        ),
    ]