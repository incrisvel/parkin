# Generated by Django 5.0.1 on 2024-02-23 23:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0012_alter_perfillocal_nota_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfillocal',
            name='nota_media',
            field=models.FloatField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='nota média'),
            preserve_default=False,
        ),
    ]
