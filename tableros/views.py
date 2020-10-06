from django.shortcuts import render

from tableros.models import Tablero


def pagina_principal(request):

    tableros_lista = Tablero.objects.all()

    results = [ob.as_json() for ob in tableros_lista]

    return render(request, 'registro/principal.html', {"tableros": results})
