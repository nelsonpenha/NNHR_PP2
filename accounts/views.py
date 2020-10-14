from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import RegistroForm
from tableros.models import Tablero
from tableros.models import Usuario

def loginView(request):
    return render(request, 'registro/login.html')


def recuperarView(request):
    return render(request, 'registro/recuperar.html')


def principalView(request):
    return render(request, 'registro/principal.html')

def area_trabajoView(request):
   return render( request,'area_trabajo.html')

def pagina_principal(request):
    """
    Obtiene la lista completa de tableros registrados en el sistema y despliega en la vista principal

    :param request: No contiene información adicional
    :return: lista de tipo @Tablero
    """

    tableros_lista = Tablero.objects.all()

    # En el caso de que queramos utilizar JSON para construir nuestros elementos
    # results = [ob.as_json() for ob in tableros_lista]

    return render(request, 'registro/principal.html', {"tableros": tableros_lista})


def registrar_usuario(request):
    """
    Despliega el formulario para crear un tablero.
    Permite crear un tablero

    :param request: El GET contiene el formulario 'tablero_form' vacío.
                    El POST contiene los datos rellenados por el usuario en 'tablero_form'
    :return: vista del formulario o redirecciona a la página principal
    """

    if request.method == 'POST':
        registro_form = RegistroForm(request.POST)
        print('Estoy almacenando')
        if registro_form.is_valid():
            print('Datos validos')
            Usuario = registro_form.save(commit=False)
            Usuario.visibilidad = 'Privado'
            Usuario.save()
            return HttpResponseRedirect(reverse('registro/registrarse'))
            # tablero_form = TableroForm()
            # return render(request, 'crear_tablero.html', {'tablero_form': tablero_form})
    else:
        #registro_form = RegistroForm()
        print('no funciona')
        registro_form = RegistroForm()

    return render(request, 'registro/registrarse.html', {'registro_form': registro_form})
