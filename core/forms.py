from django import forms
from .models import Projeto, Empresas, Pessoas

# Create the forms
class ProjetoModelForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['Nome do projeto','Data de término']
 
# try to fix the def __str__ from Projeto model
# class CustomMMCF(forms.ModelChoiceField):
#     def label_from_instance(self, projeto):
#         return "%s" % projeto.nome
            
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