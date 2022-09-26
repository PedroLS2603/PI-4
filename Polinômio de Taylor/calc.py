import math as m
import re
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

def raiz_otimizada(valor, a, n_max=20):

    if valor == 1:
        return 1
    elif valor == 8:
        return 2
    elif valor == 27:
        return 3
    elif valor == 64:
        return 4
    elif valor == 125:
        return 5
    elif valor == 216:
        return 6

    potenciaIni = 1/3
    coeficienteIni = 1
    x = coeficienteIni * (a ** potenciaIni)
    for i in range(1, n_max):
        eq = df_dx(i, potenciaIni, coeficienteIni)
        coeficiente = eq[0]
        potencia = eq[1]
        x += ((coeficiente * (a ** potencia)) / m.factorial(i)) * ((valor - a) ** i)
        
    return x

def raiz_simples(a, x, n_max=20):
    denominador = 1
    valor = a ** (1/3)
    for n in range(1, n_max):
        numerador = 1
        for i in range(1, n -1):
            numerador *= (3 * n ) - (3 * i + 1)

        numerador *= (x - a) ** n 
       
        
        denominador = (3 ** n) * (a ** ((3 * n - 1)/3))
        denominador *= m.factorial(n)

        valor += numerador /denominador

    return valor

def grafico_func(a, n_max=20):
    limite = 50
    x = np.linspace(-limite, limite, 100)

    y1 = np.cbrt(x)
    y2 = []
    y3 = []

    for valor in x: 
        y2.append(raiz_simples(x=valor, a=a, n_max=n_max))

    for valor in x:
        y3.append(raiz_otimizada(a=a, valor=valor, n_max=n_max))


    plt.ylim(top=6)
    plt.ylim(bottom=-5)
    plt.plot(x, y1, linewidth=2.0, label="Numpy")
    plt.plot(x, y2, linewidth=2.0, label="Taylor")
    plt.plot(x, y3, linewidth=2.0, label="Taylor otimizada")

    plt.legend()
    plt.grid()
    
    plt.show()


    plt.plot(x, y2)



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