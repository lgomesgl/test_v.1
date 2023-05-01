from django import forms
from .models import Projeto, Empresas, Pessoas

# Create the forms
class ProjetoModelForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','Data de término']
            
class EmpresasModelForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['Nome da empresa', 'projetos']
        
    if int(Projeto.objects.all().count()) < 5: # if size of the table is bigger then 5 choices, default the
        widget = forms.CheckboxSelectMultiple
    else:
        widget = None
    
    projetos = forms.ModelMultipleChoiceField(
        queryset = Projeto.objects.all(),
        widget = widget 
    )
    
class PessoasModelForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = ['Nome', 'Sexo', 'Cargo', 'projetos']
        
    if int(Projeto.objects.all().count()) < 5: # if size of the table is bigger then 5 choices, default the
        widget = forms.CheckboxSelectMultiple
    else:
        widget = None
        
    projetos = forms.ModelMultipleChoiceField(
        queryset = Projeto.objects.all(),
        widget = widget
    )                                                                                                                                                                                                                                                                                                                                                                                                                                       