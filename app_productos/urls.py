from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.vista_catalogo, name='catalogo'),
    path('detalle/', views.vista_detalle, name='detalle'),
]