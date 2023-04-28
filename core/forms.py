from django import forms
from .models import Projeto, Empresas

# Create the forms
# Projeto
class ProjetoModelForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['Nome do projeto']
        
# Empresas
# class EmpresasModelForm(forms.ModelForm):
#     class Meta:
#         model = Empresas
#         fields = ['Nome da empresa', 'projetos']
        
#     projetos = forms.ModelMultipleChoiceField(
#         queryset = Projeto.objects.all(),
#         widget = forms.CheckboxSelectMultiple
#     )