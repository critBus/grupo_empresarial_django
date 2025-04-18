from django.urls import path

from . import views

urlpatterns = [
    # Otras URLs...
    path(
        "api/project/comunales/vehiculos/reporte/<int:pk>/",
        views.reporte_vehiculos_view,
        name="reporte-comunales",
    ),
]
