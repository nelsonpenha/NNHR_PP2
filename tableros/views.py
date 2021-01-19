from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from tableros.forms import TableroForm, FasesForm, TarjetasForm, User_TarjetaForm, RegistrarseForm
from tableros.models import Tablero, Fases, Tarjeta, Tarjeta_Usuario


@login_required
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


def crear_fases(request,tablero_id):
    # Recuperamos la instancia
    instancia_tablero = Tablero.objects.get(id_tablero=tablero_id)
    list_fase = Fases.objects.filter(id_tablero=tablero_id, estado='Activo')
    fases_form = FasesForm()
    tarjetas_form = TarjetasForm()

    if request.method == 'POST':

        tarjetas_form = TarjetasForm(request.POST)
        fases_form = FasesForm(request.POST)

        if tarjetas_form.is_valid():
            fase_id = request.POST.get("identificador_t")
            instance_fase = Fases.objects.get(id_fases=fase_id)

            t = tarjetas_form.save(commit=False)
            t.id_usuario = request.user.id
            t.id_fases = instance_fase
            t.save()
            return render(request, "listar_fases.html", {'form': fases_form, 'tarjetas_form': tarjetas_form,
                                                         'listar_F': list_fase, 'tablero': instancia_tablero
                                                         })

        if fases_form.is_valid():
            print('Datos validos')
            fases = fases_form.save(commit=False)
            fases.id_usuario = request.user.id
            fases.id_tablero = instancia_tablero
            fases.save()
            form = FasesForm()
            return render(request, "listar_fases.html", {'form': fases_form, 'tarjetas_form': tarjetas_form,
                                                         'listar_F': list_fase, 'tablero': instancia_tablero
                                                         })
    else:
        fases_form = FasesForm()
        tarjetas_form=TarjetasForm()
    return render(request, "listar_fases.html",{'form': fases_form, 'tarjetas_form': tarjetas_form,
                                                         'listar_F': list_fase, 'tablero': instancia_tablero})


def config_tarjeta(request, cambio_id, tablero_id):

    instancia = Tarjeta.objects.get(id_tarjeta=cambio_id)
    tarjeta_usuario = Tarjeta_Usuario.objects.filter(id_tarjeta=cambio_id)
    lista_encargados = [o.id_usuario for o in tarjeta_usuario]
    usuario_lista = User.objects.filter(is_active=True).exclude(id__in=[le.id for le in lista_encargados])
    list_fase = Fases.objects.filter(id_tablero=tablero_id, estado='Activo')

    if request.method == "POST":

        form = TarjetasForm(request.POST, instance=instancia)
        form_ut = User_TarjetaForm(request.POST)
        user_id = request.POST.get("id_usuario_nuevo")

        if form.is_valid():
            fase_id = request.POST.get("id_fase_nuevo")
            instance_fase = Fases.objects.get(id_fases=fase_id)
            print(instance_fase)

            instancia = form.save(commit=False)
            instancia.id_usuario = request.user.id
            instancia.id_fases = instance_fase
            instancia.save()

            return render(request, "config_tarjeta.html", {'usuario_t':form_ut,'form': form, 'listar_fases': list_fase,
                                                           'listar_usuario': usuario_lista, 'tarjeta': instancia})
        if user_id:
            instance_usuario = User.objects.get(id=user_id)
            print("usuario id", instance_usuario)
            print('Datos validos')
            tarjeta_usuario = Tarjeta_Usuario()
            tarjeta_usuario.id_usuario = instance_usuario
            tarjeta_usuario.id_tarjeta = cambio_id
            #tarjeta_usuario.estado = 'Activo'
            tarjeta_usuario.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "config_tarjeta.html",
                          {'usuario_t': form_ut, 'form': form, 'listar_fases': list_fase,
                           'listar_usuario': usuario_lista, 'tarjeta': instancia})

    else:
        form = TarjetasForm(instance=instancia)
        form_ut = User_TarjetaForm()
        return render(request, "config_tarjeta.html", {'usuario_t': form_ut, 'form': form, 'listar_fases': list_fase,
                                                       'listar_usuario': usuario_lista, 'tarjeta': instancia,
                                                       'lista_encargados': lista_encargados})
def registrarse(request):
    if request.method == 'POST':
        registro_form = RegistrarseForm(request.POST)
        print('Estoy almacenando')
        if registro_form.is_valid():
            registro = registro_form.save(commit=False)
            registro.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        registro_form = RegistrarseForm()

    return render(request, 'registrarse.html', {'registro_form': registro_form})
    
def eliminar_fases(request, fases_id):
    faseEliminar = Fases.objects.get(id_fases=fases_id)
    instancia_tablero= faseEliminar.id_tablero
    tablero_id=instancia_tablero.id_tablero
    print(tablero_id)
    faseEliminar.estado = "Inactivo"
    faseEliminar.save()
    return HttpResponseRedirect(reverse('index'))
   # return render(request, 'listar_fases.html', {'tablero': tablero_id})
