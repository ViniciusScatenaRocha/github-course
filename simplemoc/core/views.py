from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Pessoas, Custos, Pedidos, Por_dia
import csv

def home(request):
    # path = '/home/vinicius/Área de Trabalho/Treino/pessoas.csv'
    # with open(path) as f:
    #     reader = csv.reader(f, delimiter=';')
    #     next(reader)
    #     for row in reader:
    #         print(row)
    #         _, created = Pessoas.objects.get_or_create(
    #             nome=row[1],
    #             altura=row[2],
    #             idade=row[3],
    #             cidade=row[4]
    #             )
    context = {'lista_pessoas' : Pessoas.objects.all()}
    return render(request,'pessoas.html', context)

def home2(request):
    # path = '/home/vinicius/Área de Trabalho/Treino/custos.csv'
    # with open(path) as f:
    #     reader = csv.reader(f, delimiter = ';')
    #     next(reader)
    #     for row in reader:
    #         print(row)
    #         _, created = Custos.objects.get_or_create(
    #             restaurante=row[1],
    #             comida=row[2],
    #             custos = row[3],
    #             )
    context = {'lista_custos' : Custos.objects.all()}
    return render(request,'custos.html', context)

def home3(request, id):
    # path = '/home/vinicius/Área de Trabalho/Treino/pedidos.csv'
    # with open(path) as f:
    #     reader = csv.reader(f, delimiter= ';')
    #     next(reader)
    #     for row in reader:
    #         print(row)
    #         _, created = Pedidos.objects.get_or_create(
    #             pessoa=row[1],
    #             restaurante=row[2],
    #             dia=row[3],
    #             comida=row[4],
    #             )
    usr= Pessoas.objects.get(id=id)
    context = {'lista_pedidos' : Pedidos.objects.filter(pessoa=usr)}
    return render(request,'pedidos.html', context)

def home4(request, data):
    print(data)
    #data= '2018-06-11'
    usr= Pedidos.objects.filter(dia=data)
    context ={'lista_por_dia' : usr}
    return render(request,'por_dia.html', context)
