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
    MaterialPlasticoReciclado,
    PlanDeMantenimiento,
    PlanMateriaPrima,
    PlanRecape,
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
    nombre_empresa_producciones_varias = "Empresa de Producciones Varias"
    empresas_nombres = [
        "Provincial de Construcción y Mantenimiento",
        "Provincial de Comunales",
        "Provincial de Farmacias y Ópticas",
        "Provincial de Transporte",
        "Provincial de Seguridad y Protección",
        "Provincial de Comercio, Gastronomía y Servicios",
        "Provincial de Mantenimiento Vial y Construcción",
        "Provincial de Logística",
        "Provincial de Alimentos y Producciones Varias",
        "Provincial de Servicios Técnicos del Arquitecto de la Comunidad",
        nombre_empresa_producciones_varias,
    ]

    # Crear empresas
    empresas = []
    for i, nombre in enumerate(empresas_nombres, 1):
        empresa = Empresa.objects.create(codigo=f"EMP{i:03d}", nombre=nombre)
        empresas.append(empresa)

    # Tipos comunes para varias entidades
    municipios = [
        "Pinar del Río",
        "San Luis",
        "San Juan",
        "Viñales",
        "La Palma",
    ]

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
            denuncias=random.randint(10, 100),
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

        for i in range(random.randint(1, 10)):
            no_denuncia = random.randint(1, 1000)
            if not Delitos.objects.filter(
                no_denuncia=no_denuncia, empresa=empresa
            ).exists():
                # Crear Delitos
                Delitos.objects.create(
                    no_denuncia=no_denuncia,
                    empresa=empresa,
                    denuncia=random.randint(1, 100),
                    municipio=random.choice(municipios),
                    fecha=fake.date_between(start_date="-1y", end_date="today"),
                    unidad=fake.company(),
                    tipocidad=random.choice(["Robo", "Hurto", "Vandalismo"]),
                    productosSustraidos=fake.text(max_nb_chars=50),
                    valorPerdidas=round(random.uniform(100, 10000), 2),
                    medidasTomadas=random.choice(
                        ["Preventiva", "Correctiva", "Legal"]
                    ),
                )

        # Crear PlanRecape
        # Generar planes para los últimos 3 años
        current_year = 2024
        for year in range(current_year - 2, current_year + 1):
            # Para cada mes del año
            for month in range(1, 13):
                PlanRecape.objects.create(
                    empresa=empresa,
                    plan=random.randint(1000, 5000),
                    mes=month,
                    anno=year,
                )

        # Crear PlanMateriaPrima
        current_year = 2024
        for year in range(current_year - 2, current_year + 1):
            PlanMateriaPrima.objects.create(
                empresa=empresa,
                anno=year,
                papel_carton=random.randint(0, 1000),
                chatarra_acero=random.randint(0, 1000),
                envase_textil=random.randint(0, 1000),
                chatarra_aluminio=random.randint(0, 1000),
                chatarra_plomo=random.randint(0, 1000),
                polietileno=random.randint(0, 1000),
            )
        if empresa.nombre == nombre_empresa_producciones_varias:
            # Crear MaterialPlasticoReciclado para Producciones Varias
            materiales = [
                r"Mangueras plásticas flexibles ½\"",
                r"Mangueras plásticas flexibles ¾\"",
                r"Mangueras plásticas flexibles 1\"",
                r"Tubos plásticos eléctricos ½\"",
                r"Tubos plásticos eléctricos ¾\"",
                r"Tubos plásticos eléctricos 1\"",
                "Codo",
                "Y",
                "Unión (Nudo)",
                r"Conexiones plásticas eléctricas ¾\"",
                r"Conexiones plásticas eléctricas 1\"",
                r"Conexiones plásticas hidráulicas ¾\"",
                "Llaves plásticas para agua",
                r"Cajas plásticas eléctricas de 2\" x 4\"",
                r"Cajas plásticas eléctricas de 4\" x 4\"",
            ]

            # Crear registros para cada material
            for i, material in enumerate(materiales, 1):
                # Asignar unidad de medida basada en el tipo de material
                unidad = (
                    "Km"
                    if "Mangueras" in material or "Tubos" in material
                    else "Mu"
                )

                MaterialPlasticoReciclado.objects.create(
                    empresa=empresa,
                    no_material=i,
                    materia=material,
                    unidad_de_medida=unidad,
                    plan=random.randint(100, 500),
                    real=random.randint(80, 400),
                )

        # Crear Inmuebles (uno por empresa)
        inmueble = Inmuebles.objects.create(
            empresa=empresa,
        )

        # Asignar valores aleatorios a los campos de inmuebles
        inmueble.loc_oficina = random.randint(0, 10)
        inmueble.cpl = random.randint(0, 10)
        inmueble.almacenes = random.randint(0, 10)
        inmueble.farmacias_opticas = random.randint(0, 10)
        inmueble.taller = random.randint(0, 10)
        inmueble.poncheras = random.randint(0, 10)
        inmueble.plantas_fre = random.randint(0, 10)
        inmueble.top = random.randint(0, 10)
        inmueble.nave_pasaje = random.randint(0, 10)
        inmueble.funeraria = random.randint(0, 10)
        inmueble.floristeria = random.randint(0, 10)
        inmueble.banos_p = random.randint(0, 10)
        inmueble.tienda = random.randint(0, 10)
        inmueble.base_carga = random.randint(0, 10)
        inmueble.circulos_s = random.randint(0, 10)
        inmueble.capillas = random.randint(0, 10)
        inmueble.comedores = random.randint(0, 10)
        inmueble.panaderias = random.randint(0, 10)
        inmueble.dulcerias = random.randint(0, 10)
        inmueble.pana_dulc = random.randint(0, 10)
        inmueble.bodegas = random.randint(0, 10)
        inmueble.minitalleres = random.randint(0, 10)
        inmueble.fabricas = random.randint(0, 10)
        inmueble.carnicerias = random.randint(0, 10)
        inmueble.m_ideal = random.randint(0, 10)
        inmueble.mais = random.randint(0, 10)
        inmueble.tmc = random.randint(0, 10)
        inmueble.bar = random.randint(0, 10)
        inmueble.c_elaboracion = random.randint(0, 10)
        inmueble.restaurant = random.randint(0, 10)
        inmueble.cafeterias = random.randint(0, 10)
        inmueble.c_nocturno = random.randint(0, 10)
        inmueble.cabaret = random.randint(0, 10)
        inmueble.merendero = random.randint(0, 10)
        inmueble.heladerias = random.randint(0, 10)
        inmueble.alojamiento = random.randint(0, 10)
        inmueble.servicios = random.randint(0, 10)
        inmueble.incinerador = random.randint(0, 10)
        inmueble.save()

        # Crear PlanDeMantenimiento
        current_year = 2024
        for year in range(current_year - 2, current_year + 1):
            # Para cada mes del año

            PlanDeMantenimiento.objects.create(
                anno=year,
                empresa=empresa,
                cantidad_de_obras_anual=random.randint(0, 1000),
                importe_total_anual=random.randint(0, 1000),
                cantidad_de_obras_real=random.randint(0, 1000),
                importe_total_real=random.randint(0, 1000),
            )

        # Crear Inversiones
        Inversiones.objects.create(
            empresa=empresa,
            plan_obra=random.randint(10000, 50000),
            real_obra=random.randint(10000, 50000),
            porciento_obra=random.randint(10000, 50000),
            plan_no_nominales=random.randint(10000, 50000),
            real_no_nominales=random.randint(10000, 50000),
            porciento_no_nominales=random.randint(10000, 50000),
            plan_resto=random.randint(10000, 50000),
            real_resto=random.randint(10000, 50000),
            porciento_resto=random.randint(10000, 50000),
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
