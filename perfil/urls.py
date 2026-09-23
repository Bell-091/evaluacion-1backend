from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil_1, name='perfil_1'),
    path('p1/', views.perfil_1, name='p1'),
    path('p2/', views.perfil_2, name='p2'),  
]
