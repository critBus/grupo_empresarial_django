from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()
ROL_NAME_ADMIN = "admin"
ROL_NAME_SECRETARIA = "secretaria"
ROL_NAME_DIRECTORA = "directora"
MESES_ESPANOL = {
    1: _("Enero"),
    2: _("Febrero"),
    3: _("Marzo"),
    4: _("Abril"),
    5: _("Mayo"),
    6: _("Junio"),
    7: _("Julio"),
    8: _("Agosto"),
    9: _("Septiembre"),
    10: _("Octubre"),
    11: _("Noviembre"),
    12: _("Diciembre"),
}


class Empresa(models.Model):
    codigo = models.CharField(max_length=10, verbose_name="Código", unique=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre


class Cuadro(models.Model):
    aprobada = models.IntegerField(verbose_name="Cantidad Aprobada")
    cubierta = models.IntegerField(verbose_name="Cantidad Cubierta")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Cuadro"
        verbose_name_plural = "Cuadros"

    def __str__(self):
        return f"Cuadro de {self.empresa.nombre}"


class CargoSinCubrir(models.Model):
    cargo = models.CharField(max_length=255, verbose_name="Cargo")
    cuadro = models.ForeignKey(
        Cuadro, on_delete=models.CASCADE, verbose_name="Cuadro"
    )

    class Meta:
        verbose_name = "Cargo sin Cubrir"
        verbose_name_plural = "Cargos sin Cubrir"

    def __str__(self):
        return self.cargo


class AtencionPoblacion(models.Model):
    quejas = models.IntegerField(verbose_name="Quejas")
    denuncias = models.IntegerField(verbose_name="Denuncias", default=0)
    peticiones = models.IntegerField(verbose_name="Peticiones")
    termino = models.CharField(max_length=10, verbose_name="Término")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Atención a la Población"
        verbose_name_plural = "Atenciones a la Población"

    def __str__(self):
        return f"Atención Población - {self.empresa.nombre}"


class CapitalHumano(models.Model):
    plantillaAprobada = models.IntegerField(verbose_name="Plantilla Aprobada")
    plantillaCubierta = models.IntegerField(verbose_name="Plantilla Cubierta")
    mujeres = models.IntegerField(verbose_name="Cantidad de Mujeres")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Capital Humano"
        verbose_name_plural = "Capital Humano"

    def __str__(self):
        return f"Capital Humano - {self.empresa.nombre}"


class Interruptos(models.Model):
    total = models.IntegerField(verbose_name="Total")
    equiposRotos = models.IntegerField(verbose_name="Equipos Rotos")
    faltaPiezas = models.IntegerField(verbose_name="Falta de Piezas")
    otrasCausas = models.IntegerField(verbose_name="Otras Causas")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Interrupto"
        verbose_name_plural = "Interruptos"

    def __str__(self):
        return f"Interruptos - {self.empresa.nombre}"


class Delitos(models.Model):
    no_denuncia = models.IntegerField(
        max_length=10, verbose_name="Código", validators=[MinValueValidator(1)]
    )
    denuncia = models.IntegerField(verbose_name="Número de Denuncia")
    municipio = models.CharField(max_length=50, verbose_name="Municipio")
    fecha = models.DateField(verbose_name="Fecha")
    unidad = models.CharField(max_length=50, verbose_name="Unidad")
    tipocidad = models.CharField(max_length=50, verbose_name="Tipicidad")
    productosSustraidos = models.CharField(
        max_length=255, verbose_name="Productos Sustraídos"
    )
    valorPerdidas = models.FloatField(verbose_name="Valor de Pérdidas")
    medidasTomadas = models.CharField(
        max_length=50, verbose_name="Medidas Tomadas"
    )
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Delito"
        verbose_name_plural = "Delitos"
        unique_together = ["no_denuncia", "empresa"]

    def __str__(self):
        return f"Delito en {self.unidad} - {self.fecha}"


class PlanRecape(models.Model):
    plan = models.IntegerField(verbose_name="Plan")
    mes = models.IntegerField(
        verbose_name="Mes",
        choices=[(k, v) for k, v in MESES_ESPANOL.items()],
        validators=[
            MinValueValidator(1, message="El mes debe estar entre 1 y 12"),
            MaxValueValidator(12, message="El mes debe estar entre 1 y 12"),
        ],
    )
    anno = models.IntegerField(verbose_name="Año")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Plan de Recape"
        verbose_name_plural = "Planes de Recape"
        unique_together = ("mes", "anno", "empresa")

    def __str__(self):
        return f"Plan Recape {MESES_ESPANOL.get(self.mes, self.mes)}/{self.anno} - {self.empresa.nombre}"

    def get_mes_display(self):
        return MESES_ESPANOL.get(self.mes, self.mes)


class PlanMateriaPrima(models.Model):
    anno = models.IntegerField(verbose_name="Año")

    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    papel_carton = models.IntegerField(verbose_name="Papel y Cartón", default=0)
    chatarra_acero = models.IntegerField(
        verbose_name="Chatarra de acero", default=0
    )
    envase_textil = models.IntegerField(verbose_name="Envase Textil", default=0)
    chatarra_aluminio = models.IntegerField(
        verbose_name="Chatarra aluminio", default=0
    )
    chatarra_plomo = models.IntegerField(
        verbose_name="Chatarra Plomo", default=0
    )
    polietileno = models.IntegerField(verbose_name="Polietileno", default=0)

    class Meta:
        verbose_name = "Plan de Materia Prima"
        verbose_name_plural = "Planes de Materia Prima"
        unique_together = ("anno", "empresa")

    def __str__(self):
        return f"Plan Materia Prima - {self.anno} - {self.empresa.nombre}"

    def get_total(self):
        return (
            self.papel_carton
            + self.chatarra_acero
            + self.envase_textil
            + self.chatarra_aluminio
            + self.chatarra_plomo
            + self.polietileno
        )

    def get_materiales(self):
        return [
            ("Papel y Cartón", self.papel_carton),
            ("Chatarra de acero", self.chatarra_acero),
            ("Envase Textil", self.envase_textil),
            ("Chatarra aluminio", self.chatarra_aluminio),
            ("Chatarra Plomo", self.chatarra_plomo),
            ("Polietileno", self.polietileno),
        ]


class Inmuebles(models.Model):
    loc_oficina = models.PositiveIntegerField(
        verbose_name="Loc. oficina", default=0
    )
    cpl = models.PositiveIntegerField(verbose_name="CPL", default=0)
    almacenes = models.PositiveIntegerField(verbose_name="almacenes", default=0)
    farmacias_opticas = models.PositiveIntegerField(
        verbose_name="farmacias y opticas / C. auditivo", default=0
    )
    taller = models.PositiveIntegerField(verbose_name="taller", default=0)
    poncheras = models.PositiveIntegerField(verbose_name="Poncheras", default=0)
    plantas_fre = models.PositiveIntegerField(
        verbose_name="Plantas Fre", default=0
    )
    top = models.PositiveIntegerField(verbose_name="TOP", default=0)
    nave_pasaje = models.PositiveIntegerField(
        verbose_name="nave pasaje", default=0
    )
    funeraria = models.PositiveIntegerField(verbose_name="Funeraria", default=0)
    floristeria = models.PositiveIntegerField(
        verbose_name="Floristería", default=0
    )
    banos_p = models.PositiveIntegerField(verbose_name="baños P", default=0)
    tienda = models.PositiveIntegerField(verbose_name="tienda", default=0)
    base_carga = models.PositiveIntegerField(
        verbose_name="base carga", default=0
    )
    circulos_s = models.PositiveIntegerField(
        verbose_name="Círculos .S", default=0
    )
    capillas = models.PositiveIntegerField(verbose_name="Capillas", default=0)
    comedores = models.PositiveIntegerField(verbose_name="comedores", default=0)
    panaderias = models.PositiveIntegerField(
        verbose_name="panaderías", default=0
    )
    dulcerias = models.PositiveIntegerField(verbose_name="dulcerías", default=0)
    pana_dulc = models.PositiveIntegerField(
        verbose_name="Pana / dulc", default=0
    )
    bodegas = models.PositiveIntegerField(verbose_name="Bodegas", default=0)
    minitalleres = models.PositiveIntegerField(
        verbose_name="minitalleres", default=0
    )
    fabricas = models.PositiveIntegerField(verbose_name="fabricas", default=0)
    carnicerias = models.PositiveIntegerField(
        verbose_name="Carnicerías", default=0
    )
    m_ideal = models.PositiveIntegerField(verbose_name="M. Ideal", default=0)
    mais = models.PositiveIntegerField(verbose_name="MAIS", default=0)
    tmc = models.PositiveIntegerField(verbose_name="TMC", default=0)
    bar = models.PositiveIntegerField(verbose_name="Bar", default=0)
    c_elaboracion = models.PositiveIntegerField(
        verbose_name="C. Elabor.", default=0
    )
    restaurant = models.PositiveIntegerField(
        verbose_name="Restaurant", default=0
    )
    cafeterias = models.PositiveIntegerField(
        verbose_name="Cafeterías", default=0
    )
    c_nocturno = models.PositiveIntegerField(
        verbose_name="C Nocturno", default=0
    )
    cabaret = models.PositiveIntegerField(verbose_name="Cabaret", default=0)
    merendero = models.PositiveIntegerField(verbose_name="Merendero", default=0)
    heladerias = models.PositiveIntegerField(
        verbose_name="Heladerías", default=0
    )
    alojamiento = models.PositiveIntegerField(
        verbose_name="Alojamiento", default=0
    )
    servicios = models.PositiveIntegerField(verbose_name="Servicios", default=0)
    incinerador = models.PositiveIntegerField(
        verbose_name="Incinerador", default=0
    )
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"

    def __str__(self):
        return f"Inmuebles - {self.empresa.nombre}"


class PlanDeMantenimiento(models.Model):
    anno = models.PositiveIntegerField(verbose_name="Año", default=2025)
    cantidad_de_obras_anual = models.PositiveIntegerField(
        verbose_name="Cantidad De Obras Anual", default=0
    )
    importe_total_anual = models.FloatField(
        verbose_name="Importe Total Anual",
        validators=[MinValueValidator(0)],
        default=0,
    )
    cantidad_de_obras_real = models.PositiveIntegerField(
        verbose_name="Cantidad De Obras Real", default=0
    )
    importe_total_real = models.FloatField(
        verbose_name="Importe Total Real",
        validators=[MinValueValidator(0)],
        default=0,
    )
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Plan de Mantenimiento"
        verbose_name_plural = "Planes de Mantenimiento"

    def __str__(self):
        return f"Plan Mantenimiento - {self.empresa.nombre}"


class Inversiones(models.Model):
    plan_obra = models.IntegerField(
        verbose_name="Preparación de obra: Plan", default=0
    )
    real_obra = models.IntegerField(
        verbose_name="Preparación de obra: Real", default=0
    )
    porciento_obra = models.FloatField(
        verbose_name="Preparación de obra: Porcentaje",
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    plan_no_nominales = models.IntegerField(
        verbose_name="Inversiones no nominales: Plan", default=0
    )
    real_no_nominales = models.IntegerField(
        verbose_name="Inversiones no nominales: Real", default=0
    )
    porciento_no_nominales = models.FloatField(
        verbose_name="Inversiones no nominales: Porcentaje",
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    plan_resto = models.IntegerField(
        verbose_name="Resto de inversiones no nominales: Plan", default=0
    )
    real_resto = models.IntegerField(
        verbose_name="Resto de inversiones no nominales: Real", default=0
    )
    porciento_resto = models.FloatField(
        verbose_name="Resto de inversiones no nominales: Porcentaje",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
    )
    empresa = models.OneToOneField(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name="Empresa",
        related_name="inversiones",
    )

    class Meta:
        verbose_name = "Inversión"
        verbose_name_plural = "Inversiones"

    def __str__(self):
        return f"Inversiones - {self.empresa.nombre}"


class IndicadorGeneral(models.Model):
    plan = models.IntegerField(verbose_name="Plan")
    real = models.IntegerField(verbose_name="Real")
    porciento = models.FloatField(
        verbose_name="Porcentaje",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    tipo = models.CharField(max_length=70, verbose_name="Tipo")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Indicador General"
        verbose_name_plural = "Indicadores Generales"

    def __str__(self):
        return f"Indicador General - {self.empresa.nombre}"


class Deficiencias(models.Model):
    total = models.IntegerField(verbose_name="Total")
    resueltas = models.IntegerField(verbose_name="Resueltas")
    pendientes = models.IntegerField(verbose_name="Pendientes")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Deficiencia"
        verbose_name_plural = "Deficiencias"

    def __str__(self):
        return f"Deficiencias - {self.empresa.nombre}"


class UEBperdidas(models.Model):
    cantidadUEB = models.IntegerField(verbose_name="Cantidad de UEB")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    municipio = models.CharField(max_length=255, verbose_name="Municipio")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "UEB Pérdida"
        verbose_name_plural = "UEB Pérdidas"

    def __str__(self):
        return f"{self.nombre} - {self.municipio}"


class CuentasCobrar(models.Model):
    inicio_anno = models.FloatField(
        verbose_name="Inicio de Año",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_anterior = models.FloatField(
        verbose_name="Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_actual = models.FloatField(
        verbose_name="Mes Actual", validators=[MinValueValidator(0)], default=0
    )
    diferencia_incio_anno = models.FloatField(
        verbose_name="Diferencia con Inicio de Año",
        validators=[MinValueValidator(0)],
        default=0,
    )
    diferencia_mes_anterior = models.FloatField(
        verbose_name="Diferencia con Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    saldo_al_inicio = models.FloatField(
        verbose_name="Saldo al Inicio",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_anterior_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_actual_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Actual",
        validators=[MinValueValidator(0)],
        default=0,
    )
    indice_gestion_cobro = models.FloatField(
        verbose_name="Índice Gestión Cobro",
        validators=[MinValueValidator(0)],
        default=0,
    )
    ciclo_cobros_dias = models.FloatField(
        verbose_name="Ciclo de Cobros (Días)",
        validators=[MinValueValidator(0)],
        default=0,
    )
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    por_cobrar_total = models.FloatField(
        verbose_name="Por Cobrar: Total",
        validators=[MinValueValidator(0)],
        default=0,
    )
    vencidas_total = models.FloatField(
        verbose_name="Vencidas: Total",
        validators=[MinValueValidator(0)],
        default=0,
    )
    porcentage_total = models.FloatField(
        verbose_name="%: Total", validators=[MinValueValidator(0)], default=0
    )

    por_cobrar_a_terceros = models.FloatField(
        verbose_name="Por Cobrar: a Terceros",
        validators=[MinValueValidator(0)],
        default=0,
    )
    vencidas_a_terceros = models.FloatField(
        verbose_name="Vencidas: a Terceros",
        validators=[MinValueValidator(0)],
        default=0,
    )
    porcentage_a_terceros = models.FloatField(
        verbose_name="%: a Terceros",
        validators=[MinValueValidator(0)],
        default=0,
    )

    por_cobrar_u_admin = models.FloatField(
        verbose_name="Por Cobrar: Unidad Adminstrativa",
        validators=[MinValueValidator(0)],
        default=0,
    )
    vencidas_u_admin = models.FloatField(
        verbose_name="Vencidas: Unidad Adminstrativa",
        validators=[MinValueValidator(0)],
        default=0,
    )
    porcentage_u_admin = models.FloatField(
        verbose_name="%: Unidad Adminstrativa",
        validators=[MinValueValidator(0)],
        default=0,
    )

    por_cobrar_grupo = models.FloatField(
        verbose_name="Por Cobrar: Grupo",
        validators=[MinValueValidator(0)],
        default=0,
    )
    vencidas_grupo = models.FloatField(
        verbose_name="Vencidas: Grupo",
        validators=[MinValueValidator(0)],
        default=0,
    )
    porcentage_grupo = models.FloatField(
        verbose_name="%: Grupo", validators=[MinValueValidator(0)], default=0
    )

    class Meta:
        verbose_name = "Cuenta por Cobrar"
        verbose_name_plural = "Cuentas por Cobrar"

    def __str__(self):
        return f"Cuentas por Cobrar - {self.empresa.nombre}"


class CuentasPagar(models.Model):
    inicio_anno = models.FloatField(
        verbose_name="Inicio de Año",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_anterior = models.FloatField(
        verbose_name="Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_actual = models.FloatField(
        verbose_name="Mes Actual", validators=[MinValueValidator(0)], default=0
    )
    diferencia_incio_anno = models.FloatField(
        verbose_name="Diferencia con Inicio de Año",
        validators=[MinValueValidator(0)],
        default=0,
    )
    diferencia_mes_anterior = models.FloatField(
        verbose_name="Diferencia con Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    saldo_al_inicio = models.FloatField(
        verbose_name="Saldo al Inicio",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_anterior_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Anterior",
        validators=[MinValueValidator(0)],
        default=0,
    )
    mes_actual_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Actual",
        validators=[MinValueValidator(0)],
        default=0,
    )
    indice_gestion_pago = models.FloatField(
        verbose_name="Índice Gestión Pago",
        validators=[MinValueValidator(0)],
        default=0,
    )
    ciclo_pagos_dias = models.FloatField(
        verbose_name="Ciclo de Cobros (Días)",
        validators=[MinValueValidator(0)],
        default=0,
    )
    efectos_por_pagar = models.FloatField(
        verbose_name="Efectos Por Pagar",
        validators=[MinValueValidator(0)],
        default=0,
    )
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Cuenta por Pagar"
        verbose_name_plural = "Cuentas por Pagar"

    def __str__(self):
        return f"Cuentas por Pagar - {self.empresa.nombre}"


class MaterialPlasticoReciclado(models.Model):
    no_material = models.IntegerField(
        max_length=10, verbose_name="No.", validators=[MinValueValidator(1)]
    )
    materia = models.CharField(max_length=255, verbose_name="Material")
    unidad_de_medida = models.CharField(
        max_length=255, verbose_name="Unidad de Medida"
    )
    plan = models.IntegerField(verbose_name="Plan")
    real = models.IntegerField(verbose_name="Real")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Material Plástico Reciclado"
        verbose_name_plural = "Materiales Plásticos Reciclados"

    def __str__(self):
        return f"{self.materia} - {self.empresa.nombre}"


class MaterialDeConstruccion(models.Model):
    material = models.CharField(max_length=255, verbose_name="Material")
    unidad_de_medida = models.CharField(
        max_length=255, verbose_name="Unidad de Medida"
    )
    plan = models.IntegerField(verbose_name="Plan")
    real = models.IntegerField(verbose_name="Real")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Material de Construcción"
        verbose_name_plural = "Materiales de Construcción"

    def __str__(self):
        return f"{self.material} - {self.empresa.nombre}"


class SoberaniaAlimentaria(models.Model):
    unidad = models.CharField(max_length=50, verbose_name="Unidad")
    huertos = models.PositiveIntegerField(
        verbose_name="Huertos",
        default=0,
    )
    canteros = models.PositiveIntegerField(
        verbose_name="Canteros",
        default=0,
    )
    tierras = models.PositiveIntegerField(
        verbose_name="Tierras",
        default=0,
    )

    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Soberanía Alimentaria"
        verbose_name_plural = "Soberanias Alimentarias"

    def __str__(self):
        return f"Soberanía Alimentaria - {self.empresa.nombre}"


class Bancarizacion(models.Model):
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    establecimientos = models.PositiveIntegerField(
        verbose_name="Establecimientos", default=0
    )
    total_unidades = models.PositiveIntegerField(
        verbose_name="Total Unidades", default=0
    )
    solicitadas = models.PositiveIntegerField(
        verbose_name="Solicitadas", default=0
    )
    aprobados_enzona = models.PositiveIntegerField(
        verbose_name="Aprobados Enzona", default=0
    )
    aprobados_transfermovil = models.PositiveIntegerField(
        verbose_name="Aprobados Transfermóvil", default=0
    )
    operaciones_acumuladas = models.PositiveIntegerField(
        verbose_name="Operaciones Acumuladas", default=0
    )
    importe_acumulado = models.FloatField(
        verbose_name="Importe Acumulado",
        validators=[MinValueValidator(0)],
        default=0,
    )

    class Meta:
        verbose_name = "Bancarización"
        verbose_name_plural = "Bancarizaciones"

    def __str__(self):
        return f"Bancarización - {self.empresa.nombre}"


class AtencionALaFamilia(models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    fecha = models.DateField(verbose_name="Fecha")
    total_saf = models.PositiveIntegerField(
        verbose_name="Total de SAF", default=0
    )
    beneficiados_conciliacion = models.PositiveIntegerField(
        verbose_name="Beneficiados (según conciliación)", default=0
    )
    servicio_diario = models.PositiveIntegerField(
        verbose_name="Servicio Diario", default=0
    )
    almuerzan_unidades = models.PositiveIntegerField(
        verbose_name="Almuerzan Unidades", default=0
    )
    mensajeria = models.PositiveIntegerField(
        verbose_name="Mensajería", default=0
    )
    llevan_en_cantina = models.PositiveIntegerField(
        verbose_name="Llevan en cantina", default=0
    )
    total_beneficiarios = models.PositiveIntegerField(
        verbose_name="Total Beneficiarios", default=0
    )

    class Meta:
        verbose_name = "Atención a la Familia"
        verbose_name_plural = "Atenciones a la familia"
        unique_together = [["empresa", "fecha"]]

    def __str__(self):
        return f"Atención a la Familia - {self.empresa.nombre} ({self.fecha})"


class PerfeccionamientoComercioGastronomia(models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    anno = models.PositiveIntegerField(
        verbose_name="Año",
        help_text="Año al que corresponden los datos",
        default=0,
    )
    directores_filiales = models.PositiveIntegerField(
        verbose_name="Directores E Filiales", default=0
    )
    avalados_mercancias = models.PositiveIntegerField(
        verbose_name="Avalados V Mercancías", default=0
    )
    firma_codigo_conducta = models.PositiveIntegerField(
        verbose_name="Firma del código de conducta", default=0
    )
    proceso_disponibilidad = models.CharField(
        max_length=50,
        verbose_name="Proceso de disponibilidad",
        default="N/P",
        help_text="Especificar si cumple o no ('Cumplido', 'Incumplido', etc.)",
    )
    mensajeros_vendedores_ambulantes = models.PositiveIntegerField(
        verbose_name="Mensajeros y vendedores Ambulantes", default=0
    )
    creacion_emp_filiales = models.PositiveIntegerField(
        verbose_name="Creación Emp. Filiales", default=0
    )
    ueb_dl_34 = models.CharField(
        max_length=50,
        verbose_name="UEB DL-34",
        default="N/P",
        help_text="Especificar si cumple o no ('Cumplido', 'Incumplido', etc.)",
    )
    manual_identidad_visual = models.PositiveIntegerField(
        verbose_name="Manual de Identidad Visual", default=0
    )
    categorizacion_almacenes = models.PositiveIntegerField(
        verbose_name="Categorización de almacenes", default=0
    )
    licencias_sanitarias = models.PositiveIntegerField(
        verbose_name="Licencias Sanitarias", default=0
    )
    requisitos_calidad_bodegas = models.TextField(
        verbose_name="Requisitos de calidad en bodegas",
        blank=True,
        null=True,
        help_text="Detalles sobre el cumplimiento de los requisitos en bodegas",
        default="",
    )
    estado = models.CharField(
        max_length=50,
        verbose_name="Estado",
        choices=[
            ("Cumplido", "Cumplido"),
            ("Incumplido", "Incumplido"),
            ("Pendiente", "Pendiente"),
            ("Con pérdida", "Con pérdida"),
        ],
        default="Pendiente",
    )

    class Meta:
        verbose_name = "Perfeccionamiento de Comercio y Gastronomía"
        verbose_name_plural = "Perfeccionamientos de Comercio y Gastronomía"
        unique_together = [["empresa", "anno"]]

    def __str__(self):
        return f"Indicadores de Comercio y Gastronomía - {self.empresa.nombre} ({self.anno})"


class Perdida(models.Model):
    plan = models.PositiveIntegerField(verbose_name="Plan")
    real = models.PositiveIntegerField(verbose_name="Real")
    porciento = models.FloatField(
        verbose_name="Porcentaje",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    indicador = models.CharField(max_length=256, verbose_name="Indicador")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Perdida"
        verbose_name_plural = "Perdidas"
        unique_together = [["empresa", "indicador"]]

    def __str__(self):
        return f"Perdidas - {self.empresa.nombre} {self.indicador}"


class TransportacionDePasajeros(models.Model):
    aprobadas = models.PositiveIntegerField(verbose_name="Aprobadas")
    real_ejecutadas = models.PositiveIntegerField(
        verbose_name="Real Ejecutadas"
    )
    porciento = models.FloatField(
        verbose_name="Porcentaje",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    indicador = models.CharField(max_length=256, verbose_name="Indicador")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Transportación de Pasajeros"
        verbose_name_plural = "Transportaciones de Pasajeros"
        unique_together = [["empresa", "indicador"]]

    def __str__(self):
        return f"Transportación de Pasajeros - {self.empresa.nombre} {self.indicador}"


class TransportacionDeCarga(models.Model):
    plan = models.PositiveIntegerField(verbose_name="Plan")
    real = models.PositiveIntegerField(verbose_name="Real")
    porciento = models.FloatField(
        verbose_name="Porcentaje",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    carga = models.CharField(max_length=256, verbose_name="Carga")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Transportación de Carga"
        verbose_name_plural = "Transportaciones de carga"
        unique_together = [["empresa", "carga"]]

    def __str__(self):
        return f"Perdidas - {self.empresa.nombre} {self.carga}"


class Medicamento(models.Model):
    plan = models.PositiveIntegerField(verbose_name="Plan")
    en_falta = models.PositiveIntegerField(verbose_name="En Falta")
    porciento_de_afectacion = models.FloatField(
        verbose_name="Porcentaje de Afectación",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    medicamento = models.CharField(max_length=256, verbose_name="Medicamento")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        unique_together = [["empresa", "medicamento"]]

    def __str__(self):
        return f"Medicamento - {self.empresa.nombre} {self.medicamento}"


class InformacionGeneral(models.Model):
    total = models.PositiveIntegerField(verbose_name="Total")
    cubiertos = models.PositiveIntegerField(verbose_name="Cubiertos")
    desglosados_gobierno = models.PositiveIntegerField(
        verbose_name="Desglosados Gobierno"
    )
    desglosados_tercero = models.PositiveIntegerField(
        verbose_name="Desglosados Tercero"
    )
    fluctuacion = models.FloatField(
        verbose_name="Fluctuación",
        validators=[MinValueValidator(0), MaxValueValidator(1)],
    )
    dato = models.CharField(max_length=256, verbose_name="Dato")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Información General"
        verbose_name_plural = "Informaciones Generales"
        unique_together = [["empresa", "dato"]]

    def __str__(self):
        return f"InformacionGeneral - {self.empresa.nombre} {self.dato}"
