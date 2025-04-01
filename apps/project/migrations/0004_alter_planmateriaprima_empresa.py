# Generated by Django 4.2.7 on 2025-04-01 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0003_alter_atencionpoblacion_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="planmateriaprima",
            name="empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="project.empresa",
                verbose_name="Empresa",
            ),
        ),
    ]
