from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    nascimento = models.DateField(null=True)
    email = models.EmailField(null=True)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
