# Generated by Django 4.2 on 2023-05-01 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_projeto_nome_do_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='Nome do projeto',
            field=models.CharField(max_length=100),
        ),
    ]
