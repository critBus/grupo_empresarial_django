# Generated by Django 4.2.7 on 2025-04-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0005_alter_planmateriaprima_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inmuebles",
            name="cantidad",
        ),
        migrations.RemoveField(
            model_name="inmuebles",
            name="tipo",
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="almacenes",
            field=models.PositiveIntegerField(
                default=0, verbose_name="almacenes"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="alojamiento",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Alojamiento"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="banos_p",
            field=models.PositiveIntegerField(
                default=0, verbose_name="baños P"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="bar",
            field=models.PositiveIntegerField(default=0, verbose_name="Bar"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="base_carga",
            field=models.PositiveIntegerField(
                default=0, verbose_name="base carga"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="bodegas",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Bodegas"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="c_elaboracion",
            field=models.PositiveIntegerField(
                default=0, verbose_name="C. Elabor."
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="c_nocturno",
            field=models.PositiveIntegerField(
                default=0, verbose_name="C Nocturno"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="cabaret",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Cabaret"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="cafeterias",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Cafeterías"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="capillas",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Capillas"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="carnicerias",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Carnicerías"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="circulos_s",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Círculos .S"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="comedores",
            field=models.PositiveIntegerField(
                default=0, verbose_name="comedores"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="cpl",
            field=models.PositiveIntegerField(default=0, verbose_name="CPL"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="dulcerias",
            field=models.PositiveIntegerField(
                default=0, verbose_name="dulcerías"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="fabricas",
            field=models.PositiveIntegerField(
                default=0, verbose_name="fabricas"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="farmacias_opticas",
            field=models.PositiveIntegerField(
                default=0, verbose_name="farmacias y opticas / C. auditivo"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="floristeria",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Floristería"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="funeraria",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Funeraria"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="heladerias",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Heladerías"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="incinerador",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Incinerador"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="loc_oficina",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Loc. oficina"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="m_ideal",
            field=models.PositiveIntegerField(
                default=0, verbose_name="M. Ideal"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="mais",
            field=models.PositiveIntegerField(default=0, verbose_name="MAIS"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="merendero",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Merendero"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="minitalleres",
            field=models.PositiveIntegerField(
                default=0, verbose_name="minitalleres"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="nave_pasaje",
            field=models.PositiveIntegerField(
                default=0, verbose_name="nave pasaje"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="pana_dulc",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Pana / dulc"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="panaderias",
            field=models.PositiveIntegerField(
                default=0, verbose_name="panaderías"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="plantas_fre",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Plantas Fre"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="poncheras",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Poncheras"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="restaurant",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Restaurant"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="servicios",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Servicios"
            ),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="taller",
            field=models.PositiveIntegerField(default=0, verbose_name="taller"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="tienda",
            field=models.PositiveIntegerField(default=0, verbose_name="tienda"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="tmc",
            field=models.PositiveIntegerField(default=0, verbose_name="TMC"),
        ),
        migrations.AddField(
            model_name="inmuebles",
            name="top",
            field=models.PositiveIntegerField(default=0, verbose_name="TOP"),
        ),
    ]
