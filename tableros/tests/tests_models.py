from django.test import TestCase

from tableros.models import Tablero
from tableros.models import Tarjeta

class TestModels(TestCase):

    def setUp(self):

        self.tablero1 = Tablero.objects.create(
            id_tablero=5,
            nombre='Tablero de Prueba',
            descripcion='Descripcion de prueba',
            estado='Iniciado'
        )

        self.card = Tarjeta.objects.create(
            id_tarjeta=1,
            nombre_tarjeta=' rueba',
            descripcion='Descripcion de prueba',
            fecha_limite='2020-09-19',
            id_usuario='1',
            id_tablero='5',
            estado='Activo'
        )