# Register your models here.
from django.contrib import admin
from django.urls import path, reverse
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin

from .models import (
    AtencionALaFamilia,
    AtencionPoblacion,
    Bancarizacion,
    CapitalHumano,
    CargoSinCubrir,
    Comunales,
    Cuadro,
    CuentasCobrar,
    CuentasPagar,
    Deficiencias,
    Delitos,
    Empresa,
    IndicadorGeneral,
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
    VehiculosCumnales,
)
from .utils.reportes import (
    generar_atencion_poblacion_pdf,
    generar_capital_humano_pdf,
    generar_reporte_atencion_a_la_familia_pdf,
    generar_reporte_bancarizacion_pdf,
    generar_reporte_cuadros_pdf,
    generar_reporte_cuentas_por_cobrar_pdf,
    generar_reporte_cuentas_por_pagar_pdf,
    generar_reporte_deficiencias_pdf,
    generar_reporte_delitos_pdf,
    generar_reporte_indicador_general_del_gm_pdf,
    generar_reporte_informacion_general_pdf,
    generar_reporte_inmuebles_pdf,
    generar_reporte_interruptos_pdf,
    generar_reporte_inversiones_pdf,
    generar_reporte_material_de_construccion_pdf,
    generar_reporte_material_plastico_recilcado_pdf,
    generar_reporte_medicamentos_pdf,
    generar_reporte_perdidas_pdf,
    generar_reporte_perfeccionamiento_de_comercio_y_gastronomia_pdf,
    generar_reporte_plan_de_construccion_pdf,
    generar_reporte_plan_de_mantenimiento_pdf,
    generar_reporte_planes_materia_prima_pdf,
    generar_reporte_planes_recape_pdf,
    generar_reporte_soberania_alimentaria_pdf,
    generar_reporte_transportacion_de_cargas_pdf,
    generar_reporte_transportacion_de_pasajeros_pdf,
    generar_reporte_ueb_perdidas_pdf, generar_reporte_perdidas_alimentaria_pdf,
)


def get_table_row(title, id, lista_de_columnas):
    def table_row(obj):
        # Create a list of formatted strings
        entidades = []
        for field in obj._meta.fields:
            if field.name in lista_de_columnas:
                entidades.append(
                    f'<tr><td style="width: 200px; text-align: right; padding-right: 10px;">{field.verbose_name}</td>'
                    f"<td>{getattr(obj, field.name)}</td></tr>"
                )

        return mark_safe(f"""
            <div class="collapsible-container">
                <button id="collapsible-{id}-{obj.id}" 
                class="collapsible" 
                type="button"
                >
                <i class="fas fa-plus icon"></i>
                
                </button>
                <div class="inmuebles-content">
                    <table 
                    style="border-collapse: collapse; width: 100%;">
                    
                        {"".join(entidades)}
                    </table>
                </div>
            </div>
            <style>
            
                .collapsible {{
                    background-color: #eee;
                    color: #444;
                    cursor: pointer;
                    padding: 18px;
                    width: 100%;
                    border: none;
                    text-align: left;
                    outline: none;
                    font-size: 15px;
                    position: relative;
                }}
                .collapsible .icon {{
                    position: absolute;
                    right: 10px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: #777;
                }}
                .collapsible.active, .collapsible:hover {{
                    background-color: #ddd;
                }}
                .inmuebles-content {{
                    display: none;
                    overflow: hidden;
                    background-color: #f1f1f1;
                }}
                .inmuebles-content.show {{
                    display: block;
                }}
            </style>

            <script>
                var coll = document.getElementById("collapsible-{id}-{obj.id}");
                coll.addEventListener("click", function() {{
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    content.classList.toggle("show");
                    var icon = this.querySelector(".icon");
                    if(icon.classList.contains("fa-plus")){{
                        icon.classList.remove("fa-plus");
                        icon.classList.add("fa-minus");
                    }} else {{
                        icon.classList.remove("fa-minus");
                        icon.classList.add("fa-plus");
                    }}
                }});
            </script>
        """)

    return table_row


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


class CargoSinCubrirInline(admin.TabularInline):
    model = CargoSinCubrir
    extra = 1  # Number of empty forms to display


@admin.register(Cuadro)
class CuadroAdmin(admin.ModelAdmin):
    def get_cargos_sin_cubrir(self, obj):
        cargos = [cargo.cargo for cargo in obj.cargosincubrir_set.all()]
        return mark_safe("<br>\n".join(cargos))

    get_cargos_sin_cubrir.short_description = "Cargos sin Cubrir"

    list_display = ("empresa", "aprobada", "cubierta", "get_cargos_sin_cubrir")
    ordering = (
        "empresa",
        "aprobada",
        "cubierta",
    )
    list_display_links = list(list_display).copy()
    list_filter = (
        "empresa",
        "aprobada",
        "cubierta",
        "cargosincubrir__cargo",
    )
    inlines = [CargoSinCubrirInline]
    actions = [generar_reporte_cuadros_pdf]


@admin.register(CargoSinCubrir)
class CargoSinCubrirAdmin(admin.ModelAdmin):
    list_display = ("cargo", "cuadro")
    list_filter = (
        "cuadro",
        "cargo",
    )
    search_fields = ("cargo",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(AtencionPoblacion)
class AtencionPoblacionAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "quejas",
        "peticiones",
        "denuncias",
        "termino",
    )
    search_fields = ("termino",)
    list_filter = (
        "empresa",
        "quejas",
        "peticiones",
        "denuncias",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_atencion_poblacion_pdf]


@admin.register(CapitalHumano)
class CapitalHumanoAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "plantillaAprobada",
        "plantillaCubierta",
        "mujeres",
    )
    list_filter = (
        "empresa",
        "plantillaAprobada",
        "plantillaCubierta",
        "mujeres",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_capital_humano_pdf]


@admin.register(Interruptos)
class InterruptosAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "total",
        "equiposRotos",
        "faltaPiezas",
        "otrasCausas",
    )
    list_filter = (
        "empresa",
        "total",
        "equiposRotos",
        "faltaPiezas",
        "otrasCausas",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_interruptos_pdf]


@admin.register(Delitos)
class DelitosAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "fecha",
        "municipio",
        "unidad",
        "tipocidad",
        "valorPerdidas",
    )
    list_filter = (
        "empresa",
        "fecha",
        "municipio",
        "tipocidad",
        "denuncia",
        "valorPerdidas",
    )
    search_fields = ("unidad", "productosSustraidos")
    date_hierarchy = "fecha"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_delitos_pdf]


@admin.register(PlanRecape)
class PlanRecapeAdmin(admin.ModelAdmin):
    list_display = ("empresa", "plan", "mes", "anno")
    list_filter = ("empresa", "plan", "mes", "anno")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_planes_recape_pdf]


@admin.register(PlanMateriaPrima)
class PlanMateriaPrimaAdmin(admin.ModelAdmin):
    def get_tipos_materia_prima(self, obj):
        # Create a list of formatted strings
        entidades = []
        for field in obj._meta.fields:
            if field.name in [
                "papel_carton",
                "chatarra_acero",
                "envase_textil",
                "chatarra_aluminio",
                "chatarra_plomo",
                "polietileno",
            ]:
                entidades.append(
                    f'<tr><td style="width: 200px; text-align: right; padding-right: 10px;">{field.verbose_name}</td>'
                    f"<td>{getattr(obj, field.name)}</td></tr>"
                )

        return mark_safe(
            '<table style="border-collapse: collapse; width: 100%;">'
            + '<tr><th style="width: 200px; text-align: right; padding-right: 10px;">Material</th>'
            "<th>Cantidad</th></tr>" + "".join(entidades) + "</table>"
        )

    get_tipos_materia_prima.short_description = "Materias Primas"
    get_tipos_materia_prima.allow_tags = True
    list_display = ("empresa", "anno", "get_tipos_materia_prima")
    list_filter = ("empresa", "anno")
    ordering = ("empresa", "anno")
    list_display_links = ("empresa", "anno")
    actions = [generar_reporte_planes_materia_prima_pdf]


@admin.register(Inmuebles)
class InmueblesAdmin(admin.ModelAdmin):
    def get_tipos_inmuebles(self, obj):
        # Create a list of formatted strings
        entidades = []
        for field in obj._meta.fields:
            if field.name in [
                "loc_oficina",
                "cpl",
                "almacenes",
                "farmacias_opticas",
                "taller",
                "poncheras",
                "plantas_fre",
                "top",
                "nave_pasaje",
                "funeraria",
                "floristeria",
                "banos_p",
                "tienda",
                "base_carga",
                "circulos_s",
                "capillas",
                "comedores",
                "panaderias",
                "dulcerias",
                "pana_dulc",
                "bodegas",
                "minitalleres",
                "fabricas",
                "carnicerias",
                "m_ideal",
                "mais",
                "tmc",
                "bar",
                "c_elaboracion",
                "restaurant",
                "cafeterias",
                "c_nocturno",
                "cabaret",
                "merendero",
                "heladerias",
                "alojamiento",
                "servicios",
                "incinerador",
            ]:
                entidades.append(
                    f'<tr><td style="width: 200px; text-align: right; padding-right: 10px;">{field.verbose_name}</td>'
                    f"<td>{getattr(obj, field.name)}</td></tr>"
                )

        return mark_safe(f"""
            <div class="collapsible-container">
                <button id="collapsible-{obj.id}" 
                class="collapsible" 
                type="button"
                ><i class="fas fa-plus icon"></i>Tipos de Inmuebles</button>
                <div class="inmuebles-content">
                    <table 
                    style="border-collapse: collapse; width: 100%;">
                        <tr><th style="width: 200px; text-align: right; padding-right: 10px;">Material</th>
                        <th>Cantidad</th></tr>
                        {"".join(entidades)}
                    </table>
                </div>
            </div>
            <style>
                .collapsible {{
                    background-color: #eee;
                    color: #444;
                    cursor: pointer;
                    padding: 18px;
                    width: 100%;
                    border: none;
                    text-align: left;
                    outline: none;
                    font-size: 15px;
                    position: relative;
                }}
                .collapsible .icon {{
                    position: absolute;
                    right: 10px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: #777;
                }}
                .collapsible.active, .collapsible:hover {{
                    background-color: #ddd;
                }}
                .inmuebles-content {{
                    display: none;
                    overflow: hidden;
                    background-color: #f1f1f1;
                }}
                .inmuebles-content.show {{
                    display: block;
                }}
            </style>

            <script>
                var coll = document.getElementById("collapsible-{obj.id}");
                coll.addEventListener("click", function() {{
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    content.classList.toggle("show");
                    var icon = this.querySelector(".icon");
                    if(icon.classList.contains("fa-plus")){{
                        icon.classList.remove("fa-plus");
                        icon.classList.add("fa-minus");
                    }} else {{
                        icon.classList.remove("fa-minus");
                        icon.classList.add("fa-plus");
                    }}
                }});
            </script>
        """)

    get_tipos_inmuebles.short_description = "Inmuebles"
    get_tipos_inmuebles.allow_tags = True

    list_display = ("empresa", "get_tipos_inmuebles")
    list_filter = ("empresa",)
    ordering = ("empresa",)
    list_display_links = ("empresa",)
    actions = [generar_reporte_inmuebles_pdf]


@admin.register(PlanDeMantenimiento)
class PlanDeMantenimientoAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "anno",
        "cantidad_de_obras_anual",
        "importe_total_anual",
        "cantidad_de_obras_real",
        "importe_total_real",
    )
    list_filter = (
        "empresa",
        "anno",
        "cantidad_de_obras_anual",
        "importe_total_anual",
        "cantidad_de_obras_real",
        "importe_total_real",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_plan_de_mantenimiento_pdf]


@admin.register(Inversiones)
class InversionesAdmin(admin.ModelAdmin):
    list_display = ("empresa",)
    list_filter = ("empresa",)
    ordering = ("empresa",)
    list_display_links = ("empresa",)
    actions = [generar_reporte_inversiones_pdf]


@admin.register(IndicadorGeneral)
class IndicadorGeneralAdmin(admin.ModelAdmin):
    list_display = ( "plan", "real", "tipo")
    list_filter = ("plan", "real", "tipo")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_perdidas_alimentaria_pdf]


@admin.register(Deficiencias)
class DeficienciasAdmin(admin.ModelAdmin):
    readonly_fields = ("total",)
    list_display = ("empresa", "total", "resueltas", "pendientes")
    list_filter = ("empresa", "total", "resueltas", "pendientes")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_deficiencias_pdf]


@admin.register(UEBperdidas)
class UEBperdidasAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cantidadUEB", "nombre", "municipio")
    list_filter = ("empresa", "cantidadUEB", "municipio")
    search_fields = ("nombre",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_ueb_perdidas_pdf]


@admin.register(CuentasCobrar)
class CuentasCobrarAdmin(admin.ModelAdmin):
    def get_cuentas_por_cobrar_cup(self, obj):
        return get_table_row(
            title="CUP",
            id="cup",
            lista_de_columnas=[
                "inicio_anno",
                "mes_anterior",
                "mes_actual",
                "diferencia_incio_anno",
                "diferencia_mes_anterior",
                "saldo_al_inicio",
                "mes_anterior_vencidas",
                "mes_actual_vencidas",
                "indice_gestion_cobro",
                "ciclo_cobros_dias",
            ],
        )(obj)

    get_cuentas_por_cobrar_cup.short_description = "CUP"
    get_cuentas_por_cobrar_cup.allow_tags = True

    def get_cuentas_por_cobrar_total(self, obj):
        return get_table_row(
            title="Total",
            id="total",
            lista_de_columnas=[
                "por_cobrar_total",
                "vencidas_total",
                "porcentage_total",
            ],
        )(obj)

    get_cuentas_por_cobrar_total.short_description = "Total"
    get_cuentas_por_cobrar_total.allow_tags = True

    def get_cuentas_por_cobrar_a_terceros(self, obj):
        return get_table_row(
            title="Terceros",
            id="Terceros",
            lista_de_columnas=[
                "por_cobrar_a_terceros",
                "vencidas_a_terceros",
                "porcentage_a_terceros",
            ],
        )(obj)

    get_cuentas_por_cobrar_a_terceros.short_description = "Terceros"
    get_cuentas_por_cobrar_a_terceros.allow_tags = True

    def get_cuentas_por_cobrar_admin(self, obj):
        return get_table_row(
            title="Unidad Adminstrativa",
            id="u_a",
            lista_de_columnas=[
                "por_cobrar_u_admin",
                "vencidas_u_admin",
                "porcentage_u_admin",
            ],
        )(obj)

    get_cuentas_por_cobrar_admin.short_description = "Unidad Adminstrativa"
    get_cuentas_por_cobrar_admin.allow_tags = True

    def get_cuentas_por_cobrar_grupo(self, obj):
        return get_table_row(
            title="Grupo",
            id="grupo",
            lista_de_columnas=[
                "por_cobrar_grupo",
                "vencidas_grupo",
                "porcentage_grupo",
            ],
        )(obj)

    get_cuentas_por_cobrar_grupo.short_description = "Grupo"
    get_cuentas_por_cobrar_grupo.allow_tags = True

    list_display = (
        "empresa",
        "get_cuentas_por_cobrar_cup",
        "get_cuentas_por_cobrar_total",
        "get_cuentas_por_cobrar_a_terceros",
        "get_cuentas_por_cobrar_admin",
        "get_cuentas_por_cobrar_grupo",
    )

    list_filter = ("empresa",)
    ordering = ("empresa",)
    list_display_links = ("empresa",)
    actions = [generar_reporte_cuentas_por_cobrar_pdf]


@admin.register(CuentasPagar)
class CuentasPagarAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "inicio_anno",
        "mes_anterior",
        "mes_actual",
        "diferencia_incio_anno",
        "diferencia_mes_anterior",
        "saldo_al_inicio",
        "mes_anterior_vencidas",
        "mes_actual_vencidas",
        "indice_gestion_pago",
        "ciclo_pagos_dias",
        "efectos_por_pagar",
    )
    list_filter = (
        "empresa",
        "inicio_anno",
        "mes_anterior",
        "mes_actual",
        "diferencia_incio_anno",
        "diferencia_mes_anterior",
        "saldo_al_inicio",
        "mes_anterior_vencidas",
        "mes_actual_vencidas",
        "indice_gestion_pago",
        "ciclo_pagos_dias",
        "efectos_por_pagar",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_cuentas_por_pagar_pdf]


@admin.register(MaterialPlasticoReciclado)
class MaterialPlasticoRecicladoAdmin(admin.ModelAdmin):
    list_display = (
        "no_material",
        "materia",
        "unidad_de_medida",
        "plan",
        "real",
    )
    list_filter = (
        "no_material",
        "materia",
        "unidad_de_medida",
        "plan",
        "real",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_material_plastico_recilcado_pdf]


@admin.register(MaterialDeConstruccion)
class MaterialDeConstruccionAdmin(admin.ModelAdmin):
    list_display = (
        "material",
        "unidad_de_medida",
        "plan",
        "real",
    )
    list_filter = (
        "material",
        "unidad_de_medida",
        "plan",
        "real",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_material_de_construccion_pdf]


@admin.register(SoberaniaAlimentaria)
class SoberaniaAlimentariaAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "huertos",
        "canteros",
        "tierras",
    )
    list_filter = (
        "empresa",
        "huertos",
        "canteros",
        "tierras",
    )
    search_fields = ("unidad",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_soberania_alimentaria_pdf]


@admin.register(Bancarizacion)
class BancarizacionAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "establecimientos",
        "total_unidades",
        "solicitadas",
        "aprobados_enzona",
        "aprobados_transfermovil",
        "operaciones_acumuladas",
        "importe_acumulado",
    )
    list_filter = (
        "establecimientos",
        "total_unidades",
        "solicitadas",
        "aprobados_enzona",
        "aprobados_transfermovil",
        "operaciones_acumuladas",
        "importe_acumulado",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_bancarizacion_pdf]


@admin.register(AtencionALaFamilia)
class AtencionALaFamiliaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "total_saf",
        "beneficiados_conciliacion",
        "servicio_diario",
        "almuerzan_unidades",
        "mensajeria",
        "llevan_en_cantina",

    )
    list_filter = (
        "fecha",
        "total_saf",
        "beneficiados_conciliacion",
        "servicio_diario",
        "almuerzan_unidades",
        "mensajeria",
        "llevan_en_cantina",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    date_hierarchy = "fecha"
    actions = [generar_reporte_atencion_a_la_familia_pdf]


@admin.register(PerfeccionamientoComercioGastronomia)
class PerfeccionamientoComercioGastronomiaAdmin(admin.ModelAdmin):
    def get_data(self, obj):
        return get_table_row(
            title="Data",
            id="data",
            lista_de_columnas=[
                "directores_filiales",
                "avalados_mercancias",
                "firma_codigo_conducta",
                "proceso_disponibilidad",
                "mensajeros_vendedores_ambulantes",
                "creacion_emp_filiales",
                "ueb_dl_34",
                "manual_identidad_visual",
                "categorizacion_almacenes",
                "licencias_sanitarias",
                "requisitos_calidad_bodegas",
            ],
        )(obj)

    get_data.short_description = "Data"
    get_data.allow_tags = True

    list_display = ("anno", "estado", "get_data")
    list_filter = (
        "anno",
        "estado",
    )
    ordering = (
        "anno",
        "estado",
    )
    list_display_links = (
        "anno",
        "estado",
    )
    actions = [generar_reporte_perfeccionamiento_de_comercio_y_gastronomia_pdf]


@admin.register(Perdida)
class PerdidaAdmin(admin.ModelAdmin):
    list_display = ("plan", "real", "porciento", "indicador")
    list_filter = ("plan", "real", "porciento", "indicador")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_perdidas_pdf]


@admin.register(TransportacionDePasajeros)
class TransportacionDePasajerosAdmin(admin.ModelAdmin):
    list_display = (
        "aprobadas",
        "real_ejecutadas",
        "porciento",
        "indicador",
    )
    list_filter = (
        "aprobadas",
        "real_ejecutadas",
        "porciento",
        "indicador",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_transportacion_de_pasajeros_pdf]


@admin.register(TransportacionDeCarga)
class TransportacionDeCargaAdmin(admin.ModelAdmin):
    list_display = ("empresa", "plan", "real", "porciento", "carga")
    list_filter = ("empresa", "plan", "real", "porciento", "carga")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_transportacion_de_cargas_pdf]


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "plan",
        "en_falta",
        "porciento_de_afectacion",
        "medicamento",
    )
    list_filter = (
        "empresa",
        "plan",
        "en_falta",
        "porciento_de_afectacion",
        "medicamento",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_medicamentos_pdf]


@admin.register(InformacionGeneral)
class InformacionGeneralAdmin(admin.ModelAdmin):
    list_display = (
        "total",
        "cubiertos",
        "desglosados_gobierno",
        "desglosados_tercero",
        "fluctuacion",
        "dato",
    )
    list_filter = (
        "total",
        "cubiertos",
        "desglosados_gobierno",
        "desglosados_tercero",
        "fluctuacion",
        "dato",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_informacion_general_pdf]


@admin.register(PlanDeConstruccion)
class PlanDeConstruccionAdmin(admin.ModelAdmin):
    list_display = ("plan", "real", "nombre", "donde_se_incumple")
    list_filter = ("plan", "real", "nombre")
    search_fields = ("donde_se_incumple",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_plan_de_construccion_pdf]


@admin.register(IndicadorGeneralGM)
class IndicadorGeneralGMAdmin(admin.ModelAdmin):
    list_display = (
        "empresa",
        "nombre_indicador",
        "unidad_medida",
        "plan_acumulado",
        "real_acumulado",
        "porcentaje_cumplimiento",
    )
    list_filter = (
        "empresa",
        "nombre_indicador",
        "unidad_medida",
        "plan_acumulado",
        "real_acumulado",
        "porcentaje_cumplimiento",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    actions = [generar_reporte_indicador_general_del_gm_pdf]


@admin.register(VehiculosCumnales)
class VehiculosCumnalesAdmin(admin.ModelAdmin):
    list_display = (
        "tipo",
        "cantidad",
        "activo",
        "municipio",
    )
    list_filter = (
        "tipo",
        "cantidad",
        "activo",
        "municipio",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(Comunales)
class ComunalesAdmin(admin.ModelAdmin):
    def custom_button(self, obj):
        """
        Genera un botón HTML para ejecutar un script personalizado.
        """
        # URL a la que se redirigirá cuando se haga clic en el botón
        url = reverse(
            "reporte-comunales", args=[obj.pk]
        )  # Asegúrate de definir esta vista
        return mark_safe(
            f'<a class="button btn btn-high btn-danger mt-2 " href="{url}"><i class="fas fa-file-pdf"></i></a>'
        )

    custom_button.short_description = "Acción"
    list_display = ("plan", "real", "custom_button")
    list_filter = (
        "plan",
        "real",
    )
    ordering = (
        "plan",
        "real",
    )
    list_display_links = (
        "plan",
        "real",
    )
    filter_horizontal = ["vehiculos"]
