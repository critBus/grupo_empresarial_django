from typing import List

from apps.project.models import (
    AtencionPoblacion,
    CapitalHumano,
    CargoSinCubrir,
    Cuadro,
    Interruptos,
)
from apps.project.utils.util_reporte_d import custom_export_report_by_name


def format_float(value):
    if value is None:
        return "-"
    else:
        return f"{value:.2f}"


def generar_reporte_cuadros_pdf(modeladmin, request, queryset):
    elementos: List[Cuadro] = queryset
    lista = []
    for elemento in elementos:
        cargos_sin_cubrir = []
        for cargo in CargoSinCubrir.objects.filter(cuadro=elemento):
            cargos_sin_cubrir.append(f"{cargo.cargo}")
        lista.append(
            {
                "no": str(elemento.empresa.codigo),
                "empresa": str(elemento.empresa.nombre),
                "aprobada": str(elemento.aprobada),
                "cubierta": str(elemento.cubierta),
                "cargos_sin_cubrir": "\n".join(cargos_sin_cubrir),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Cuadros",
        data,
        file="reporte_cuadros",
    )


generar_reporte_cuadros_pdf.short_description = "Generar Reporte Cuadros PDF"


def generar_atencion_poblacion_pdf(modeladmin, request, queryset):
    elementos: List[AtencionPoblacion] = queryset
    lista = []
    total_quejas = 0
    total_denuncias = 0
    total_total_de_casos = 0
    for elemento in elementos:
        total_quejas += elemento.quejas
        total_denuncias += elemento.denuncias
        total_total_de_casos += elemento.quejas + elemento.denuncias
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "quejas": str(elemento.quejas),
                "denuncias": str(elemento.denuncias),
                "total_de_casos": str(elemento.quejas + elemento.denuncias),
            }
        )

    data = {
        "lista": lista,
        "total_quejas": str(total_quejas),
        "total_denuncias": str(total_denuncias),
        "total_de_total_casos": str(total_total_de_casos),
    }
    return custom_export_report_by_name(
        "Atencion a la Poblacion",
        data,
        file="reporte_atencion_poblacion",
    )


generar_atencion_poblacion_pdf.short_description = (
    "Generar Reporte Atencion a la Poblacion PDF"
)


def generar_capital_humano_pdf(modeladmin, request, queryset):
    elementos: List[CapitalHumano] = queryset
    lista = []
    total_aprobadas = 0
    total_cubierta = 0
    total_mujeres = 0
    for elemento in elementos:
        total_aprobadas += elemento.plantillaAprobada
        total_cubierta += elemento.plantillaCubierta
        total_mujeres += elemento.mujeres
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "aprobada": str(elemento.plantillaAprobada),
                "cubierta": str(elemento.plantillaCubierta),
                "mujeres": str(elemento.mujeres),
            }
        )

    data = {
        "lista": lista,
        "total_mujeres": str(total_mujeres),
        "total_aprobadas": str(total_aprobadas),
        "ttoal_cubiertas": str(total_cubierta),
    }
    return custom_export_report_by_name(
        "Capital Humano",
        data,
        file="reporte_capital_humano",
    )


generar_capital_humano_pdf.short_description = (
    "Generar Reporte Capital Humano PDF"
)


def generar_reporte_interruptos_pdf(modeladmin, request, queryset):
    elementos: List[Interruptos] = queryset
    lista = []
    total_interruptos = 0
    total_roturas = 0
    total_piezas = 0
    total_otras_causas = 0
    for elemento in elementos:
        total_interruptos += elemento.total
        total_roturas += elemento.equiposRotos
        total_piezas += elemento.faltaPiezas
        total_otras_causas += elemento.otrasCausas
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "interruptos": str(elemento.total),
                "roturas": str(elemento.equiposRotos),
                "piezas": str(elemento.faltaPiezas),
                "otras_causas": str(elemento.otrasCausas),
            }
        )

    data = {
        "lista": lista,
        "total_interruptos": str(total_interruptos),
        "total_roturas": str(total_roturas),
        "total_piezas": str(total_piezas),
        "total_otras_causas": str(total_otras_causas),
    }
    return custom_export_report_by_name(
        "Cantidad de Interruptos",
        data,
        file="reporte_interruptos",
    )


generar_reporte_interruptos_pdf.short_description = (
    "Generar Reporte Interruptos PDF"
)
