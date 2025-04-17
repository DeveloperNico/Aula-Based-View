from django.db import models
from django.contrib.auth.models import AbstractUser

class Aniversariante(models.Model):
    nome = models.CharField(max_length=20)
    data = models.DateField()
    idade = models.PositiveIntegerField()
    CPF = models.CharField(max_length=14, unique=True)
    boloPreferido = models.CharField(max_length=255)
    sexo = models.CharField(choices=(
        ('F', 'Feminino'),
        ('M','Masculino'),
        ('O', 'Outros')
    ))

    def __str__(self):
        return self.nome
    
class Usuario(AbstractUser):
    telefone = models.CharField(max_length=12, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username