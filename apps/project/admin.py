# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    AtencionPoblacion,
    CapitalHumano,
    CargoSinCubrir,
    Cuadro,
    CuentasCobrar,
    CuentasPagar,
    Deficiencias,
    Delitos,
    Empresa,
    IndicadorGeneral,
    Inmuebles,
    Interruptos,
    Inversiones,
    PlanDeMantenimiento,
    PlanMateriaPrima,
    PlanRecape,
    UEBperdidas,
)
from .utils.reportes import (
    generar_atencion_poblacion_pdf,
    generar_capital_humano_pdf,
    generar_reporte_cuadros_pdf,
    generar_reporte_delitos_pdf,
    generar_reporte_interruptos_pdf,
    generar_reporte_planes_recape_pdf,
)


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
    list_display = ("empresa",  "mes", "anno")
    list_filter = ("empresa", "mes", "anno")
    ordering = ("empresa", )
    list_display_links = list(list_display).copy()



@admin.register(Inmuebles)
class InmueblesAdmin(admin.ModelAdmin):
    list_display = ("empresa", "tipo", "cantidad")
    list_filter = ("empresa", "tipo", "cantidad")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(PlanDeMantenimiento)
class PlanDeMantenimientoAdmin(admin.ModelAdmin):
    list_display = ("empresa", "plan", "real", "porciento", "tipo")
    list_filter = ("empresa", "plan", "real", "porciento", "tipo")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(Inversiones)
class InversionesAdmin(admin.ModelAdmin):
    list_display = ("empresa", "plan", "real", "porciento", "tipo")
    list_filter = ("empresa", "plan", "real", "porciento", "tipo")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(IndicadorGeneral)
class IndicadorGeneralAdmin(admin.ModelAdmin):
    list_display = ("empresa", "plan", "real", "porciento", "tipo")
    list_filter = ("empresa", "plan", "real", "porciento", "tipo")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(Deficiencias)
class DeficienciasAdmin(admin.ModelAdmin):
    list_display = ("empresa", "total", "resueltas", "pendientes")
    list_filter = ("empresa", "total", "resueltas", "pendientes")
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(UEBperdidas)
class UEBperdidasAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cantidadUEB", "nombre", "municipio")
    list_filter = ("empresa", "cantidadUEB", "municipio")
    search_fields = ("nombre",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(CuentasCobrar)
class CuentasCobrarAdmin(admin.ModelAdmin):
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
        "indice_gestion_cloro",
        "ciclo_cobros_dias",
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
        "indice_gestion_cloro",
        "ciclo_cobros_dias",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


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
        "indice_gestion_cloro",
        "ciclo_cobros_dias",
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
        "indice_gestion_cloro",
        "ciclo_cobros_dias",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
