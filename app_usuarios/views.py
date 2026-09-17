from django.shortcuts import render

# Create your views here.
def vista_registro(request):
    return render(request, 'app_usuarios/vista1.html')

def vista_perfil(request):
    return render(request, 'app_usuarios/vista2.html')