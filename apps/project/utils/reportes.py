from typing import List

from apps.project.models import (
    AtencionPoblacion,
    CapitalHumano,
    CargoSinCubrir,
    Cuadro,
    Delitos,
    Interruptos,
    PlanRecape,
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


def generar_reporte_delitos_pdf(modeladmin, request, queryset):
    elementos: List[Delitos] = queryset.order_by("empresa", "-fecha")
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "no": str(elemento.empresa.codigo),
                "empresa": str(elemento.empresa.nombre),
                "municipios": str(elemento.municipio),
                "unidad": str(elemento.unidad),
                "tipicidad": str(elemento.tipocidad),
                "productos_sustraidos": str(elemento.productosSustraidos),
                "valor_perdidas": format_float(elemento.valorPerdidas),
                "medidas_tomadas": str(elemento.medidasTomadas),
                "no_denuncia": str(elemento.no_denuncia),
                "fecha": str(elemento.fecha),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Delitos",
        data,
        file="reporte_delitos",
    )


generar_reporte_delitos_pdf.short_description = "Generar Reporte Delitos PDF"


def generar_reporte_planes_recape_pdf(modeladmin, request, queryset):
    elementos: List[PlanRecape] = queryset#.order_by("empresa", "anno", "mes")
    
    # Organizar datos por empresa y año
    data_by_empresa = {}
    years = set()
    
    for plan in elementos:
        empresa_id = plan.empresa_id
        year = plan.anno
        years.add(year)
        
        if empresa_id not in data_by_empresa:
            data_by_empresa[empresa_id] = {
                "empresa": plan.empresa.nombre,
                "meses": {mes: 0 for mes in range(1, 13)},
                "total": 0
            }
        
        data_by_empresa[empresa_id]["meses"][plan.mes] = plan.plan
        data_by_empresa[empresa_id]["total"] += plan.plan
    
    # Crear la lista final con el formato requerido
    lista = []
    for empresa_data in data_by_empresa.values():
        row = {
            "empresa": empresa_data["empresa"],
            "enero_1": str(empresa_data["meses"][1]),
            "febrero_2": str(empresa_data["meses"][2]),
            "marzo_3": str(empresa_data["meses"][3]),
            "abril_4": str(empresa_data["meses"][4]),
            "mayo_5": str(empresa_data["meses"][5]),
            "junio_6": str(empresa_data["meses"][6]),
            "julio_7": str(empresa_data["meses"][7]),
            "agosto_8": str(empresa_data["meses"][8]),
            "septiembre_9": str(empresa_data["meses"][9]),
            "octubre_10": str(empresa_data["meses"][10]),
            "noviembre_11": str(empresa_data["meses"][11]),
            "diciembre_12": str(empresa_data["meses"][12]),
            "total": str(empresa_data["total"])
        }
        lista.append(row)
    
    data = {
        "lista": lista,
        "mostrar_anno": len(years) > 1
    }
    
    return custom_export_report_by_name(
        "Plan de Recape",
        data,
        file="reporte_planes_recape"
    )


generar_reporte_planes_recape_pdf.short_description = "Generar Reporte Recape PDF"
