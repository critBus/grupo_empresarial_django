# Generated by Django 4.2.7 on 2025-04-17 23:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0034_alter_plandeconstruccion_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="informaciongeneral",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="materialdeconstruccion",
            name="empresa",
        ),
        migrations.RemoveField(
            model_name="materialplasticoreciclado",
            name="empresa",
        ),
        migrations.RemoveField(
            model_name="informaciongeneral",
            name="empresa",
        ),
    ]
