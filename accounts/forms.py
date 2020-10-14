from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form

from tableros.models import Usuario


class RegistroForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'contrasenha']
        labels = {
            "contrasenha": "Contraseña",
            #"fecha_nacimiento": "Fecha de Nacimiento"
        }
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
            #'fecha_nacimiento':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),


            'correo': forms.TextInput(
                attrs={
                    'rows': 3,
                    'class': 'form-control col-lg-6'
                }
            ),
            'contrasenha': forms.TextInput(
                attrs={
                    'rows': 4,
                    'class': 'form-control col-lg-6'
                }
            )

        }



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user