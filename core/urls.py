from django.urls import path
from .views import index, projetos, empresas, pessoas

urlpatterns = [
    path('', index, name='index'),
    path('projetos/', projetos, name='projetos'),
    path('empresas/', empresas, name='empresas'),
    path('pessoas/', pessoas, name='pessoas'),
]
