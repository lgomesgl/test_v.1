from django.urls import path
from .views import IndexView, ProjetosView, EmpresasView, PessoasView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('empresas/', EmpresasView.as_view(), name='empresas'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
]
