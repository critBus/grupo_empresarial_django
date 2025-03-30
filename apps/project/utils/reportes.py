from typing import List

from apps.project.models import CargoSinCubrir, Cuadro
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
