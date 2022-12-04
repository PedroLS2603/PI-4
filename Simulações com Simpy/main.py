import simpy
import numpy  as np
import simulador as sim
from simulador import chegadas, saidas, horarios_nas_filas, tamanho_da_fila
import matplotlib.pyplot as plt
import pandas as pd

TEMPO_DE_SIMULACAO  = 100

# Seed fixo. Assim, será o mesmo valor todas as vezes que executarmos
## selecting a random seed for the probability distributions
## defining the truck arrival process
np.random.seed(seed = 1)

## prepara o ambiente
env = simpy.Environment()

## Definindo recursos: Quantidade de balanças disponíveis
QTD_MEDICOS = 1
medicos = simpy.Resource(env, capacity = QTD_MEDICOS)

env.process(sim.chegada_paciente(env, medicos))

# Roda a simulação
env.run(until = TEMPO_DE_SIMULACAO)


tmpdf1 = pd.DataFrame(horarios_nas_filas, columns = ['horario'])
tmpdf2 = pd.DataFrame(tamanho_da_fila, columns = ['tamanho'])
tmpdf3 = pd.DataFrame(chegadas, columns = ['chegadas'])
tmpdf4 = pd.DataFrame(saidas, columns = ['partidas'])

df_tamanho_da_fila = pd.concat([tmpdf1, tmpdf2], axis = 1)
df_entrada_saida = pd.concat([tmpdf3, tmpdf4], axis = 1)

fig, ax = plt.subplots()
fig.set_size_inches(10, 5.4)

y1, x1 = list(df_entrada_saida['chegadas'].keys()), df_entrada_saida['chegadas']
y2, x2 = list(df_entrada_saida['partidas'].keys()), df_entrada_saida['partidas']

ax.plot(x1, y1, color='blue', marker="o", linewidth=0, label="Chegada")
ax.plot(x2, y2, color='red', marker="o", linewidth=0, label="Saída")

ax.set_xlabel('Tempo')
ax.set_ylabel('ID paciente')
ax.set_title("Chegada e saída dos pacientes no PS")
ax.legend()
plt.show()


fig, ax = plt.subplots()
fig.set_size_inches(10, 5.4)

ax.plot(df_tamanho_da_fila['horario'], df_tamanho_da_fila['tamanho'], color='blue', linewidth=1)
ax.set_xlabel('Tempo')
ax.set_ylabel('Tamanho da fila')
ax.set_title("Número de pacientes com {0} {1}".format(QTD_MEDICOS, 'médico' if QTD_MEDICOS == 1 else 'médicos'))
ax.grid()
plt.show()
