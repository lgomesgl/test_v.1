from django.contrib import admin
from .models import Projeto, Empresas, Pessoas

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'Data de término', 'Dia de criação']
    # list_filter = ['nome']
    search_fields = ['nome']
    
@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ['Nome da empresa', 'Dia de criação', 'Dia da modificação']
    # list_filter = ['Nome da empresa']
    search_fields = ['Nome da empresa']

@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Sexo', 'Cargo', 'Dia de criação', 'Dia da modificação']
    # list_filter = ['Nome', 'Cargo']
    search_fields = ['Nome']
