# Generated by Django 4.2.7 on 2025-04-04 16:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0015_soberaniaalimentaria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bancarizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "establecimientos",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Establecimientos"
                    ),
                ),
                (
                    "total_unidades",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total Unidades"
                    ),
                ),
                (
                    "solicitadas",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Solicitadas"
                    ),
                ),
                (
                    "aprobados_enzona",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Aprobados Enzona"
                    ),
                ),
                (
                    "aprobados_transfermovil",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Aprobados Transfermóvil"
                    ),
                ),
                (
                    "operaciones_acumuladas",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Operaciones Acumuladas"
                    ),
                ),
                (
                    "importe_acumulado",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0)
                        ],
                        verbose_name="Importe Acumulado",
                    ),
                ),
                (
                    "empresa",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.empresa",
                        verbose_name="Empresa",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bancarización",
                "verbose_name_plural": "Bancarizaciones",
            },
        ),
    ]
