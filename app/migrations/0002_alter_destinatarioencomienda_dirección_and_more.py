# Generated by Django 4.1.3 on 2022-11-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Nombre Destinatario',
            name='Dirección',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='destinatarioencomienda',
            name='descripción',
            field=models.TextField(max_length=300),
        ),
    ]
