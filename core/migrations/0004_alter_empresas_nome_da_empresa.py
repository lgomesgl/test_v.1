# Generated by Django 4.2 on 2023-04-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_projeto_nome_do_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='Nome da empresa',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
