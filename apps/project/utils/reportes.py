from typing import List

from apps.project.models import (
    AtencionALaFamilia,
    AtencionPoblacion,
    Bancarizacion,
    CapitalHumano,
    CargoSinCubrir,
    Cuadro,
    CuentasCobrar,
    CuentasPagar,
    Deficiencias,
    Delitos,
    IndicadorGeneralGM,
    InformacionGeneral,
    Inmuebles,
    Interruptos,
    Inversiones,
    MaterialDeConstruccion,
    MaterialPlasticoReciclado,
    Medicamento,
    Perdida,
    PerfeccionamientoComercioGastronomia,
    PlanDeConstruccion,
    PlanDeMantenimiento,
    PlanMateriaPrima,
    PlanRecape,
    SoberaniaAlimentaria,
    TransportacionDeCarga,
    TransportacionDePasajeros,
    UEBperdidas,
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
    elementos: List[PlanRecape] = queryset

    # Organizar datos por empresa y año
    data_by_empresa_año = {}
    years = set()
    for plan in elementos:
        empresa_id = plan.empresa_id
        year = plan.anno
        years.add(year)
        key = (empresa_id, year)

        if key not in data_by_empresa_año:
            data_by_empresa_año[key] = {
                "empresa": plan.empresa.nombre,
                "año": str(year),
                "meses": {mes: 0 for mes in range(1, 13)},
                "total": 0,
            }

        data_by_empresa_año[key]["meses"][plan.mes] = plan.plan
        data_by_empresa_año[key]["total"] += plan.plan

    # Crear la lista final con el formato requerido
    lista = []
    for empresa_data in data_by_empresa_año.values():
        row = {
            "empresa": empresa_data["empresa"],
            "anno": str(empresa_data["año"]),
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
            "total": str(empresa_data["total"]),
        }
        lista.append(row)

    # Ordenar la lista primero por año y luego por empresa
    lista = sorted(lista, key=lambda x: (int(x["anno"]), x["empresa"]))

    data = {"lista": lista, "mostrar_anno": str(len(years) > 1)}

    return custom_export_report_by_name(
        "Plan de Recape", data, file="reporte_planes_recape"
    )


generar_reporte_planes_recape_pdf.short_description = (
    "Generar Reporte Recape PDF"
)


def generar_reporte_planes_materia_prima_pdf(modeladmin, request, queryset):
    elementos: List[PlanMateriaPrima] = queryset

    # Organizar datos por empresa y año
    years = set()
    lista = []
    for plan in elementos:
        year = plan.anno
        years.add(year)
        lista.append(
            {
                "empresa": plan.empresa.nombre,
                "anno": str(year),
                "papel_carton": str(plan.papel_carton),
                "chatarra_acero": str(plan.chatarra_acero),
                "envase_textil": str(plan.envase_textil),
                "chatarra_aluminio": str(plan.chatarra_aluminio),
                "chatarra_plomo": str(plan.chatarra_plomo),
                "polietileno": str(plan.polietileno),
            }
        )

    # Ordenar la lista primero por año y luego por empresa
    lista = sorted(lista, key=lambda x: (int(x["anno"]), x["empresa"]))

    data = {"lista": lista, "mostrar_anno": len(years) > 1}

    return custom_export_report_by_name(
        "Plan de Materia Prima", data, file="reporte_planes_materia_prima"
    )


generar_reporte_planes_materia_prima_pdf.short_description = (
    "Generar Reporte Materia Prima PDF"
)


def generar_reporte_inmuebles_pdf(modeladmin, request, queryset):
    elementos: List[Inmuebles] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "loc_oficina": str(elemento.loc_oficina),
                "cpl": str(elemento.cpl),
                "almacenes": str(elemento.almacenes),
                "farmacias_opticas": str(elemento.farmacias_opticas),
                "taller": str(elemento.taller),
                "poncheras": str(elemento.poncheras),
                "plantas_fre": str(elemento.plantas_fre),
                "top": str(elemento.top),
                "nave_pasaje": str(elemento.nave_pasaje),
                "funeraria": str(elemento.funeraria),
                "floristeria": str(elemento.floristeria),
                "banos_p": str(elemento.banos_p),
                "tienda": str(elemento.tienda),
                "base_carga": str(elemento.base_carga),
                "circulos_s": str(elemento.circulos_s),
                "capillas": str(elemento.capillas),
                "comedores": str(elemento.comedores),
                "panaderias": str(elemento.panaderias),
                "dulcerias": str(elemento.dulcerias),
                "pana_dulc": str(elemento.pana_dulc),
                "bodegas": str(elemento.bodegas),
                "minitalleres": str(elemento.minitalleres),
                "fabricas": str(elemento.fabricas),
                "carnicerias": str(elemento.carnicerias),
                "m_ideal": str(elemento.m_ideal),
                "mais": str(elemento.mais),
                "tmc": str(elemento.tmc),
                "bar": str(elemento.bar),
                "c_elaboracion": str(elemento.c_elaboracion),
                "restaurant": str(elemento.restaurant),
                "cafeterias": str(elemento.cafeterias),
                "c_nocturno": str(elemento.c_nocturno),
                "cabaret": str(elemento.cabaret),
                "merendero": str(elemento.merendero),
                "heladerias": str(elemento.heladerias),
                "alojamiento": str(elemento.alojamiento),
                "servicios": str(elemento.servicios),
                "incinerador": str(elemento.incinerador),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Red de Inmuebles",
        data,
        file="reporte_inmuebles",
    )


generar_reporte_inmuebles_pdf.short_description = (
    "Generar Reporte Inmuebles PDF"
)


def generar_reporte_plan_de_mantenimiento_pdf(modeladmin, request, queryset):
    elementos: List[PlanDeMantenimiento] = queryset

    # Organizar datos por empresa y año
    years = set()
    lista = []
    for plan in elementos:
        year = plan.anno
        years.add(year)
        lista.append(
            {
                "empresa": plan.empresa.nombre,
                "anno": str(year),
                "cantidad_de_obras_anual": str(plan.cantidad_de_obras_anual),
                "importe_total_anual": str(plan.importe_total_anual),
                "cantidad_de_obras_real": str(plan.cantidad_de_obras_real),
                "importe_total_real": str(plan.importe_total_real),
            }
        )

    # Ordenar la lista primero por año y luego por empresa
    lista = sorted(lista, key=lambda x: (int(x["anno"]), x["empresa"]))

    data = {"lista": lista, "mostrar_anno": len(years) > 1}

    return custom_export_report_by_name(
        "Plan de Mantenimiento", data, file="reporte_planes_mantenimento"
    )


generar_reporte_plan_de_mantenimiento_pdf.short_description = (
    "Generar Reporte Plan Mantenimiento PDF"
)


def generar_reporte_inversiones_pdf():
    elementos: List[Inversiones] = [Inversiones.get_solo()]

    # Organizar datos por empresa y año
    lista = []
    for plan in elementos:
        lista.append(
            {
                "plan_obra": format_float(plan.plan_obra),
                "real_obra": format_float(plan.real_obra),
                "porciento_obra": format_float(plan.porciento_obra),
                "plan_no_nominales": format_float(plan.plan_no_nominales),
                "real_no_nominales": format_float(plan.real_no_nominales),
                "porciento_no_nominales": format_float(
                    plan.porciento_no_nominales
                ),
                "plan_resto": format_float(plan.plan_resto),
                "real_resto": format_float(plan.real_resto),
                "porciento_resto": format_float(plan.porciento_resto),
            }
        )

    data = {
        "lista": lista,
    }

    return custom_export_report_by_name(
        "Inversiones", data, file="reporte_inversiones"
    )


generar_reporte_inversiones_pdf.short_description = (
    "Generar Reporte Inversiones PDF"
)


def generar_reporte_deficiencias_pdf(modeladmin, request, queryset):
    elementos: List[Deficiencias] = queryset
    lista = []
    suma_total = 0
    total_resueltas = 0
    total_pendientes = 0
    for elemento in elementos:
        suma_total += elemento.total
        total_resueltas += elemento.resueltas
        total_pendientes += elemento.pendientes
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "total": str(elemento.total),
                "resueltas": str(elemento.resueltas),
                "pendientes": str(elemento.pendientes),
            }
        )

    data = {
        "lista": lista,
        "suma_total": str(suma_total),
        "total_resueltas": str(total_resueltas),
        "total_pendientes": str(total_pendientes),
    }
    return custom_export_report_by_name(
        "Deficiencias Detectadas por el INRE",
        data,
        file="reporte_deficiencias",
    )


generar_reporte_deficiencias_pdf.short_description = (
    "Generar Reporte Deficiencias Detectadas por el INRE PDF"
)


def generar_reporte_ueb_perdidas_pdf(modeladmin, request, queryset):
    elementos: List[UEBperdidas] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "cantidadUEB": str(elemento.cantidadUEB),
                "nombre": str(elemento.nombre),
                "municipio": str(elemento.municipio),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Pérdidas UEB",
        data,
        file="reporte_perdidas",
    )


generar_reporte_ueb_perdidas_pdf.short_description = (
    "Generar Reporte Pérdidas UEB PDF"
)


def generar_reporte_material_plastico_recilcado_pdf(
    modeladmin, request, queryset
):
    elementos: List[MaterialPlasticoReciclado] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "no": str(elemento.no_material),
                "nombre": str(elemento.materia),
                "unidad_de_medida": str(elemento.unidad_de_medida),
                "plan": str(elemento.plan),
                "real": str(elemento.real),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Material Plástico Reciclado",
        data,
        file="reporte_material_plastico_reciclado",
    )


generar_reporte_material_plastico_recilcado_pdf.short_description = (
    "Generar Reporte Material Plástico Reciclado  PDF"
)


def generar_reporte_material_de_construccion_pdf(modeladmin, request, queryset):
    elementos: List[MaterialDeConstruccion] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "nombre": str(elemento.material),
                "unidad_de_medida": str(elemento.unidad_de_medida),
                "plan": str(elemento.plan),
                "real": str(elemento.real),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Materiales de Construcción",
        data,
        file="reporte_material_de_contruccion",
    )


generar_reporte_material_de_construccion_pdf.short_description = (
    "Generar Reporte Materiales de Construcción  PDF"
)


def generar_reporte_cuentas_por_pagar_pdf(modeladmin, request, queryset):
    elementos: List[CuentasPagar] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "inicio_anno": format_float(elemento.inicio_anno),
                "mes_anterior": format_float(elemento.mes_anterior),
                "mes_actual": format_float(elemento.mes_actual),
                "diferencia_incio_anno": format_float(
                    elemento.diferencia_incio_anno
                ),
                "diferencia_mes_anterior": format_float(
                    elemento.diferencia_mes_anterior
                ),
                "saldo_al_inicio": format_float(elemento.saldo_al_inicio),
                "mes_anterior_vencidas": format_float(
                    elemento.mes_anterior_vencidas
                ),
                "mes_actual_vencidas": format_float(
                    elemento.mes_actual_vencidas
                ),
                "indice_gestion_pago": format_float(
                    elemento.indice_gestion_pago
                ),
                "ciclo_pagos_dias": format_float(elemento.ciclo_pagos_dias),
                "efectos_por_pagar": format_float(elemento.efectos_por_pagar),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Cuentas por Pagar",
        data,
        file="reporte_cuentas_por_pagar",
    )


generar_reporte_cuentas_por_pagar_pdf.short_description = (
    "Generar Reporte Cuentas por Pagar  PDF"
)


def generar_reporte_cuentas_por_cobrar_pdf(modeladmin, request, queryset):
    elementos: List[CuentasCobrar] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "inicio_anno": format_float(elemento.inicio_anno),
                "mes_anterior": format_float(elemento.mes_anterior),
                "mes_actual": format_float(elemento.mes_actual),
                "diferencia_incio_anno": format_float(
                    elemento.diferencia_incio_anno
                ),
                "diferencia_mes_anterior": format_float(
                    elemento.diferencia_mes_anterior
                ),
                "saldo_al_inicio": format_float(elemento.saldo_al_inicio),
                "mes_anterior_vencidas": format_float(
                    elemento.mes_anterior_vencidas
                ),
                "mes_actual_vencidas": format_float(
                    elemento.mes_actual_vencidas
                ),
                "indice_gestion_cobro": format_float(
                    elemento.indice_gestion_cobro
                ),
                "ciclo_cobros_dias": format_float(elemento.ciclo_cobros_dias),
                "por_cobrar_total": format_float(elemento.por_cobrar_total),
                "vencidas_total": format_float(elemento.vencidas_total),
                "porcentage_total": format_float(elemento.porcentage_total),
                "por_cobrar_a_terceros": format_float(
                    elemento.por_cobrar_a_terceros
                ),
                "vencidas_a_terceros": format_float(
                    elemento.vencidas_a_terceros
                ),
                "porcentage_a_terceros": format_float(
                    elemento.porcentage_a_terceros
                ),
                "por_cobrar_u_admin": format_float(elemento.por_cobrar_u_admin),
                "vencidas_u_admin": format_float(elemento.vencidas_u_admin),
                "porcentage_u_admin": format_float(elemento.porcentage_u_admin),
                "por_cobrar_grupo": format_float(elemento.por_cobrar_grupo),
                "vencidas_grupo": format_float(elemento.vencidas_grupo),
                "porcentage_grupo": format_float(elemento.porcentage_grupo),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Cuentas por Cobrar",
        data,
        file="reporte_cuentas_por_cobrar",
    )


generar_reporte_cuentas_por_cobrar_pdf.short_description = (
    "Generar Reporte Cuentas por Cobrar  PDF"
)


def generar_reporte_soberania_alimentaria_pdf(modeladmin, request, queryset):
    elementos: List[SoberaniaAlimentaria] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "unidad": str(elemento.unidad),
                "huertos": format_float(elemento.huertos),
                "canteros": format_float(elemento.canteros),
                "tierras": format_float(elemento.tierras),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Soberanía Alimentaria",
        data,
        file="reporte_material_de_soberiania_alimentaria",
    )


generar_reporte_soberania_alimentaria_pdf.short_description = (
    "Generar Reporte Soberanía Alimentaria  PDF"
)


def generar_reporte_bancarizacion_pdf(modeladmin, request, queryset):
    elementos: List[Bancarizacion] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "establecimientos": str(elemento.establecimientos),
                "total_unidades": str(elemento.total_unidades),
                "solicitadas": str(elemento.solicitadas),
                "aprobados_enzona": str(elemento.aprobados_enzona),
                "aprobados_transfermovil": str(
                    elemento.aprobados_transfermovil
                ),
                "importe_acumulado": format_float(elemento.importe_acumulado),
                "operaciones_acumuladas": str(elemento.operaciones_acumuladas),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Bancarización",
        data,
        file="reporte_material_bancarizacion",
    )


generar_reporte_bancarizacion_pdf.short_description = (
    "Generar Reporte Bancarización  PDF"
)


def generar_reporte_atencion_a_la_familia_pdf(modeladmin, request, queryset):
    elementos: List[AtencionALaFamilia] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "fecha": str(elemento.fecha),
                "total_saf": str(elemento.total_saf),
                "beneficiados_conciliacion": str(
                    elemento.beneficiados_conciliacion
                ),
                "servicio_diario": str(elemento.servicio_diario),
                "almuerzan_unidades": str(elemento.almuerzan_unidades),
                "mensajeria": format_float(elemento.mensajeria),
                "llevan_en_cantina": str(elemento.llevan_en_cantina),
                "total_beneficiarios": str(elemento.total_beneficiarios),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Atención a la Familia",
        data,
        file="reporte_atencion_a_la_familia",
    )


generar_reporte_atencion_a_la_familia_pdf.short_description = (
    "Generar Reporte Atención a la Familia  PDF"
)


def generar_reporte_perfeccionamiento_de_comercio_y_gastronomia_pdf(
    modeladmin, request, queryset
):
    elementos: List[PerfeccionamientoComercioGastronomia] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "anno": str(elemento.anno),
                "directores_filiales": str(elemento.directores_filiales),
                "avalados_mercancias": str(elemento.avalados_mercancias),
                "firma_codigo_conducta": str(elemento.firma_codigo_conducta),
                "proceso_disponibilidad": str(elemento.proceso_disponibilidad),
                "mensajeros_vendedores_ambulantes": str(
                    elemento.mensajeros_vendedores_ambulantes
                ),
                "creacion_emp_filiales": str(elemento.creacion_emp_filiales),
                "ueb_dl_34": str(elemento.ueb_dl_34),
                "manual_identidad_visual": str(
                    elemento.manual_identidad_visual
                ),
                "categorizacion_almacenes": str(
                    elemento.categorizacion_almacenes
                ),
                "licencias_sanitarias": str(elemento.licencias_sanitarias),
                "requisitos_calidad_bodegas": str(
                    elemento.requisitos_calidad_bodegas
                ),
                "estado": str(elemento.estado),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Perfeccionamiento de Comercio y Gastronomía",
        data,
        file="reporte_perfeccionamiento_de_comercio_y_gastronomia",
    )


generar_reporte_perfeccionamiento_de_comercio_y_gastronomia_pdf.short_description = "Generar Reporte Perfeccionamiento de Comercio y Gastronomía  PDF"


def generar_reporte_perdidas_pdf(modeladmin, request, queryset):
    elementos: List[Perdida] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "indicador": str(elemento.indicador),
                "plan": str(elemento.plan),
                "real": str(elemento.real),
                "porciento": str(elemento.porciento),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Perdida",
        data,
        file="reporte_perdidas",
    )


generar_reporte_perdidas_pdf.short_description = "Generar Reporte Perdidas  PDF"


def generar_reporte_transportacion_de_pasajeros_pdf(
    modeladmin, request, queryset
):
    elementos: List[TransportacionDePasajeros] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "indicador": str(elemento.indicador),
                "aprobadas": str(elemento.aprobadas),
                "real_ejecutadas": str(elemento.real_ejecutadas),
                "porciento": str(elemento.porciento),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Transportación de Pasajeros",
        data,
        file="reporte_transportacion_de_pasajeros",
    )


generar_reporte_transportacion_de_pasajeros_pdf.short_description = (
    "Generar Reporte Transportación de Pasajeros PDF"
)


def generar_reporte_transportacion_de_cargas_pdf(modeladmin, request, queryset):
    elementos: List[TransportacionDeCarga] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "carga": str(elemento.carga),
                "plan": str(elemento.plan),
                "real": str(elemento.real),
                "porciento": str(elemento.porciento),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Transportación de Carga",
        data,
        file="reporte_transportacion_de_cargas",
    )


generar_reporte_transportacion_de_cargas_pdf.short_description = (
    "Generar Reporte Transportación de Carga  PDF"
)


def generar_reporte_medicamentos_pdf(modeladmin, request, queryset):
    elementos: List[Medicamento] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "medicamento": str(elemento.medicamento),
                "plan": str(elemento.plan),
                "en_falta": str(elemento.en_falta),
                "porciento_de_afectacion": str(
                    elemento.porciento_de_afectacion
                ),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Medicamentos",
        data,
        file="reporte_medicamentos",
    )


generar_reporte_medicamentos_pdf.short_description = (
    "Generar Reporte Medicamentos PDF"
)


def generar_reporte_informacion_general_pdf(modeladmin, request, queryset):
    elementos: List[InformacionGeneral] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "dato": str(elemento.dato),
                "total": str(elemento.total),
                "cubiertos": str(elemento.cubiertos),
                "desglosados_gobierno": str(elemento.desglosados_gobierno),
                "desglosados_tercero": str(elemento.desglosados_tercero),
                "fluctuacion": format_float(elemento.fluctuacion),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Información General",
        data,
        file="reporte_informacion_general",
    )


generar_reporte_informacion_general_pdf.short_description = (
    "Generar Reporte Información General PDF"
)


def generar_reporte_plan_de_construccion_pdf(modeladmin, request, queryset):
    elementos: List[PlanDeConstruccion] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "nombre": str(elemento.nombre),
                "plan": str(elemento.plan),
                "real": str(elemento.real),
                "donde_se_incumple": str(elemento.donde_se_incumple),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Plan de Construcción",
        data,
        file="reporte_plan_de_construccion",
    )


generar_reporte_plan_de_construccion_pdf.short_description = (
    "Generar Reporte Plan de Construcción PDF"
)


def generar_reporte_indicador_general_del_gm_pdf(modeladmin, request, queryset):
    elementos: List[IndicadorGeneralGM] = queryset
    lista = []
    for elemento in elementos:
        lista.append(
            {
                "empresa": str(elemento.empresa.nombre),
                "nombre_indicador": str(elemento.nombre_indicador),
                "unidad_medida": str(elemento.unidad_medida),
                "plan_acumulado": str(elemento.plan_acumulado),
                "real_acumulado": str(elemento.real_acumulado),
                "porcentaje_cumplimiento": str(
                    elemento.porcentaje_cumplimiento
                ),
            }
        )

    data = {
        "lista": lista,
    }
    return custom_export_report_by_name(
        "Indicador General del GM",
        data,
        file="reporte_indicador_general_del_gm",
    )


generar_reporte_indicador_general_del_gm_pdf.short_description = (
    "Generar Reporte Indicador General del GM PDF"
)
