# Generated by Django 4.2.7 on 2025-04-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0028_vehiculoscumnales_comunales"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiculoscumnales",
            name="activo",
            field=models.PositiveIntegerField(default=0, verbose_name="Activo"),
        ),
        migrations.AlterField(
            model_name="vehiculoscumnales",
            name="cantidad",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Cantidad"
            ),
        ),
        migrations.AlterField(
            model_name="vehiculoscumnales",
            name="municipio",
            field=models.CharField(max_length=256, verbose_name="Municipio"),
        ),
    ]
