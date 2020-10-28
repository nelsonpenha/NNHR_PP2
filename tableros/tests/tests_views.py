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
        self.crear_tarjeta_url = reverse('crear_tarjeta')
        # /tableros/edit/5
        self.editar_tablero_url = reverse('editar', args=[5])
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
            fecha_limite='22/10/2020',
            fecha_registro='22/10/2020',
            id_tablero='1'
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

    def test_crear_tarjeta_GET(self):
        response = self.client.get(self.crear_tarjeta_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_tarjeta.html')

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
            'nombre_tarjeta': 'Carga de tablero de tarjeta',
            'descripcion': 'Descripcion de prueba',
            'estado': 'Activo',
            'fecha_limite': '22/10/2020',
            'id_tablero': '1',
            'fecha_registro': '20/10/2020'
        })

        # Se busca un tablero con el id_tablero=1
        tarjeta = Tarjeta.objects.get(id_tarjeta=1)
        # status_code = 302 porque se redirige a la pantalla principal
        self.assertEquals(response.status_code, 302)
        # Corroboramos los valores persistidos en la tarjeta
        self.assertEquals(tarjeta.descripcion, 'Descripcion de prueba')