from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Projeto, Empresas, Pessoas

# Create the forms
class CreateUserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
class ProjetoModelForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome','Data de término']
        
    # def save(self, commit=True):
    #     user = super(ProjetoModelForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #         self.save_m2m()
    #     return user
    
    # def save(self):
    #     user = super(ProjetoModelForm, self).save()
    #     user.save()
        
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
    
    # def save(self):
    #     user = super(EmpresasModelForm, self).save()
    #     user.save()
    
class PessoasModelForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = ['Nome', 'Sexo', 'Cargo', 'projetos']
        
    if int(Projeto.objects.all().count()) < 5: # if size of the table is bigger then 5 choices, default the
        widget = forms.CheckboxSelectMultiple
    else:
        widget = None
        
    projetos = forms.ModelMultipleChoiceField( # projetos field in form
        queryset = Projeto.objects.all(),
        widget = widget
    )                
    
    # def save(self, commit=True):
    #     user = super(PessoasModelForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #         self.save_m2m()
    #     return user                                                                                                                                                                                                                                                                                                                                                                                                                       