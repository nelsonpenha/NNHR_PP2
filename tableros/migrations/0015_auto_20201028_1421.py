# Generated by Django 3.1.2 on 2020-10-28 17:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0014_merge_20201028_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='descripcion',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='id_tablero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tableros.tablero'),
            preserve_default=False,
        ),
    ]
