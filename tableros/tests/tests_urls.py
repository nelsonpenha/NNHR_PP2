from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tableros.views import pagina_principal, crear_tablero, edit


class TestUrls(SimpleTestCase):

    def test_principal_url_works(self):
        url = reverse('principal')
        self.assertEquals(resolve(url).func, pagina_principal)

    def test_crear_tablero_url_works(self):
        url = reverse('crear')
        self.assertEquals(resolve(url).func, crear_tablero)

    def test_edit_tablero_url_works(self):
        url = reverse('editar', args=[1])
        self.assertEquals(resolve(url).func, edit)
