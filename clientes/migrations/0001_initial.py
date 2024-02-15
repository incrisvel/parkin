# Generated by Django 4.2.10 on 2024-02-12 02:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critica', models.CharField(max_length=1000, null=True, verbose_name='crítica')),
                ('data_envio', models.DateTimeField(auto_now_add=True, verbose_name='data de envio')),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'verbose_name': 'avaliação de usuários',
                'verbose_name_plural': 'avaliações de usuários',
                'ordering': ['data_envio'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(default='', max_length=200)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
