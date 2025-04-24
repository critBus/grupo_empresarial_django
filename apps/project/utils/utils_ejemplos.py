import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from faker import Faker

from ..models import (
    AtencionALaFamilia,
    AtencionPoblacion,
    Bancarizacion,
    CapitalHumano,
    CargoSinCubrir,
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
)
from .nomencladores import (
    NOMBRE_EMPRESA_CONSTRUCCION,
    NOMBRE_EMPRESA_FARMACIAS_OPTICAS,
    NOMBRE_EMPRESA_PRODUCCIONES_VARIAS,
    NOMBRE_EMPRESA_SEGURIDAD_PROTECCION,
)

User = get_user_model()


def crear_datos_random():
    if User.objects.count() > 4 or Cuadro.objects.count() > 0:
        return

    fake = Faker("es_ES")
    today = timezone.now().date()

    # Tipos comunes para varias entidades
    municipios = [
        "Pinar del Río",
        "San Luis",
        "San Juan",
        "Viñales",
        "La Palma",
    ]

    indicadores_generales = [
        "Circulación Mercantil",
        "Ventas Totales",
        "Total de Ingresos",
        "Total de Gastos",
        "Utilidad (o Pérdida) del Periodo",
        "Fondo de Salario Total",
        "Promedio de trabajadores",
        "Producción de Bienes y Servicios",
        "Gasto Material",
        "Otros Gastos Monetarios",
        "Financiamiento entregado al OSDE",
        "Valor Agregado",
        "Productividad",
        "Salario Medio",
        "Gasto total x peso de ingreso total",
        "Fdo de salario x Peso de Ingreso Total",
        "Correlación SM/P",
        "Utilidad o Pérdida Bruta en Ventas",
        "Utilidad o Pérdida Neta en Vtas",
        "Utilidad o Pérdida en Operaciones",
    ]

    # Unidades de medida
    unidades_medida = {
        "Circulación Mercantil": "MP",
        "Ventas Totales": "MP",
        "Total de Ingresos": "MP",
        "Total de Gastos": "MP",
        "Utilidad (o Pérdida) del Periodo": "MP",
        "Fondo de Salario Total": "MP",
        "Promedio de trabajadores": "Uno",
        "Producción de Bienes y Servicios": "MP",
        "Gasto Material": "MP",
        "Otros Gastos Monetarios": "MP",
        "Financiamiento entregado al OSDE": "MP",
        "Valor Agregado": "MP",
        "Productividad": "Pesos",
        "Salario Medio": "Pesos",
        "Gasto total x peso de ingreso total": "Pesos",
        "Fdo de salario x Peso de Ingreso Total": "Pesos",
        "Correlación SM/P": "Índice",
        "Utilidad o Pérdida Bruta en Ventas": "MP",
        "Utilidad o Pérdida Neta en Vtas": "MP",
        "Utilidad o Pérdida en Operaciones": "MP",
    }

    for empresa in Empresa.objects.all():
        # Crear Cuadro
        cuadro = Cuadro.objects.create(
            empresa=empresa,
            aprobada=random.randint(50, 200),
            cubierta=random.randint(30, 150),
        )

        for nombre_indicador in indicadores_generales:
            # Generar valores aleatorios
            plan_acumulado = random.uniform(10000, 1000000)
            real_acumulado = random.uniform(
                plan_acumulado * 0.7, plan_acumulado
            )
            porcentaje_cumplimiento = round(
                (real_acumulado / plan_acumulado) * 100, 2
            )

            # Crear el registro
            IndicadorGeneralGM.objects.create(
                empresa=empresa,
                nombre_indicador=nombre_indicador,
                unidad_medida=unidades_medida.get(nombre_indicador, "MP"),
                plan_acumulado=plan_acumulado,
                real_acumulado=real_acumulado,
                porcentaje_cumplimiento=porcentaje_cumplimiento,
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
        if empresa.nombre == NOMBRE_EMPRESA_PRODUCCIONES_VARIAS:
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
            indice_gestion_cobro=random.uniform(0.7, 1.0),
            ciclo_cobros_dias=random.randint(30, 90),
            por_cobrar_total=random.randint(1000, 90000),
            vencidas_total=random.randint(1000, 90000),
            porcentage_total=random.randint(1000, 90000),
            por_cobrar_a_terceros=random.randint(1000, 90000),
            vencidas_a_terceros=random.randint(1000, 90000),
            porcentage_a_terceros=random.randint(1000, 90000),
            por_cobrar_u_admin=random.randint(1000, 90000),
            vencidas_u_admin=random.randint(1000, 90000),
            porcentage_u_admin=random.randint(1000, 90000),
            por_cobrar_grupo=random.randint(1000, 90000),
            vencidas_grupo=random.randint(1000, 90000),
            porcentage_grupo=random.randint(1000, 90000),
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
            indice_gestion_pago=random.uniform(0.7, 1.0),
            ciclo_pagos_dias=random.randint(30, 90),
            efectos_por_pagar=random.randint(30, 90),
        )

        SoberaniaAlimentaria.objects.create(
            unidad=random.choice(["Km", "Ha", "m²"]),  # Unidad aleatoria
            huertos=random.randint(0, 50),  # Número aleatorio de huertos
            canteros=random.randint(0, 100),  # Número aleatorio de canteros
            tierras=random.randint(0, 200),  # Número aleatorio de tierras
            empresa=empresa,  # Relación con la empresa
        )

        Bancarizacion.objects.create(
            empresa=empresa,
            establecimientos=random.randint(1, 10),
            total_unidades=random.randint(50, 200),
            solicitadas=random.randint(30, 150),
            aprobados_enzona=random.randint(20, 100),
            aprobados_transfermovil=random.randint(20, 100),
            operaciones_acumuladas=random.randint(100, 500),
            importe_acumulado=round(random.uniform(1000, 10000), 2),
        )

        cargas = ["Madera", "Comida", "Plastico"]
        for carga in cargas:
            plan_ind = random.randint(1000, 5000)
            real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
            TransportacionDeCarga.objects.create(
                empresa=empresa,
                plan=plan_ind,
                real=real_ind,
                porciento=int((real_ind / plan_ind) * 100),
                carga=carga,
            )

    # empresa_producciones_varias = Empresa.objects.filter(
    #     nombre=NOMBRE_EMPRESA_PRODUCCIONES_VARIAS
    # ).first()
    #
    # if empresa_producciones_varias:
    #     agregar_perdidas(empresa_producciones_varias)

    empresa_farmacia = Empresa.objects.filter(
        nombre=NOMBRE_EMPRESA_FARMACIAS_OPTICAS
    ).first()

    if empresa_farmacia:
        agregar_perdidas()

        medicamentos = ["Antibiotico", "Aspirina", "Vitamina C"]
        for medicamento in medicamentos:
            plan_ind = random.randint(1000, 5000)
            real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
            Medicamento.objects.create(
                empresa=empresa_farmacia,
                plan=plan_ind,
                en_falta=real_ind,
                porciento_de_afectacion=int((real_ind / plan_ind) * 100),
                medicamento=medicamento,
            )

    # Crear MaterialDeConstruccion solo para la empresa de Construcción

    empresa_construccion = Empresa.objects.filter(
        nombre=NOMBRE_EMPRESA_CONSTRUCCION
    ).first()

    if empresa_construccion:
        # Lista de materiales de construcción
        materiales_construccion = [
            "Bloques hormigón",
            "Ladrillo prensado",
            "Adocreto",
            "Losetas hidráulicas",
            "Baldosas de terrazo",
            "Viguetas hormigón",
            "Placas hormigón",
            "Losa canal hormigón",
            "Marcos de puertas hormigón",
            "Marquetería de hormigón",
            "Mesetas hormigón",
            "Fregaderos hormigón",
            "Lavaderos hormigón",
            "Tanques de hormigón",
            "Cimientos, columnas y paneles de vivienda",
        ]

        # Crear registros para cada material
        for i, material in enumerate(materiales_construccion, 1):
            # Asignar unidad de medida basada en el tipo de material
            unidad = "Mu" if i % 2 == 0 else "mm"  # Alternar entre Mu y mm

            # Crear el registro de MaterialDeConstruccion
            MaterialDeConstruccion.objects.create(
                material=material,
                unidad_de_medida=unidad,
                plan=random.randint(100, 500),  # Valor aleatorio para el plan
                real=random.randint(80, 400),  # Valor aleatorio para el real
            )

        datos_planes = [
            ["Inversiones", ""],
            ["Inicio y Desarrollo", ""],
            ["Operativo", ""],
            ["TOM", "Las dos obras que faltan se terminan este mes"],
            ["Mezcla fria", "Igual porque este mes no se produjo"],
        ]
        for dato_plan in datos_planes:
            PlanDeConstruccion.objects.create(
                nombre=dato_plan[0],
                donde_se_incumple=dato_plan[1],
                plan=random.randint(100, 500),  # Valor aleatorio para el plan
                real=random.randint(80, 400),  # Valor aleatorio para el real
            )

    empresa_seguridad_y_proteccion = Empresa.objects.filter(
        nombre=NOMBRE_EMPRESA_SEGURIDAD_PROTECCION
    ).first()

    if empresa_seguridad_y_proteccion:
        datos = ["Objetivos", "Plantilla", "Decreto 200"]
        for dato in datos:
            total = random.randint(1000, 5000)
            cubiertos = random.randint(int(total * 0.7), total)
            InformacionGeneral.objects.create(
                total=total,
                cubiertos=cubiertos,
                desglosados_gobierno=random.randint(1000, 5000),
                desglosados_tercero=random.randint(1000, 5000),
                fluctuacion=total / cubiertos,
                dato=dato,
            )
    for i in range(30):  # Crear datos para los últimos 30 días
        fecha = today - timedelta(days=i)
        AtencionALaFamilia.objects.create(
            fecha=fecha,
            total_saf=random.randint(50, 200),
            beneficiados_conciliacion=random.randint(100, 300),
            servicio_diario=random.randint(80, 250),
            almuerzan_unidades=random.randint(50, 150),
            mensajeria=random.randint(20, 80),
            llevan_en_cantina=random.randint(30, 100),
            total_beneficiarios=random.randint(100, 300),
        )
    current_year = 2024
    for year in range(current_year - 2, current_year + 1):
        PerfeccionamientoComercioGastronomia.objects.create(
            anno=year,
            directores_filiales=random.randint(0, 20),
            avalados_mercancias=random.randint(0, 500),
            firma_codigo_conducta=random.randint(0, 1000),
            proceso_disponibilidad=random.choice(
                ["Cumplido", "Incumplido", "N/P"]
            ),
            mensajeros_vendedores_ambulantes=random.randint(0, 100),
            creacion_emp_filiales=random.randint(0, 20),
            ueb_dl_34=random.choice(["Cumplido", "Incumplido", "N/P"]),
            manual_identidad_visual=random.randint(0, 500),
            categorizacion_almacenes=random.randint(0, 200),
            licencias_sanitarias=random.randint(0, 300),
            requisitos_calidad_bodegas=fake.text(max_nb_chars=200),
            estado=random.choice(
                ["Cumplido", "Incumplido", "Pendiente", "Con pérdida"]
            ),
        )

    # Crear Inversiones
    Inversiones.objects.create(
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

    indicadores = ["Pasajeros", "Distancias", "Combustible Consumido"]
    for indicador in indicadores:
        plan_ind = random.randint(1000, 5000)
        real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
        TransportacionDePasajeros.objects.create(
            aprobadas=plan_ind,
            real_ejecutadas=real_ind,
            porciento=int((real_ind / plan_ind) * 100),
            indicador=indicador,
        )

    # Crear IndicadorGeneral
    plan_ind = random.randint(1000, 5000)
    real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
    IndicadorGeneral.objects.create(
        plan=plan_ind,
        real=real_ind,
        tipo=random.choice(["Producción", "Servicios", "Ventas"]),
    )


def agregar_perdidas():
    indicadores = ["Producción", "Servicios", "Ventas"]
    for indicador in indicadores:
        plan_ind = random.randint(1000, 5000)
        real_ind = random.randint(int(plan_ind * 0.7), plan_ind)
        Perdida.objects.create(
            plan=plan_ind,
            real=real_ind,
            porciento=int((real_ind / plan_ind) * 100),
            indicador=indicador,
        )
