import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
def soma_elementos(*args):
    retorno = []
    for i in range(len(args[0])):
        soma = 0
        for l in args:
            soma += l[i]
        retorno.append(soma)
    
    return retorno

def total_vendas_por_mes(meses, *args):
    plt.plot(meses, soma_elementos(list(args)[0]))
    plt.legend(["Total"])

    plt.show()


def vendas_de_produtos_por_mes(*args):
    legendas = []
    for l in args:
        legendas.append(l.titulo)
        plt.plot(l.x, l.y, label=l.titulo)
    plt.legend(legendas)
    plt.show()



def comparativo_por_mes(graf1, graf2):
    plt.bar(graf1.x, graf1.y)
    plt.bar(graf2.x, graf2.y)

    plt.legend([graf1.titulo, graf2.titulo])

    plt.show()

def hist_faixa_qtd_por_mes(lista):
    yint = range(1, 12, 1)

    plt.yticks(yint)
    plt.hist(lista)
    plt.show()



def perc_quantidade_por_ano(*args):
    total = soma_elementos(list(args)[0])
    labels = ['Creme facial', 'Limpeza facial', 'Pasta dentária', 'Sabonete', 'Shampoo', 'Hidratante']
    total = np.array(total)
    total = np.sum(total)
    perc = []

    for l in args:
        lista = np.array(l)
        totalLista = np.sum(lista)
        perc.append((totalLista * 100) / total)

    plt.figure('Porcentagem do total de venda dos produtos no ano')
    plt.pie(perc, labels=labels, shadow=True,  autopct='%1.1f%%')
    plt.show()