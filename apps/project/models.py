from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()
ROL_NAME_ADMIN = "admin"
ROL_NAME_SECRETARIA = "secretaria"
ROL_NAME_DIRECTORA = "directora"
MESES_ESPANOL = {
        1: _('Enero'),
        2: _('Febrero'),
        3: _('Marzo'),
        4: _('Abril'),
        5: _('Mayo'),
        6: _('Junio'),
        7: _('Julio'),
        8: _('Agosto'),
        9: _('Septiembre'),
        10: _('Octubre'),
        11: _('Noviembre'),
        12: _('Diciembre'),
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
            MaxValueValidator(12, message="El mes debe estar entre 1 y 12")
        ]
    )
    anno = models.IntegerField(verbose_name="Año")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Plan de Recape"
        verbose_name_plural = "Planes de Recape"
        unique_together = ('mes', 'anno', 'empresa')

    def __str__(self):
        return f"Plan Recape {MESES_ESPANOL.get(self.mes, self.mes)}/{self.anno} - {self.empresa.nombre}"

    def get_mes_display(self):
        return MESES_ESPANOL.get(self.mes, self.mes)


class PlanMateriaPrima(models.Model):
    anno = models.IntegerField(verbose_name="Año")
    
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    
    papel_carton = models.IntegerField(
        verbose_name="Papel y Cartón",
        default=0
    )
    chatarra_acero = models.IntegerField(
        verbose_name="Chatarra de acero",
        default=0
    )
    envase_textil = models.IntegerField(
        verbose_name="Envase Textil",
        default=0
    )
    chatarra_aluminio = models.IntegerField(
        verbose_name="Chatarra aluminio",
        default=0
    )
    chatarra_plomo = models.IntegerField(
        verbose_name="Chatarra Plomo",
        default=0
    )
    polietileno = models.IntegerField(
        verbose_name="Polietileno",
        default=0
    )

    class Meta:
        verbose_name = "Plan de Materia Prima"
        verbose_name_plural = "Planes de Materia Prima"
        unique_together = ( 'anno', 'empresa')

    def __str__(self):
        return f"Plan Materia Prima - {self.anno} - {self.empresa.nombre}"

    

    def get_total(self):
        return (
            self.papel_carton +
            self.chatarra_acero +
            self.envase_textil +
            self.chatarra_aluminio +
            self.chatarra_plomo +
            self.polietileno
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
    tipo = models.CharField(max_length=255, verbose_name="Tipo")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Inmueble"
        verbose_name_plural = "Inmuebles"

    def __str__(self):
        return f"{self.tipo} - {self.empresa.nombre}"


class PlanDeMantenimiento(models.Model):
    plan = models.IntegerField(verbose_name="Plan")
    real = models.IntegerField(verbose_name="Real")
    porciento = models.IntegerField(verbose_name="Porcentaje")
    tipo = models.CharField(max_length=70, verbose_name="Tipo")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Plan de Mantenimiento"
        verbose_name_plural = "Planes de Mantenimiento"

    def __str__(self):
        return f"Plan Mantenimiento - {self.empresa.nombre}"


class Inversiones(models.Model):
    plan = models.IntegerField(verbose_name="Plan")
    real = models.IntegerField(verbose_name="Real")
    porciento = models.IntegerField(verbose_name="Porcentaje")
    tipo = models.CharField(max_length=70, verbose_name="Tipo")
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
    porciento = models.IntegerField(verbose_name="Porcentaje")
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

    def clean(self):
        super().clean()
        # Validar que el total sea igual a resueltas + pendientes
        if self.total != (self.resueltas + self.pendientes):
            raise ValidationError(
                "El total debe ser igual a la suma de resueltas y pendientes."
            )


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
    inicio_anno = models.FloatField(verbose_name="Inicio de Año")
    mes_anterior = models.FloatField(verbose_name="Mes Anterior")
    mes_actual = models.FloatField(verbose_name="Mes Actual")
    diferencia_incio_anno = models.FloatField(
        verbose_name="Diferencia con Inicio de Año"
    )
    diferencia_mes_anterior = models.FloatField(
        verbose_name="Diferencia con Mes Anterior"
    )
    saldo_al_inicio = models.FloatField(verbose_name="Saldo al Inicio")
    mes_anterior_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Anterior"
    )
    mes_actual_vencidas = models.FloatField(verbose_name="Vencidas Mes Actual")
    indice_gestion_cloro = models.FloatField(
        verbose_name="Índice Gestión Cloro"
    )
    ciclo_cobros_dias = models.FloatField(verbose_name="Ciclo de Cobros (Días)")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Cuenta por Cobrar"
        verbose_name_plural = "Cuentas por Cobrar"

    def __str__(self):
        return f"Cuentas por Cobrar - {self.empresa.nombre}"


class CuentasPagar(models.Model):
    inicio_anno = models.FloatField(verbose_name="Inicio de Año")
    mes_anterior = models.FloatField(verbose_name="Mes Anterior")
    mes_actual = models.FloatField(verbose_name="Mes Actual")
    diferencia_incio_anno = models.FloatField(
        verbose_name="Diferencia con Inicio de Año"
    )
    diferencia_mes_anterior = models.FloatField(
        verbose_name="Diferencia con Mes Anterior"
    )
    saldo_al_inicio = models.FloatField(verbose_name="Saldo al Inicio")
    mes_anterior_vencidas = models.FloatField(
        verbose_name="Vencidas Mes Anterior"
    )
    mes_actual_vencidas = models.FloatField(verbose_name="Vencidas Mes Actual")
    indice_gestion_cloro = models.FloatField(
        verbose_name="Índice Gestión Cloro"
    )
    ciclo_cobros_dias = models.FloatField(verbose_name="Ciclo de Cobros (Días)")
    empresa = models.OneToOneField(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )

    class Meta:
        verbose_name = "Cuenta por Pagar"
        verbose_name_plural = "Cuentas por Pagar"

    def __str__(self):
        return f"Cuentas por Pagar - {self.empresa.nombre}"
