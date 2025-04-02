# Generated by Django 4.2.7 on 2025-04-02 22:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "project",
            "0009_remove_inversiones_plan_remove_inversiones_porciento_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="MaterialPlasticoReciclado",
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
                    "no_material",
                    models.IntegerField(
                        max_length=10,
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="No.",
                    ),
                ),
                ("materia", models.CharField(max_length=255, verbose_name="Material")),
                (
                    "unidad_de_medida",
                    models.CharField(max_length=255, verbose_name="Unidad de Medida"),
                ),
                ("plan", models.IntegerField(verbose_name="Plan")),
                ("real", models.IntegerField(verbose_name="Real")),
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
                "verbose_name": "Material Plástico Reciclado",
                "verbose_name_plural": "Materiales Plásticos Reciclados",
            },
        ),
    ]
