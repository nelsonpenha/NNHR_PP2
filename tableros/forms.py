from django.forms import ModelForm
from django import forms

from tableros.models import Tablero


class TableroForm(ModelForm):
    # descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Tablero
        fields = ['nombre', 'descripcion', 'visibilidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control col-lg-6'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'rows': 2,
                    'class': 'form-control col-lg-6'
                }
            ),
            'visibilidad': forms.Select(
                choices=Tablero.ESTADOS_VISIBILIDAD,
                attrs={
                    'class': 'form-control w-50'
                }
            ),
            'estado': forms.Select(
                choices=Tablero.ESTADOS_TABLERO,
                attrs={
                    'class': 'form-control w-50'
                }
            )
        }


