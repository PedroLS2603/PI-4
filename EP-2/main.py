import regressao as regr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotErroPorIteracao(iteracoes, erros, titulo):
    x = range(iteracoes)
    plt.plot(x, erros)
    plt.xlabel("Iterações")
    plt.ylabel("Erro")
    plt.title(titulo)
    plt.show()


def plotData(data, label_x, label_y, label_pos, label_neg, title, axes=None, estimado=False):
    if not estimado:
        neg = (notas['resultado'] == 0)
        pos = (notas['resultado'] == 1)
    else:
        corte = 0.65
        neg = (notas['resultado'] < corte)
        pos = (notas['resultado'] >= corte)

    if axes == None:
        axes = plt.gca()
    axes.scatter(data[pos][["nota_1"]], data[pos][["nota_2"]], marker='+', c='k', s=60, linewidth=2, label=label_pos)
    axes.scatter(data[neg][["nota_1"]], data[neg][["nota_2"]], c='y', s=60, label=label_neg)
    axes.set_xlabel(label_x)
    axes.set_ylabel(label_y)
    axes.legend(frameon= True, fancybox = True)
    axes.set_title(title)
    plt.show()

notas = pd.read_csv('https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/notas-estudantes.csv')

x1 = np.array(notas['nota_1'], dtype=float)
x2 = np.array(notas['nota_2'], dtype=float)

z = np.array(notas['resultado'])

plotData(notas, 'Nota 1', 'Nota 2', 'Aprovado', 'Reprovado', title="Resultado original")

a, b, c, perdas, var_a, var_b, iteracoes = regr.desc_gradiente(x1=x1, x2=x2, z=z)
a, b, c, perdas2, var_a, var_b, iteracoes2 = regr.desc_gradiente(x1=x1, x2=x2, z=z, alpha = 1e-4, parada=1e-6)
a, b, c, perdas3, var_a, var_b, iteracoes3 = regr.desc_gradiente(x1=x1, x2=x2, z=z, alpha=1e-3, parada=1e-5)





print("a: {0}\nb: {1}\nc: {2}\niterações: {3}".format(a,b,c,iteracoes))


z_estimado = regr.sigmoide(x1,x2,a,b,c)
notas['resultado'] = z_estimado

#Gráfico de perda por iteração
plotErroPorIteracao(iteracoes, perdas, titulo="alpha = 1e-6, parada=1e-7")
plotErroPorIteracao(iteracoes2, perdas2, titulo="alpha = 1e-4, parada=1e-6")
plotErroPorIteracao(iteracoes3, perdas3, titulo="alpha = 1e-3, parada=1e-5")

plotData(notas, 'Nota 1', 'Nota 2', 'Aprovado estimado', 'Reprovado estimado',title="Resultado estimado", estimado=True)
