# Generated by Django 5.0.1 on 2024-02-08 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_options_rename_senha_cliente_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='password',
            new_name='senha',
        ),
    ]