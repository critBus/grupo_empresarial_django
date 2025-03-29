"""
Django settings for notas_estudiantes_back_drf project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG").lower() == "true"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOST").split(",")

# CSRF_TRUSTED_ORIGINS = ["https://dir"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Application definition
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "apps.base",
    "apps.users",
    "apps.project",
]
THIRD_APPS = [
    "django.contrib.postgres",
    "django_extensions",
    "rest_framework",
    "django_reportbroD.apps.ReportbrodConfig",
]
PRIORITY_THIRD_APPS = [
    "jazzmin",
]
INSTALLED_APPS = PRIORITY_THIRD_APPS + BASE_APPS + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# crum
MIDDLEWARE += ("crum.CurrentRequestUserMiddleware",)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
USE_SQLITE = str(os.environ.get("USE_SQLITE", default=False)).lower() == "true"
DATABASES = {}
if USE_SQLITE:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
else:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": int(os.environ.get("POSTGRES_PORT")),
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-ar"  #'en-us'

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

AUTH_USER_MODEL = "users.User"

JAZZMIN_SETTINGS = {
    "welcome_sign": "Bienvenido",
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Administración",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Administración",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Administración",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "img/logo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "",
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "icons": {
        "project.empresa": "fas fa-building",  # Icono de edificio para empresas
        "project.cuadro": "fas fa-table",  # Tabla para cuadro
        "project.cargoSinCubrir": "fas fa-user-times",  # Usuario con X para cargos sin cubrir
        "project.atencionPoblacion": "fas fa-hands-helping",  # Manos ayudando para atención a población
        "project.capitalHumano": "fas fa-users",  # Grupo de usuarios para capital humano
        "project.interruptos": "fas fa-stop-circle",  # Círculo de parada para interruptos
        "project.delitos": "fas fa-exclamation-triangle",  # Triángulo de advertencia para delitos
        "project.planRecape": "fas fa-car-side",  # Carro para plan recape
        "project.planMateriaPrima": "fas fa-boxes",  # Cajas para materia prima
        "project.tipoMateriaPrima": "fas fa-box",  # Caja individual para tipo de materia prima
        "project.inmuebles": "fas fa-home",  # Casa para inmuebles
        "project.planDeMantenimiento": "fas fa-tools",  # Herramientas para mantenimiento
        "project.inversiones": "fas fa-chart-line",  # Gráfico de línea para inversiones
        "project.indicadorGeneral": "fas fa-chart-bar",  # Gráfico de barras para indicadores
        "project.deficiencias": "fas fa-exclamation-circle",  # Círculo de exclamación para deficiencias
        "project.uebPerdidas": "fas fa-minus-circle",  # Círculo con menos para UEB perdidas
        "project.cuentasCobrar": "fas fa-hand-holding-usd",  # Mano sosteniendo dinero para cuentas por cobrar
        "project.cuentasPagar": "fas fa-money-bill-wave",  # Billete para cuentas por pagar
    },
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {
            "name": "Plantillas Reportes",
            "url": "/reportbroD",
            "permissions": [
                "reportbroD.view_reportrequest",
                "reportbroD.delete_reportrequest",
                "reportbroD.change_reportrequest",
                "reportbroD.add_reportrequest",
                "reportbroD.view_reportdefinition",
                "reportbroD.delete_reportdefinition",
                "reportbroD.change_reportdefinition",
                "reportbroD.add_reportdefinition",
            ],
        },
    ],
}
JAZZMIN_UI_TWEAKS = {
    "theme": "default",
}

DJANGO_SUPERUSER_USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
DJANGO_SUPERUSER_EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")
DJANGO_SUPERUSER_FIRST_NAME = os.environ.get("DJANGO_SUPERUSER_FIRST_NAME")
DJANGO_SUPERUSER_LAST_NAME = os.environ.get("DJANGO_SUPERUSER_LAST_NAME")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "file_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "info.log",
        },
        "file_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "error.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file_info", "file_error"],
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

LOAD_EXAMPLE_DATA = (
    str(os.environ.get("LOAD_EXAMPLE_DATA", default=False)).lower() == "true"
)
