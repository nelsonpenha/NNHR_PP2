# Generated by Django 3.1.2 on 2021-01-17 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0004_auto_20210117_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta_usuario',
            name='nombre_encargado',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
