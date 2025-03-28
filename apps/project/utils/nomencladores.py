from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django_reportbroD.models import ReportDefinition, ReportRequest

from apps.project.models import (
    ROL_NAME_ADMIN, 
    ROL_NAME_DIRECTORA, 
    ROL_NAME_SECRETARIA,
    Empresa,
    Cuadro,
    CargoSinCubrir,
    AtencionPoblacion,
    CapitalHumano,
    Interruptos,
    Delitos,
    PlanRecape,
    PlanMateriaPrima,
    TipoMateriaPrima,
    Inmuebles,
    PlanDeMantenimiento,
    Inversiones,
    IndicadorGeneral,
    Deficiencias,
    UEBperdidas,
    CuentasCobrar,
    CuentasPagar,
)

from config.utils.utils_permission import crear_rol

User = get_user_model()


def crear_roles_django_default():
    crear_rol(
        lista_modelos=[
            ReportDefinition,
            User,
            Group,
            Permission,
            ReportRequest
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=ROL_NAME_ADMIN,
    )
    crear_rol(
        lista_modelos=[
            Empresa,
            Cuadro,
            CargoSinCubrir,
            AtencionPoblacion,
            CapitalHumano,
            Interruptos,
            Delitos,
            PlanRecape,
            PlanMateriaPrima,
            TipoMateriaPrima,
            Inmuebles,
            PlanDeMantenimiento,
            Inversiones,
            IndicadorGeneral,
            Deficiencias,
            UEBperdidas,
            CuentasCobrar,
            CuentasPagar,
        ],
        nombre_rol=ROL_NAME_SECRETARIA,
    )
    crear_rol(
        nombre_rol=ROL_NAME_DIRECTORA,
        lista_modelos_solo_view=[
            Empresa,
            Cuadro,
            CargoSinCubrir,
            AtencionPoblacion,
            CapitalHumano,
            Interruptos,
            Delitos,
            PlanRecape,
            PlanMateriaPrima,
            TipoMateriaPrima,
            Inmuebles,
            PlanDeMantenimiento,
            Inversiones,
            IndicadorGeneral,
            Deficiencias,
            UEBperdidas,
            CuentasCobrar,
            CuentasPagar,
            ReportRequest,
            ReportDefinition,
        ],
    )
