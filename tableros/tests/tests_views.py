from django.test import TestCase, Client
from django.urls import reverse
from tableros.models import Tablero, Tarjeta


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # /tableros/principal
        self.principal_url = reverse('principal')
        # /tableros/crear
        self.crear_tablero_url = reverse('crear')
        # /tableros/edit/5
        self.editar_tablero_url = reverse('editar', args=[5])

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
            id_usuario= '1',
            id_tablero='5',
            estado='Activo'
        )

    def test_tablero_list_GET(self):
        response = self.client.get(self.principal_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro/principal.html')

    def test_crear_tablero_GET(self):
        response = self.client.get(self.crear_tablero_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_tablero.html')

    def test_editar_tablero_GET(self):
        response = self.client.get(self.editar_tablero_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_crear_tablero_POST(self):
        # Se simula un request POST de un cliente creando un tablero
        # y se guarda la respuesta en la variable response
        response = self.client.post(self.crear_tablero_url, {
            'id_tablero': 1,
            'nombre': 'Carga de tablero de prueba',
            'descripcion': 'Descripcion de prueba',
            'estado': 'Iniciado'
        })

        # Se busca un tablero con el id_tablero=1
        tablero = Tablero.objects.get(id_tablero=1)
        # status_code = 302 porque se redirige a la pantalla principal
        self.assertEquals(response.status_code, 302)
        # Corroboramos los valores persistidos en el tablero
        self.assertEquals(tablero.descripcion, 'Descripcion de prueba')

    def test_crear_tarjeta_POST(self):
        # Se simula un request POST de un cliente creando una tarjeta
        # y se guarda la respuesta en la variable response
        response = self.client.post(self.crear_tablero_url, {
            'id_tarjeta': 1,
            'nombre_tarjeta': 'Carga de tablero de prueba',
            'descripcion': 'Descripcion de prueba',
            'fecha_limite': '2020-10-29',
            'id_usuario': 1,
            'id_tablero': 1,
            'estado': 'Arctivo'

        })

        # Se busca un tablero con el id_tarjeta=1
        tarjeta = Tarjeta.objects.get(id_tarjeta=1)
        # status_code = 302 porque se redirige a la pantalla principal
        self.assertEquals(response.status_code, 302)
        # Corroboramos los valores persistidos en la tarjeta
        self.assertEquals(tarjeta.descripcion, 'Descripcion de prueba')