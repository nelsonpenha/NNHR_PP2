from django.forms import ModelForm
from django import forms

from tableros.models import Tablero, Fases, Tarjeta, Tarjeta_Usuario


class TableroForm(ModelForm):
    descripcion = forms.CharField(max_length=256, min_length=5, widget=forms.Textarea(attrs={
                    'rows': 2,
                    'class': 'form-control col-lg-6'
                }))
    nombre = forms.CharField(max_length=256, min_length=5, widget=forms.TextInput(attrs={
        'class': 'form-control col-lg-6'
    }))

    class Meta:
        requiredMessage = 'Este campo es requerido'
        model = Tablero
        fields = ['nombre', 'descripcion', 'visibilidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),
            # 'descripcion': forms.Textarea(
            #     attrs={
            #         'rows': 2,
            #         'class': 'form-control col-lg-6'
            #     }
            # ),
            'visibilidad': forms.Select(
                choices=Tablero.ESTADOS_VISIBILIDAD,
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),
            'estado': forms.Select(
                choices=Tablero.ESTADOS_TABLERO,
                attrs={
                    'class': 'form-control col-lg-6'
                }
            )
        }
        error_messages = {
            'nombre': {
                'required': requiredMessage,
            },
            'descripcion': {
                'required': requiredMessage,
            },
            'visibilidad': {
                'required': requiredMessage,
            },
            'estado': {
                'required': requiredMessage,
            }
        }


class FasesForm(ModelForm):
    # descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Fases
        fields = ['nombre_fases']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),

        }
class TarjetasForm(ModelForm):

    nombre_tarjeta = forms.CharField(max_length=256, min_length=5, widget=forms.TextInput(attrs={
        'class': 'form-control col-lg-6'
    }))

    class Meta:
        requiredMessage = 'Este campo es requerido'
        model = Tarjeta
        fields = ['nombre_tarjeta','fecha_limite']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),

            'fecha_limite': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}
            ),


        }
        error_messages = {
            'nombre': {
                'required': requiredMessage,
            },


        }
class User_TarjetaForm(ModelForm):

    class Meta:

        model = Tarjeta_Usuario
        fields = ['id_tarjeta','id_usuario']


