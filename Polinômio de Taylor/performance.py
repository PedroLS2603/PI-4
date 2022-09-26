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
a = 15


def tempo(x,n,a):
  ini = timeit.default_timer()
  valor = c.raiz_otimizada(valor=x, a=a, n_max=n)
  loss_function = np.power((valor - np.cbrt(x)), 2) 
  return (timeit.default_timer() - ini) * 1000 * 1000, loss_function

tempo_vector = np.vectorize(tempo)
for n in enes:
  tempos, erro = tempo_vector(x,n,a)
  medias[n-1] = np.mean(tempos)
  error[n-1] = np.sum(erro)/points


fig, ax = plt.subplots()
fig.set_size_inches(20,8)
ax.plot(enes, medias, linewidth=2.0)
ax.grid()
color = "blue"
ax.set_ylabel('tempo em ns', color=color)
ax.tick_params(axis='y', labelcolor=color)

ax2 = ax.twinx()

color = "red"
ax2.set_ylabel('Erro', color=color) 
ax2.plot(enes, error, color=color)

ax2.tick_params(axis='y', labelcolor=color)

plt.show()
