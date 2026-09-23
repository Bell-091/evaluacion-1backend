from django.shortcuts import render

# Create your views here.

def perfil_1(request):
    # contexto de datos para la plantilla 
    data={"nombre":"Mario","año":1990,"correo":"mario@example.com"}
    return render(request,'perfil/p1.html',data)


def perfil_2(request):
    # contexto de datos para la plantilla 
    data={"nombre":"Sonic","año":1991,"correo":"sonic@example.com"}
    return render(request,'perfil/p2.html',data)    