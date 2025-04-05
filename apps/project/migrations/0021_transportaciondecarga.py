# Generated by Django 4.2.7 on 2025-04-05 16:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0020_alter_perdida_indicador_transportaciondepasajeros"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransportacionDeCarga",
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
                ("plan", models.PositiveIntegerField(verbose_name="Plan")),
                ("real", models.PositiveIntegerField(verbose_name="Real")),
                (
                    "porciento",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Porcentaje",
                    ),
                ),
                (
                    "carga",
                    models.CharField(max_length=256, verbose_name="Carga"),
                ),
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
                "verbose_name": "Transportación de Carga",
                "verbose_name_plural": "Transportaciones de carga",
                "unique_together": {("empresa", "carga")},
            },
        ),
    ]
