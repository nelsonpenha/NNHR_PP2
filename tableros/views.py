from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from tableros.forms import TableroForm, FasesForm,TarjetasForm
from tableros.models import Tablero, Fases


def pagina_principal(request):
    """
    Obtiene la lista completa de tableros registrados en el sistema y despliega en la vista principal

    :param request: No contiene información adicional
    :return: lista de tipo @Tablero
    """

    # Verifica si se recibe un mensaje para desplegar
    message = None
    if 'form_message' in request.session:
        message = request.session['form_message']
        del request.session['form_message']
        messages.success(request, message)

    tableros_lista = Tablero.objects.filter(activo=True)

    # En el caso de que queramos utilizar JSON para construir nuestros elementos
    # results = [ob.as_json() for ob in tableros_lista]

    return render(request, 'registro/principal.html', {"tableros": tableros_lista, "message": message})


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
            tablero.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        tablero_form = TableroForm()

    return render(request, 'crear_tablero.html', {'tablero_form': tablero_form})


def edit(request, cambio_id):
    # Recuperamos la instancia de la persona
    instancia = Tablero.objects.get(id_tablero=cambio_id)

    # Creamos el formulario con los datos de la instancia
    form = TableroForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TableroForm(request.POST, instance=instancia)
        # Si el formulario es válido
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

            # pasamos el mensaje de guardado con éxito al request
            request.session['form_message'] = "Guardado exitosamente"

            #volvemos al inicio
            return HttpResponseRedirect(reverse('index'))

    # Si llegamos al final renderizamos el formulario
    return render(request, "edit.html", {'form': form})


def eliminarTablero(request, eliminarId):
    tableroEliminar = Tablero.objects.get(id_tablero = eliminarId)
    tableroEliminar.activo = False
    tableroEliminar.save()
    return HttpResponseRedirect(reverse('index'))


def crear_fases(request,fases_id):
    # Recuperamos la instancia
    list_fase = Fases.objects.all()
    instancia_fase = Tablero.objects.get(id_tablero=fases_id)
    id_valor=instancia_fase.id_tablero
    if request.method == 'POST':
        fases_form = FasesForm(request.POST)
        print('Estoy almacenando')
        if fases_form.is_valid():
            print('Datos validos')
            fases = fases_form.save(commit=False)
            fases.id_usuario ='1'
            fases.id_tablero = instancia_fase
            fases.save()
            return HttpResponseRedirect(reverse('index'))
            #return HttpResponseRedirect(reverse(lista))
    else:
        form = FasesForm()
    return render(request, "listar_fases.html", {'form': form,'listar_F': list_fase})

def listar_fas(request):

    list_fase = Fases.objects.all()

    return render(request, "ejemplo_listF.html", {'listar_F': list_fase})



