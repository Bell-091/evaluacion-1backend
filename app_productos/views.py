from django.shortcuts import render

# Create your views here.

def vista_catalogo(request):
    return render(request, 'app_productos/vista1.html')

def vista_detalle(request):
    return render(request, 'app_productos/vista2.html')