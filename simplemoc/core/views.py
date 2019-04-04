import pygal
from django.shortcuts import render


from .models import Pessoas, Custos, Pedidos


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
    grafico = gerar_graf()
    context = {'lista_pessoas': Pessoas.objects.all(), 'grafico': grafico}
    return render(request, 'pessoas.html', context)


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

    context = {'lista_custos': Custos.objects.all()}
    return render(request, 'custos.html', context)


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
    usr = Pessoas.objects.get(id=id)
    context = {'lista_pedidos': Pedidos.objects.filter(pessoa=usr)}
    return render(request, 'pedidos.html', context)


def home4(request, data):
    print(data)
    # data= '2018-06-11'
    usr = Pedidos.objects.filter(dia=data)
    context = {'lista_por_dia': usr}
    return render(request, 'por_dia.html', context)


def gerar_graf():
    line_chart = pygal.Line()
    line_chart.title = 'Numero de restaurantes (em %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Hamburgueria BoiNaChapa', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Pastelaria Cruzoé', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('Newton Massas', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Pizzaria do Nono', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])

    return line_chart.render()
