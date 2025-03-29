from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from apps.project.models import (
    Empresa,
    Cuadro,
    AtencionPoblacion,
    CapitalHumano,
    Interruptos,
    Delitos,
    PlanRecape,
    PlanMateriaPrima,
    PlanDeMantenimiento,
    Inversiones,
    IndicadorGeneral,
    Deficiencias,
    UEBperdidas,
    CuentasCobrar,
    CuentasPagar,
    Inmuebles,
)


class OneToOneRelationsTest(TestCase):
    def setUp(self):
        # Crear una empresa para las pruebas
        self.empresa1 = Empresa.objects.create(
            codigo="EMP001", nombre="Empresa Test 1"
        )
        self.empresa2 = Empresa.objects.create(
            codigo="EMP002", nombre="Empresa Test 2"
        )

    @transaction.atomic
    def test_cuadro_one_to_one(self):
        # Crear primer cuadro
        cuadro1 = Cuadro.objects.create(
            aprobada=10, cubierta=8, empresa=self.empresa1
        )

        # Intentar crear otro cuadro para la misma empresa debe fallar
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Cuadro.objects.create(
                    aprobada=12, cubierta=10, empresa=self.empresa1
                )

        # Crear cuadro para otra empresa debe funcionar
        Cuadro.objects.create(aprobada=15, cubierta=12, empresa=self.empresa2)

    @transaction.atomic
    def test_atencion_poblacion_one_to_one(self):
        atencion1 = AtencionPoblacion.objects.create(
            quejas=5, peticiones=10, termino="Q1", empresa=self.empresa1
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                AtencionPoblacion.objects.create(
                    quejas=3, peticiones=7, termino="Q2", empresa=self.empresa1
                )

    @transaction.atomic
    def test_capital_humano_one_to_one(self):
        capital1 = CapitalHumano.objects.create(
            plantillaAprobada=100,
            plantillaCubierta=90,
            mujeres=45,
            empresa=self.empresa1,
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                CapitalHumano.objects.create(
                    plantillaAprobada=120,
                    plantillaCubierta=110,
                    mujeres=55,
                    empresa=self.empresa1,
                )

    @transaction.atomic
    def test_interruptos_one_to_one(self):
        interruptos1 = Interruptos.objects.create(
            total=20,
            equiposRotos=8,
            faltaPiezas=7,
            otrasCausas=5,
            empresa=self.empresa1,
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Interruptos.objects.create(
                    total=15,
                    equiposRotos=6,
                    faltaPiezas=5,
                    otrasCausas=4,
                    empresa=self.empresa1,
                )

    @transaction.atomic
    def test_delitos_one_to_one(self):
        delitos1 = Delitos.objects.create(
            denuncia=1,
            municipio="Test",
            fecha="2025-03-28",
            unidad="Unidad1",
            tipocidad="Tipo1",
            productosSustraidos="Productos1",
            valorPerdidas=1000.0,
            medidasTomadas="Medidas1",
            empresa=self.empresa1,
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Delitos.objects.create(
                    denuncia=2,
                    municipio="Test2",
                    fecha="2025-03-28",
                    unidad="Unidad2",
                    tipocidad="Tipo2",
                    productosSustraidos="Productos2",
                    valorPerdidas=2000.0,
                    medidasTomadas="Medidas2",
                    empresa=self.empresa1,
                )

    @transaction.atomic
    def test_deficiencias_one_to_one(self):
        deficiencias1 = Deficiencias.objects.create(
            total=10, resueltas=6, pendientes=4, empresa=self.empresa1
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Deficiencias.objects.create(
                    total=8, resueltas=5, pendientes=3, empresa=self.empresa1
                )

    @transaction.atomic
    def test_ueb_perdidas_one_to_one(self):
        ueb1 = UEBperdidas.objects.create(
            cantidadUEB=5,
            nombre="UEB Test",
            municipio="Municipio Test",
            empresa=self.empresa1,
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                UEBperdidas.objects.create(
                    cantidadUEB=3,
                    nombre="UEB Test 2",
                    municipio="Municipio Test 2",
                    empresa=self.empresa1,
                )

    @transaction.atomic
    def test_inmuebles_one_to_one(self):
        inmuebles1 = Inmuebles.objects.create(
            tipo="Tipo Test", cantidad=10, empresa=self.empresa1
        )

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Inmuebles.objects.create(
                    tipo="Tipo Test 2", cantidad=5, empresa=self.empresa1
                )

    def test_deficiencias_validation_rule(self):
        """Prueba específica para la regla de validación de Deficiencias"""
        with self.assertRaises(ValidationError):
            deficiencias = Deficiencias(
                total=10,
                resueltas=4,
                pendientes=5,  # 4 + 5 != 10
                empresa=self.empresa1,
            )
            deficiencias.full_clean()  # Esto dispara las validaciones

        # Debe funcionar cuando la suma es correcta
        deficiencias = Deficiencias(
            total=10,
            resueltas=6,
            pendientes=4,  # 6 + 4 = 10
            empresa=self.empresa1,
        )
        deficiencias.full_clean()  # No debe lanzar excepción
