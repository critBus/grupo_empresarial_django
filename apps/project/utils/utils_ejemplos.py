import random

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from faker import Faker

from ..models import (
    ROL_NAME_DIRECTORA,
    ROL_NAME_SECRETARIA,
    AtencionPoblacion,
    CapitalHumano,
    CargoSinCubrir,
    Cuadro,
    CuentasCobrar,
    CuentasPagar,
    Deficiencias,
    Delitos,
    Empresa,
    IndicadorGeneral,
    Inmuebles,
    Interruptos,
    Inversiones,
    PlanDeMantenimiento,
    PlanMateriaPrima,
    PlanRecape,
    TipoMateriaPrima,
    UEBperdidas,
)

User = get_user_model()


def crear_datos_random():
    if User.objects.count() > 1 or Empresa.objects.count() > 0:
        return

    fake = Faker("es_ES")

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

    directora_user = User.objects.create_user(
        username="directora",
        email="directora@example.com",
        password="123",
        first_name="Directora",
        last_name="General",
    )
    directora_group = Group.objects.get(name=ROL_NAME_DIRECTORA)
    directora_user.groups.add(directora_group)

    # Lista de empresas predefinidas
    empresas_nombres = [
        "Empresa Provincial de Construcción y Mantenimiento",
        "Empresa Provincial de Comunales",
        "Empresa Provincial de Farmacias y Ópticas",
        "Empresa Provincial de Transporte",
        "Empresa Provincial de Seguridad y Protección",
        "Empresa Provincial de Comercio, Gastronomía y Servicios",
        "Empresa Provincial de Mantenimiento Vial y Construcción",
        "Empresa Provincial de Logística",
        "Empresa Provincial de Alimentos y Producciones Varias",
        "Empresa Provincial de Servicios Técnicos del Arquitecto de la Comunidad",
    ]

    # Crear empresas
    empresas = []
    for i, nombre in enumerate(empresas_nombres, 1):
        empresa = Empresa.objects.create(codigo=f"EMP{i:03d}", nombre=nombre)
        empresas.append(empresa)

    # Tipos comunes para varias entidades
    tipos_mantenimiento = ["Preventivo", "Correctivo", "Predictivo"]
    tipos_inmuebles = ["Oficina", "Almacén", "Taller", "Local Comercial"]
    municipios = [
        "Pinar del Río",
        "San Luis",
        "San Juan",
        "Viñales",
        "La Palma",
    ]
    tipos_materia_prima = ["Tipo A", "Tipo B", "Tipo C", "Tipo D"]

    for empresa in empresas:
        # Crear Cuadro
        cuadro = Cuadro.objects.create(
            empresa=empresa,
            aprobada=random.randint(50, 200),
            cubierta=random.randint(30, 150),
        )

        # Crear CargoSinCubrir
        for _ in range(random.randint(2, 5)):
            CargoSinCubrir.objects.create(cuadro=cuadro, cargo=fake.job())

        # Crear AtencionPoblacion
        AtencionPoblacion.objects.create(
            empresa=empresa,
            quejas=random.randint(0, 50),
            peticiones=random.randint(10, 100),
            termino=random.choice(["Enero", "Febrero", "Marzo"]),
        )

        # Crear CapitalHumano
        plantilla_aprobada = random.randint(100, 500)
        CapitalHumano.objects.create(
            empresa=empresa,
            plantillaAprobada=plantilla_aprobada,
            plantillaCubierta=random.randint(80, plantilla_aprobada),
            mujeres=random.randint(30, 200),
        )

        # Crear Interruptos
        total_interrupts = random.randint(10, 50)
        Interruptos.objects.create(
            empresa=empresa,
            total=total_interrupts,
            equiposRotos=random.randint(5, 20),
            faltaPiezas=random.randint(3, 15),
            otrasCausas=random.randint(2, 15),
        )

        # Crear Delitos (uno por empresa)
        Delitos.objects.create(
            empresa=empresa,
            denuncia=random.randint(1, 100),
            municipio=random.choice(municipios),
            fecha=fake.date_between(start_date="-1y", end_date="today"),
            unidad=fake.company(),
            tipocidad=random.choice(["Robo", "Hurto", "Vandalismo"]),
            productosSustraidos=fake.text(max_nb_chars=50),
            valorPerdidas=round(random.uniform(100, 10000), 2),
            medidasTomadas=random.choice(["Preventiva", "Correctiva", "Legal"]),
        )

        # Crear PlanRecape
        PlanRecape.objects.create(
            empresa=empresa,
            plan=random.randint(1000, 5000),
            mes=random.randint(1, 12),
            anno=2024,
        )

        # Crear PlanMateriaPrima y TipoMateriaPrima
        plan_mp = PlanMateriaPrima.objects.create(
            empresa=empresa, plan=random.randint(1000, 5000)
        )
        for tipo in tipos_materia_prima:
            TipoMateriaPrima.objects.create(
                plan_materia_prima=plan_mp,
                tipo=tipo,
                cantidad=random.randint(100, 1000),
            )

        # Crear Inmuebles (uno por empresa)
        Inmuebles.objects.create(
            empresa=empresa,
            tipo=random.choice(tipos_inmuebles),
            cantidad=random.randint(1, 10),
        )

        # Crear PlanDeMantenimiento
        plan = random.randint(1000, 5000)
        real = random.randint(int(plan * 0.7), plan)
        PlanDeMantenimiento.objects.create(
            empresa=empresa,
            plan=plan,
            real=real,
            porciento=int((real / plan) * 100),
            tipo=random.choice(tipos_mantenimiento),
        )

        # Crear Inversiones
        plan_inv = random.randint(10000, 50000)
        real_inv = random.randint(int(plan_inv * 0.7), plan_inv)
        Inversiones.objects.create(
            empresa=empresa,
            plan=plan_inv,
            real=real_inv,
            porciento=int((real_inv / plan_inv) * 100),
            tipo=random.choice(
                ["Construcción", "Equipamiento", "Infraestructura"]
            ),
        )

        # Crear IndicadorGeneral
        plan_ind = random.randint(1000, 5000)
        real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
        IndicadorGeneral.objects.create(
            empresa=empresa,
            plan=plan_ind,
            real=real_ind,
            porciento=int((real_ind / plan_ind) * 100),
            tipo=random.choice(["Producción", "Servicios", "Ventas"]),
        )

        # Crear Deficiencias (una por empresa)
        total = random.randint(5, 20)
        resueltas = random.randint(0, total)
        Deficiencias.objects.create(
            empresa=empresa,
            total=total,
            resueltas=resueltas,
            pendientes=total - resueltas,
        )

        # Crear UEBperdidas (una por empresa)
        UEBperdidas.objects.create(
            empresa=empresa,
            cantidadUEB=random.randint(1, 5),
            nombre=fake.company(),
            municipio=random.choice(municipios),
        )

        # Crear CuentasCobrar
        valor_base = random.uniform(10000, 50000)
        CuentasCobrar.objects.create(
            empresa=empresa,
            inicio_anno=valor_base,
            mes_anterior=valor_base * 1.1,
            mes_actual=valor_base * 1.2,
            diferencia_incio_anno=valor_base * 0.2,
            diferencia_mes_anterior=valor_base * 0.1,
            saldo_al_inicio=valor_base,
            mes_anterior_vencidas=valor_base * 0.3,
            mes_actual_vencidas=valor_base * 0.25,
            indice_gestion_cloro=random.uniform(0.7, 1.0),
            ciclo_cobros_dias=random.randint(30, 90),
        )

        # Crear CuentasPagar
        valor_base = random.uniform(8000, 40000)
        CuentasPagar.objects.create(
            empresa=empresa,
            inicio_anno=valor_base,
            mes_anterior=valor_base * 1.1,
            mes_actual=valor_base * 1.2,
            diferencia_incio_anno=valor_base * 0.2,
            diferencia_mes_anterior=valor_base * 0.1,
            saldo_al_inicio=valor_base,
            mes_anterior_vencidas=valor_base * 0.3,
            mes_actual_vencidas=valor_base * 0.25,
            indice_gestion_cloro=random.uniform(0.7, 1.0),
            ciclo_cobros_dias=random.randint(30, 90),
        )
