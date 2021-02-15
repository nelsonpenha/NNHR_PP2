"""nnhr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('principal/', views.pagina_principal, name='principal'),
    path('crear/', views.crear_tablero, name='crear'),
    path('edit/<int:cambio_id>', views.edit, name='editar'),
    path('crear_fases/<int:fases_id>', views.crear_fases, name='crear_tablero'),
    path('eliminarTablero/<int:eliminarId>', views.eliminarTablero, name='eliminar-tablero'),
    path('crear_tarjeta/<int:card_id>', views.crear_tarjeta, name='crear_tarjeta'),
]
