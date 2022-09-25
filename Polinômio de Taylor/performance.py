import numpy as np
import timeit
import calc as c
import matplotlib.pyplot as plt

n_max = 20
points = 100
enes = np.arange(1,n_max+1)
medias = np.zeros(n_max)
error = np.zeros(n_max)
x = np.linspace(-20, 20, points)

def tempo(x,n):
  ini = timeit.default_timer()
  valor = c.raiz_otimizada(valor=x, a=1)
  fim = timeit.default_timer()
  loss_function = pow(valor - np.cbrt(x),2)
  return fim - ini, loss_function

tempo_vector = np.vectorize(tempo)
for n in enes:
  print(n)
  calc, erro = tempo_vector(x,n)
  medias[n-1] = np.mean(calc)*1000*1000
  error[n-1] = np.sum(erro)/points


fig, ax = plt.subplots()
fig.set_size_inches(20,8)
ax.plot(enes, medias, linewidth=2.0)
ax.grid()
color = "blue"
ax.set_ylabel('tempo em ns', color=color)
ax.tick_params(axis='y', labelcolor=color)

ax2 = ax.twinx()

# plotando 2 gráficos com escalas diferentes
color = "red"
ax2.set_ylabel('Erro', color=color) 
ax2.plot(enes, error, color=color)

ax2.tick_params(axis='y', labelcolor=color)

plt.show()
