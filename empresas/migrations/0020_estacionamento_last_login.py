# Generated by Django 5.0.1 on 2024-02-08 03:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0019_remove_estacionamento_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamento',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
