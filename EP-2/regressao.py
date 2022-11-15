import numpy as np


def sigmoide(x1, x2, a, b, c):
    return 1.0 / (1.0 + np.exp(-(a * x1 + b * x2 + c)))

def cross_entropy(z, estimativa):
    n = len(z)

    somatorio = np.sum(-(z * np.log(estimativa) + (1 - z) * np.log(1 - estimativa))) 

    return somatorio/n

def desc_gradiente(x1, x2, z, iteracoes = 100000, alpha = 1e-6, parada=1e-7):
    n = float(len(z)) 

    #Coeficientes iniciais
    a = 1e-2
    b = 1e-2
    c = 1e-3

    #Perda
    loss = []
    prev_loss = float('inf')
    curr_loss = 0

    
    #Variações
    var_a = []
    var_b = []
    
    #Contador de iterações
    count = 0


    for i in range(iteracoes):
        estimativa = sigmoide(x1,x2,a,b,c)        
        curr_loss = cross_entropy(z,estimativa)
        
        var_a.append(a)
        var_b.append(b)

        if abs(prev_loss - curr_loss) <= parada:
            count = i
            return a, b, c, loss, var_a, var_b, count

        #Atualizando perdas
        loss.append(curr_loss)
        prev_loss = curr_loss

        derivada_a = np.sum(x1 * (estimativa - z)) / n 
        derivada_b = np.sum(x2 * (estimativa - z)) / n 
        derivada_c = np.sum(estimativa - z) / n 

        a -= (alpha * derivada_a)
        b -= (alpha * derivada_b)
        c -= (alpha * derivada_c)

        count = i
        
    return a, b, c, loss, var_a, var_b, count

