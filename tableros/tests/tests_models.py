from django.test import TestCase

from tableros.models import Tablero


class TestModels(TestCase):

    def setUp(self):

        self.tablero1 = Tablero.objects.create(
            id_tablero=5,
            nombre='Tablero de Prueba',
            descripcion='Descripcion de prueba',
            estado='Iniciado'
        )
