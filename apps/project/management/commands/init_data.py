import traceback

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from apps.project.models import ROL_NAME_ADMIN, ROL_NAME_SECRETARIA, ROL_NAME_DIRECTORA
from apps.project.utils.nomencladores import crear_roles_django_default, crear_empresas_default
from apps.project.utils.util_reporte_d import load_automatic_reports


def creat_first_superuser_and_roles():
    User = get_user_model()
    crear_roles_django_default()
    if User.objects.all().count() == 0:
        user = User.objects.create_superuser(
            username=settings.DJANGO_SUPERUSER_USERNAME,
            email=settings.DJANGO_SUPERUSER_EMAIL,
            first_name=settings.DJANGO_SUPERUSER_FIRST_NAME,
            last_name=settings.DJANGO_SUPERUSER_LAST_NAME,
            password=settings.DJANGO_SUPERUSER_PASSWORD,
        )
        user.groups.add(Group.objects.get(name=ROL_NAME_ADMIN))

def crear_extra_users():
    User = get_user_model()

    if not User.objects.filter(username="secretaria",groups__name=ROL_NAME_SECRETARIA).exists():
        # Crear usuarios para cada rol
        secretaria_user = User.objects.create_user(
            username="secretaria",
            email="secretaria@example.com",
            password="123",
            first_name="Secretaria",
            last_name="General",
        )
        secretaria_group = Group.objects.get(name=ROL_NAME_SECRETARIA)
        secretaria_user.groups.add(secretaria_group)
    if not User.objects.filter(username="directora", groups__name=ROL_NAME_DIRECTORA).exists():
        directora_user = User.objects.create_user(
            username="directora",
            email="directora@example.com",
            password="123",
            first_name="Directora",
            last_name="General",
        )
        directora_group = Group.objects.get(name=ROL_NAME_DIRECTORA)
        directora_user.groups.add(directora_group)

class Command(BaseCommand):
    help = "Create All Tables"

    def handle(self, *args, **kwargs):
        try:
            creat_first_superuser_and_roles()
            load_automatic_reports()
            crear_empresas_default()
            crear_extra_users()

            if settings.LOAD_EXAMPLE_DATA:
                from apps.project.utils.utils_ejemplos import crear_datos_random

                crear_datos_random()

        except Exception:
            print(traceback.format_exc())
