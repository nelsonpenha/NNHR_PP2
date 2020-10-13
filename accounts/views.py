from django.template.context_processors import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import RegistroForm
from tableros.models import Usuario


def loginView(request):
    return render(request, 'registro/login.html')


def recuperarView(request):
    return render(request, 'registro/recuperar.html')


def principalView(request):
    return render(request, 'registro/principal.html')





class RegistroForm(request):

    if request.method == 'POST':

        registro_form = RegistroForm(request.POST)

        if registro_form.is_valid():

            Usuario = registro_form.save(commit=False)

            Usuario.visibilidad = 'Privado'

            Usuario.save()

           #return HttpResponseRedirect(reverse('index'))

        else:

            registro_form_form = RegistroForm()

       # return render (request,'registrarse.html',{'registro_form': registro_form})

