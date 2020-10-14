from django.conf.urls import url
from django.urls import path

from accounts.views import registrar_form
from . import views


urlpatterns = [
	path("login", views.login_request),
	path('registrarse/', views.registrar_form, name="registrarse.html"),
	path('recuperar/',views.recuperarView, name="recuperar.html"),
	path('principal/',views.principalView, name="principal.html"),
	
]
