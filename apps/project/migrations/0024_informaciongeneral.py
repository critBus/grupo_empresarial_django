# Generated by Django 4.2.7 on 2025-04-05 18:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0023_alter_indicadorgeneral_porciento_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="InformacionGeneral",
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
                ("total", models.PositiveIntegerField(verbose_name="Total")),
                (
                    "cubiertos",
                    models.PositiveIntegerField(verbose_name="Cubiertos"),
                ),
                (
                    "desglosados_gobierno",
                    models.PositiveIntegerField(
                        verbose_name="Desglosados Gobierno"
                    ),
                ),
                (
                    "desglosados_tercero",
                    models.PositiveIntegerField(
                        verbose_name="Desglosados Tercero"
                    ),
                ),
                (
                    "fluctuacion",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(1),
                        ],
                        verbose_name="Fluctuación",
                    ),
                ),
                ("dato", models.CharField(max_length=256, verbose_name="Dato")),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.empresa",
                        verbose_name="Empresa",
                    ),
                ),
            ],
            options={
                "verbose_name": "Información General",
                "verbose_name_plural": "Informaciones Generales",
                "unique_together": {("empresa", "dato")},
            },
        ),
    ]
