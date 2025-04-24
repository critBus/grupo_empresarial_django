from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.project"
    verbose_name = "Modelos"

    def ready(self):
        from . import signals  # noqa
