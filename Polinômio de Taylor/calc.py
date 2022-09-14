import math as m
import numpy as np
import matplotlib.pyplot as plt

def str_poli_taylor(a, n_max=20):
    potenciaIni = 1/3
    coeficienteIni = 1
    i = 1

    str = '{0}'.format(round(coeficienteIni * (a ** potenciaIni), 2))
    while i <= n_max:
        eq = df_dx(i, potenciaIni, coeficienteIni)
        coeficiente = eq[0]
        potencia = eq[1]
        str += " + ({0})/{1}!).(x - {2})^{3}".format(round(coeficiente * (a ** potencia), 2), i, a, i)
        i += 1
    return str 

def poli_taylor(valor, a, n_max = 20):
    potenciaIni = 1/3
    coeficienteIni = 1
    i = 1
    x = coeficienteIni * (a ** potenciaIni)
    
    while i <= n_max:
        eq = df_dx(i, potenciaIni, coeficienteIni)
        coeficiente = eq[0]
        potencia = eq[1]
        x += ((coeficiente * (a ** potencia)) / m.factorial(i)) * ((valor - a) ** i)
        i += 1
    
    return x

def grafico_func(a, n_max=20):
    y1 = []
    x = np.linspace(0, 100)


    y2 = np.cbrt(x)
    for valor in x:
        y1.append(poli_taylor(valor, a, n_max))

    plt.ylim(top=10)
    plt.xlim(right=14)

    print(y1)
    plt.plot(x, y1)
    plt.plot(x, y2)

    plt.legend(["Taylor","Numpy"])
    plt.grid()
    plt.show()

# derivação de função potência

def df_dx(ordem, potencia, coeficiente = 1):    
    i = 0
    while i < ordem:
        coeficiente *= potencia
        potencia -= 1
        i += 1
        if(potencia == 0):
            potencia = 0
            break

    elementos = [coeficiente, potencia]

    return elementos