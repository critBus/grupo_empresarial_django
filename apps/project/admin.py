# Register your models here.
from django.contrib import admin
from .models import (
    Empresa, Cuadro, CargoSinCubrir, AtencionPoblacion, CapitalHumano,
    Interruptos, Delitos, PlanRecape, PlanMateriaPrima, TipoMateriaPrima,
    Inmuebles, PlanDeMantenimiento, Inversiones, IndicadorGeneral,
    Deficiencias, UEBperdidas, CuentasCobrar, CuentasPagar
)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(Cuadro)
class CuadroAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'aprobada', 'cubierta')

@admin.register(CargoSinCubrir)
class CargoSinCubrirAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'cuadro')
    list_filter = ('cuadro',)

@admin.register(AtencionPoblacion)
class AtencionPoblacionAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'quejas', 'peticiones', 'termino')

@admin.register(CapitalHumano)
class CapitalHumanoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plantillaAprobada', 'plantillaCubierta', 'mujeres')

@admin.register(Interruptos)
class InterruptosAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'total', 'equiposRotos', 'faltaPiezas', 'otrasCausas')

@admin.register(Delitos)
class DelitosAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'fecha', 'municipio', 'unidad', 'tipocidad', 'valorPerdidas')
    list_filter = ('fecha', 'municipio', 'tipocidad')
    search_fields = ('unidad', 'productosSustraidos')

@admin.register(PlanRecape)
class PlanRecapeAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plan', 'mes', 'anno')
    list_filter = ('mes', 'anno')

@admin.register(PlanMateriaPrima)
class PlanMateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plan')

@admin.register(TipoMateriaPrima)
class TipoMateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('plan_materia_prima', 'tipo', 'cantidad')
    list_filter = ('tipo',)

@admin.register(Inmuebles)
class InmueblesAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'tipo', 'cantidad')
    list_filter = ('tipo',)

@admin.register(PlanDeMantenimiento)
class PlanDeMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plan', 'real', 'porciento', 'tipo')
    list_filter = ('tipo',)

@admin.register(Inversiones)
class InversionesAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plan', 'real', 'porciento', 'tipo')
    list_filter = ('tipo',)

@admin.register(IndicadorGeneral)
class IndicadorGeneralAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'plan', 'real', 'porciento', 'tipo')
    list_filter = ('tipo',)

@admin.register(Deficiencias)
class DeficienciasAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'total', 'resueltas', 'pendientes')

@admin.register(UEBperdidas)
class UEBperdidasAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cantidadUEB', 'nombre', 'municipio')
    list_filter = ('municipio',)
    search_fields = ('nombre', 'municipio')

@admin.register(CuentasCobrar)
class CuentasCobrarAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'inicio_anno', 'mes_anterior', 'mes_actual', 'diferencia_incio_anno', 
                   'diferencia_mes_anterior', 'saldo_al_inicio', 'mes_anterior_vencidas', 
                   'mes_actual_vencidas', 'indice_gestion_cloro', 'ciclo_cobros_dias')

@admin.register(CuentasPagar)
class CuentasPagarAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'inicio_anno', 'mes_anterior', 'mes_actual', 'diferencia_incio_anno', 
                   'diferencia_mes_anterior', 'saldo_al_inicio', 'mes_anterior_vencidas', 
                   'mes_actual_vencidas', 'indice_gestion_cloro', 'ciclo_cobros_dias')
