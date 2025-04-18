from django.shortcuts import get_object_or_404

from .models import Comunales
from .utils.reportes import generar_reporte_comunales_vehiculos_pdf


def reporte_vehiculos_view(request, pk):
    comunales = get_object_or_404(Comunales, pk=pk)

    return generar_reporte_comunales_vehiculos_pdf(request, comunales)
