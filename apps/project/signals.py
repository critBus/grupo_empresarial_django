from django.contrib.auth import user_logged_in
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.project.models import CuentasCobrar, CuentasPagar, Deficiencias


@receiver(pre_save, sender=Deficiencias)
def calcular_total_al_manipular_una_deficiencia(sender, instance, **kwargs):
    instance.total = instance.resueltas + instance.pendientes


@receiver(user_logged_in)
def mostrar_notificacion_login(sender, request, user, **kwargs):
    mensajes = []
    for cuenta in CuentasCobrar.objects.all():
        if cuenta.mes_actual >= 10:
            mensajes.append(
                f"En {cuenta.empresa.nombre} existen Cuentas por Cobrar"
            )
    for cuenta in CuentasPagar.objects.all():
        if cuenta.mes_actual >= 10:
            mensajes.append(
                f"En {cuenta.empresa.nombre} existen Cuentas por Pagar"
            )
    # for mensaje in mensajes:
    #     messages.warning(request, mensaje)
