# Generated by Django 4.2.7 on 2025-04-04 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0013_cuentascobrar_por_cobrar_a_terceros_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cuentascobrar",
            name="indice_gestion_cloro",
        ),
        migrations.AddField(
            model_name="cuentascobrar",
            name="indice_gestion_cobro",
            field=models.FloatField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Índice Gestión Cobro",
            ),
        ),
    ]
