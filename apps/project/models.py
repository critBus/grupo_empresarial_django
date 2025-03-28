from typing import Dict, List

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()
ROL_NAME_ADMIN="admin"

class Empresa(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Cuadro(models.Model):
    aprobada = models.IntegerField()
    cubierta = models.IntegerField()
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cuadro de {self.empresa.nombre}"

class CargoSinCubrir(models.Model):
    cargo = models.CharField(max_length=255)
    cuadro = models.ForeignKey(Cuadro, on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo

class AtencionPoblacion(models.Model):
    quejas = models.IntegerField()
    peticiones = models.IntegerField()
    termino = models.CharField(max_length=10)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atención Población - {self.empresa.nombre}"

class CapitalHumano(models.Model):
    plantillaAprobada = models.IntegerField()
    plantillaCubierta = models.IntegerField()
    mujeres = models.IntegerField()
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Capital Humano - {self.empresa.nombre}"

class Interruptos(models.Model):
    total = models.IntegerField()
    equiposRotos = models.IntegerField()
    faltaPiezas = models.IntegerField()
    otrasCausas = models.IntegerField()
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Interruptos - {self.empresa.nombre}"

class Delitos(models.Model):
    denuncia = models.IntegerField()
    municipio = models.CharField(max_length=50)
    fecha = models.DateField()
    unidad = models.CharField(max_length=50)
    tipocidad = models.CharField(max_length=50)
    productosSustraidos = models.CharField(max_length=255)
    valorPerdidas = models.FloatField()
    medidasTomadas = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Delito en {self.unidad} - {self.fecha}"

class PlanRecape(models.Model):
    plan = models.IntegerField()
    mes = models.IntegerField()
    anno = models.IntegerField()
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plan Recape {self.mes}/{self.anno} - {self.empresa.nombre}"

class PlanMateriaPrima(models.Model):
    plan = models.IntegerField()
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plan Materia Prima - {self.empresa.nombre}"

class TipoMateriaPrima(models.Model):
    plan_materia_prima = models.ForeignKey(PlanMateriaPrima, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.cantidad}"

class Inmuebles(models.Model):
    tipo = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.empresa.nombre}"

class PlanDeMantenimiento(models.Model):
    plan = models.IntegerField()
    real = models.IntegerField()
    porciento = models.IntegerField()
    tipo = models.CharField(max_length=70)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plan Mantenimiento - {self.empresa.nombre}"

class Inversiones(models.Model):
    plan = models.IntegerField()
    real = models.IntegerField()
    porciento = models.IntegerField()
    tipo = models.CharField(max_length=70)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name='inversiones')

    def __str__(self):
        return f"Inversiones - {self.empresa.nombre}"

class IndicadorGeneral(models.Model):
    plan = models.IntegerField()
    real = models.IntegerField()
    porciento = models.IntegerField()
    tipo = models.CharField(max_length=70)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Indicador General - {self.empresa.nombre}"

class Deficiencias(models.Model):
    total = models.IntegerField()
    resueltas = models.IntegerField()
    pendientes = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Deficiencias - {self.empresa.nombre}"

class UEBperdidas(models.Model):
    cantidadUEB = models.IntegerField()
    nombre = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.municipio}"

class CuentasCobrar(models.Model):
    cantidad = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cuentas por Cobrar - {self.empresa.nombre}"

class CuentasPagar(models.Model):
    cantidad = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cuentas por Pagar - {self.empresa.nombre}"