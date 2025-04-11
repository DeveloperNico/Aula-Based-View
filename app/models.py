from django.db import models

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