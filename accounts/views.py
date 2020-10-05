from django.shortcuts import render

def registrarseView(request):
	return render( request,'registro/registrarse.html')
	
def loginView(request):
	return render( request,'registro/login.html')

def recuperarView(request):
	return render( request,'registro/recuperar.html')

def principalView(request):
	return render( request,'registro/principal.html')
