from django.shortcuts import render
from django.contrib import messages

from .forms import ProjetoModelForm, EmpresasModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projetos(request):
    if str(request.method) == 'POST': # se o método for POST
        form = ProjetoModelForm(request.POST or None)
        if form.is_valid(): # validando o formulario
            form.save() # colocando os dados no banco de dados
            
            messages.success(request, 'Novo projeto cadastrado')
            form = ProjetoModelForm() # deixando o formulario em branco
        else:
            messages.error(request, 'ERRO')
    else:
        form = ProjetoModelForm() # deixando o formulario em branco
        
    context = { # o que vai ser levado para o .html
        'form': form 
    }  
        
    return render(request, 'projetos.html', context)

def empresas(request):
    if str(request.method) == 'POST': # se o método for POST
        form = EmpresasModelForm(request.POST or None)
        if form.is_valid(): # validando o formulario
            form.save() # colocando os dados no banco de dados
            
            messages.success(request, 'Nova empresa cadastrada')
            form = EmpresasModelForm() # deixando o formulario em branco
        else:
            messages.error(request, 'ERRO')
    else:
        form = EmpresasModelForm() # deixando o formulario em branco
        
    context = { # o que vai ser levado para o .html
        'form': form 
    }  
      
    return render(request, 'empresas.html', context)

def pessoas(request):
    return render(request, 'pessoas.html')
