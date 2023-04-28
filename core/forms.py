from django import forms
from .models import Projeto, Empresas, Pessoas

# Create the forms
# Projeto
class ProjetoModelForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['Nome do projeto']
        
# Empresas
class EmpresasModelForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['Nome da empresa', 'projetos']
        
    if Projeto.objects.all().count() < 5: # if size of the table is bigger then 5 choices, default the
        widget = forms.CheckboxSelectMultiple
    else:
        widget = False
    
    projetos = forms.ModelMultipleChoiceField(
        queryset = Projeto.objects.all(),
        widget = widget 
    )
    
# Pessoas
class PessoasModelForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = ['Nome', 'Sexo', 'Cargo', 'projetos']
        
    projetos = forms.ModelMultipleChoiceField(
        queryset = Projeto.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )                                                                                                                                                                                                                                                                                                                                                                                                                                       