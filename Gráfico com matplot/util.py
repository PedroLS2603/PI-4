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



def hist_faixa_qtd_por_mes():
    pass

def perc_quantidade_por_ano():
    pass