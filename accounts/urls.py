from django.urls import path
from . import views


urlpatterns = [
	path('login/',views.loginView, name="login.html"),
	path('registrarse/',views.registrarseView, name="registrarse.html"),
	path('recuperar/',views.recuperarView, name="recuperar.html"),
	path('principal/',views.principalView, name="principal.html"),
	
]