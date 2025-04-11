from django.core.management.base import BaseCommand

from apps.project.utils.util_reporte_d import load_report


class Command(BaseCommand):
    help = "Cargar reporte"

    def add_arguments(self, parser):
        # Agregamos un argumento posicional que puede contener espacios
        parser.add_argument(
            "report", nargs="+", type=str, help="Nombre Del Reporte"
        )

    def handle(self, *args, **kwargs):
        # Recibimos el argumento 'texto' como una lista de palabras
        report_name_in_list = kwargs["report"]

        # Unimos las palabras para formar el string completo
        report_name = " ".join(report_name_in_list)
        self.stdout.write(
            self.style.SUCCESS(f"buscando reporte: {report_name}")
        )
        load_report(report_name, force=True)
