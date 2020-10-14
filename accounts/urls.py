from django.conf.urls import url
from django.urls import path

from accounts.views import registrar_usuario
from . import views


urlpatterns = [
	path('login/',views.loginView, name="login.html"),
	path('registrarse/', views.registrar_usuario, name="registrarse.html"),
	path('recuperar/',views.recuperarView, name="recuperar.html"),
	path('principal/',views.principalView, name="principal.html"),
	
]