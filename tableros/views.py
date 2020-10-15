from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from tableros.forms import TableroForm
from tableros.models import Tablero


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


def crear_tablero(request):
    """
    Despliega el formulario para crear un tablero.
    Permite crear un tablero

    :param request: El GET contiene el formulario 'tablero_form' vacío.
                    El POST contiene los datos rellenados por el usuario en 'tablero_form'
    :return: vista del formulario o redirecciona a la página principal
    """

    if request.method == 'POST':
        tablero_form = TableroForm(request.POST)
        print('Estoy almacenando')
        if tablero_form.is_valid():
            print('Datos validos')
            tablero = tablero_form.save(commit=False)
            tablero.visibilidad = 'Privado'
            tablero.save()
            return HttpResponseRedirect(reverse('index'))
            # tablero_form = TableroForm()
            # return render(request, 'crear_tablero.html', {'tablero_form': tablero_form})
    else:
        tablero_form = TableroForm()

    return render(request, 'crear_tablero.html', {'tablero_form': tablero_form})


def editar_form(request):

    #edit_tab = Tablero.objects.get(id = id )
    editar= TableroForm()
    
    return render(request,'editar_tablero.html',{'editar':editar})
