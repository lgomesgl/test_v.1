# Generated by Django 4.2 on 2023-05-01 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_projeto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresas',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='pessoas',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
    ]
