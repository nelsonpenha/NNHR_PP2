# Generated by Django 3.1.2 on 2020-10-26 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0009_auto_20201005_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fases',
            old_name='id_tarjeta',
            new_name='id_tablero',
        ),
    ]
