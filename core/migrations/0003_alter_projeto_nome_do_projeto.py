# Generated by Django 4.2 on 2023-04-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pessoas_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='Nome do projeto',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
