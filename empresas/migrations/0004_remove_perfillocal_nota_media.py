# Generated by Django 4.2.10 on 2024-02-19 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_perfillocal_nota_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfillocal',
            name='nota_media',
        ),
    ]
