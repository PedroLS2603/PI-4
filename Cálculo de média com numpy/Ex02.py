import numpy as np
import util as u

mediaAltura = 0
anos = np.loadtxt('anos.txt')
altura = np.loadtxt('altura.txt')

indices = u.filterIndex(anos >= 1998, anos <= 2005)

for indice in indices:
    mediaAltura += (altura[indice]/indices.size)
    
print(mediaAltura)