from django.contrib import admin
from .models import Projeto, Empresas, Pessoas

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['Nome do projeto', 'Data de término', 'Dia de criação']
    
@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['Nome da empresa', 'Dia de criação', 'Dia da modificação']

@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Sexo', 'Cargo', 'Dia de criação', 'Dia da modificação']
