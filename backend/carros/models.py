from django.db import models
from django.contrib.auth.models import User

class Carro(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('VENDIDO', 'Vendido'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não urgente'),
    ]

    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')
    
  
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')

    data_cadastro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.carro.nome}"
    
