from django.conf.urls import url
from django.urls import path

from accounts.views import RegistroForm
from . import views


urlpatterns = [
	path('login/',views.loginView, name="login.html"),
	path('registro/', views.RegistroForm),
	path('recuperar/',views.recuperarView, name="recuperar.html"),
	path('principal/',views.principalView, name="principal.html"),
	
]