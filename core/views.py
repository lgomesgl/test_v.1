from django.shortcuts import render
from django.contrib import messages

from .forms import ProjetoModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projetos(request):
    if str(request.method) == 'POST': # se o método for POST
        form = ProjetoModelForm(request.POST or None)
        if form.is_valid(): # validando o formulario
            form.save()
            
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
    return render(request, 'empresas.html')

def pessoas(request):
    return render(request, 'pessoas.html')
