from typing import List

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django_reportbroD.models import ReportDefinition, ReportRequest

from apps.project.models import (
    ROL_NAME_ADMIN,
    ROL_NAME_DIRECTORA,
    ROL_NAME_SECRETARIA,
    AtencionALaFamilia,
    AtencionPoblacion,
    Bancarizacion,
    CapitalHumano,
    CargoSinCubrir,
    Comunales,
    Cuadro,
    CuentasCobrar,
    CuentasPagar,
    Deficiencias,
    Delitos,
    Empresa,
    IndicadorGeneral,
    IndicadorGeneralGM,
    InformacionGeneral,
    Inmuebles,
    Interruptos,
    Inversiones,
    MaterialDeConstruccion,
    MaterialPlasticoReciclado,
    Medicamento,
    Perdida,
    PerfeccionamientoComercioGastronomia,
    PlanDeConstruccion,
    PlanDeMantenimiento,
    PlanMateriaPrima,
    PlanRecape,
    SoberaniaAlimentaria,
    TransportacionDeCarga,
    TransportacionDePasajeros,
    UEBperdidas,
    VehiculosCumnales,
)
from config.utils.utils_permission import crear_rol

User = get_user_model()


CONST_ALL_MODELS = [
    Empresa,
    Cuadro,
    CargoSinCubrir,
    AtencionPoblacion,
    CapitalHumano,
    Interruptos,
    Delitos,
    PlanRecape,
    PlanMateriaPrima,
    Inmuebles,
    PlanDeMantenimiento,
    Inversiones,
    IndicadorGeneral,
    Deficiencias,
    UEBperdidas,
    CuentasCobrar,
    CuentasPagar,
    MaterialPlasticoReciclado,
    MaterialDeConstruccion,
    SoberaniaAlimentaria,
    Bancarizacion,
    AtencionALaFamilia,
    PerfeccionamientoComercioGastronomia,
    Perdida,
    TransportacionDePasajeros,
    TransportacionDeCarga,
    Medicamento,
    InformacionGeneral,
    PlanDeConstruccion,
    IndicadorGeneralGM,
    VehiculosCumnales,
    Comunales,
]


def crear_roles_django_default():
    crear_rol(
        lista_modelos=[
            ReportDefinition,
            User,
            Group,
            Permission,
            ReportRequest,
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=ROL_NAME_ADMIN,
    )
    crear_rol(
        lista_modelos=CONST_ALL_MODELS,
        nombre_rol=ROL_NAME_SECRETARIA,
    )
    crear_rol(
        nombre_rol=ROL_NAME_DIRECTORA,
        lista_modelos_solo_update=CONST_ALL_MODELS,
    )

# Nombres de empresas como constantes
NOMBRE_EMPRESA_CONSTRUCCION = "Provincial de Construcción y Mantenimiento"
NOMBRE_EMPRESA_COMUNALES = "Provincial de Comunales"
NOMBRE_EMPRESA_FARMACIAS_OPTICAS = "Provincial de Farmacias y Ópticas"
NOMBRE_EMPRESA_TRANSPORTE = "Provincial de Transporte"
NOMBRE_EMPRESA_SEGURIDAD_PROTECCION = "Provincial de Seguridad y Protección"
NOMBRE_EMPRESA_COMERCIO_GASTRONOMIA = "Provincial de Comercio, Gastronomía y Servicios"
NOMBRE_EMPRESA_MANTENIMIENTO_VIAL = "Provincial de Mantenimiento Vial y Construcción"
NOMBRE_EMPRESA_LOGISTICA = "Provincial de Logística"
NOMBRE_EMPRESA_PRODUCCIONES_VARIAS = "Provincial de Alimentos y Producciones Varias"
NOMBRE_EMPRESA_SERVICIOS_TECNICOS = "Provincial de Servicios Técnicos del Arquitecto de la Comunidad"
NOMBRE_EMPRESA_GRUPO_EMPRESARIAL="Grupo Empresarial"
# Lista constante con todos los nombres de empresas
EMPRESAS_NOMBRES = [
    NOMBRE_EMPRESA_CONSTRUCCION,
    NOMBRE_EMPRESA_COMUNALES,
    NOMBRE_EMPRESA_FARMACIAS_OPTICAS,
    NOMBRE_EMPRESA_TRANSPORTE,
    NOMBRE_EMPRESA_SEGURIDAD_PROTECCION,
    NOMBRE_EMPRESA_COMERCIO_GASTRONOMIA,
    NOMBRE_EMPRESA_MANTENIMIENTO_VIAL,
    NOMBRE_EMPRESA_LOGISTICA,
    NOMBRE_EMPRESA_PRODUCCIONES_VARIAS,
    NOMBRE_EMPRESA_SERVICIOS_TECNICOS,
    NOMBRE_EMPRESA_GRUPO_EMPRESARIAL
]
def crear_empresas_default()->List[Empresa]:
    empresas = []
    for i, nombre in enumerate(EMPRESAS_NOMBRES, 1):
        empresa = Empresa.objects.filter(nombre=nombre).first()
        if not empresa:
            empresa = Empresa.objects.create(codigo=f"EMP{i:03d}", nombre=nombre)
        empresas.append(empresa)
    return empresas