from django.test import TestCase

from tableros.models import Tablero, Tarjeta


class TestModels(TestCase):

    def setUp(self):

        self.tablero1 = Tablero.objects.create(
            id_tablero=5,
            nombre='Tablero de Prueba',
            descripcion='Descripcion de prueba',
            estado='Iniciado'
        )

        self.tarjeta1 = Tarjeta.objects.create(
            id_tarjeta=5,
            nombre_tarjeta='Tarjeta de Prueba',
            descripcion='Descripcion de prueba',
            estado='Activo',
            fecha_limite = '22/10/2020',
            fecha_registro='22/10/2020',
            id_tablero = '1'
        )

