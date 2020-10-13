from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from tableros.models import Usuario


class RegistroForm(ModelForm):

    class Meta:
        model: Usuario
        fields = ['nombre', 'apellido', 'correo', 'contraseña']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'rows': 2,
                    'class': 'form-control col-lg-6'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'rows': 3,
                    'class': 'form-control col-lg-6'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'rows': 4,
                    'class': 'form-control col-lg-6'
                }
            )

        }
