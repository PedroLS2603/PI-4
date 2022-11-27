import simpy
import numpy  as np
import simulador as sim

TEMPO_DE_SIMULACAO  = 100

# Seed fixo. Assim, será o mesmo valor todas as vezes que executarmos
## selecting a random seed for the probability distributions
## defining the truck arrival process
np.random.seed(seed = 1)

## prepara o ambiente
env = simpy.Environment()

## Definindo recursos: Quantidade de balanças disponíveis
QTD_MEDICOS = 3
medicos = simpy.Resource(env, capacity = QTD_MEDICOS)

env.process(sim.chegada_paciente(env, medicos))

# Roda a simulação
env.run(until = TEMPO_DE_SIMULACAO)