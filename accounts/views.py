from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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


def registrar_form(request):
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
            registro = registro_form.save(commit=False)
            registro .visibilidad = 'Privado'
            registro.save()
            return HttpResponseRedirect(reverse('registro/registrarse'))
            # tablero_form = TableroForm()
            # return render(request, 'crear_tablero.html', {'tablero_form': tablero_form})
    else:

        #registro_form = RegistroForm()
        print('no funciona')
        registro_form = RegistroForm()

    return render(request, 'registro/registrarse.html', {'registro_form': registro_form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registro/login.html",
                    context={"form":form})
