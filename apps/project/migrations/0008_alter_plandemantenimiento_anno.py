# Generated by Django 4.2.7 on 2025-04-02 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0007_remove_plandemantenimiento_plan_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plandemantenimiento",
            name="anno",
            field=models.PositiveIntegerField(default=2025, verbose_name="Año"),
        ),
    ]
