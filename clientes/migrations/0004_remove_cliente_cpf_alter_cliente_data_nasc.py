# Generated by Django 5.0.1 on 2024-01-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_nasc',
            field=models.DateTimeField(default='', verbose_name='data de nascimento'),
        ),
    ]