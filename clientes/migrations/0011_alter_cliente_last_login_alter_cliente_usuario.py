# Generated by Django 5.0.1 on 2024-02-09 02:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_alter_cliente_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(choices=[('ADMIN', 'Admin'), ('CLIENTE', 'Cliente'), ('ESTACIONAMENTO', 'Estacionamento')], default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]