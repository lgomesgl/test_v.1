from django.db import models

# Create your models here.
# Create a Base model with some ordinary column.
class Base(models.Model):
    date_creates = models.DateField(name='Dia de criação', auto_now_add=True) # auto_now_add: firts time are created
    date_modify = models.DateField(name='Dia da modificação', auto_now=True)

    class Meta: 
        abstract = True # deixando a classe abstrata.
        
class Projeto(Base):
    nome = models.CharField(max_length=100, unique=True)
    data_over = models.DateField(name='Data de término', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
    
    def __str__(self): # why is not working????? -- WORK: NO method name in models.CharField
        return self.nome
      
class Empresas(Base):
    nome = models.CharField(name='Nome da empresa', max_length=100, unique=True)
    projeto = models.ManyToManyField(Projeto)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    #def __str__(self):
        #return self.nome
    
class Pessoas(Base):
    SEXO = [
        ('M','Masculino'),
        ('F','Feminino'),    
    ]
    
    CARGOS = [
        ('Professor Doutor','Professor Doutor'),
        ('Professor Adjunto','Professor Adjunto'),
        ('Pesquisador','Pesquisador'),
        ('Pós-Doc','Pós-Doc'),
        ('Doutorando','Doutorando'),
        ('Mestrando','Mestrando'),
    ]
    
    nome = models.CharField(name='Nome', max_length=100)
    sexo = models.CharField(name='Sexo', max_length=1, choices=SEXO)
    cargo = models.CharField(name='Cargo', max_length=100, choices=CARGOS)
    projeto = models.ManyToManyField(Projeto)
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        
    #def __str__(self):
        #return self.nome
    
