from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.project.models import Deficiencias


@receiver(pre_save, sender=Deficiencias)
def calcular_total_al_manipular_una_deficiencia(sender, instance, **kwargs):
    instance.total = instance.resueltas + instance.pendientes


# @receiver(user_logged_in)
# def mostrar_notificacion_login(sender, request, user, **kwargs):
#     messages.warning(
#         request,
#         f'¡Tienes tareas pendientes!'
#     )
