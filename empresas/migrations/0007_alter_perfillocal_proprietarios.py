# Generated by Django 5.0.1 on 2024-02-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_alter_perfillocal_proprietarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfillocal',
            name='proprietarios',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
