# Create your models here.
from django.db import models


class Pessoas(models.Model):
    nome = models.CharField(max_length=30, default='0')
    altura = models.DecimalField(max_digits=4, decimal_places=2, default='1')
    idade = models.DecimalField(max_digits=4, decimal_places=0, default='2')
    cidade = models.CharField(max_length=30, default='3')

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Custos(models.Model):
    restaurante = models.CharField(max_length=50, default='4')
    comida = models.CharField(max_length=30, default='5')
    custos = models.CharField(max_length=30, default='6')

    class Meta:
        ordering = ["restaurante"]


class Pedidos(models.Model):
    pessoa = models.CharField(max_length=30, default='7')
    restaurante = models.CharField(max_length=30, default='8')
    dia = models.DateTimeField()
    comida = models.CharField(max_length=30, default='10')

    class Meta:
        ordering = ["pessoa"]


class Por_dia(models.Model):
    pedidos = models.CharField(max_length=30, default='11')
    dia = models.DateTimeField()
