from scipy.stats import norm, expon


# listas de horários de chegada e saída dos consultórios
chegadas, saidas = [],[]
# listas de horários de chegada e saída das filas
in_queue, in_system  = [],[]
# tempo na fila e tamanho das fulas
horarios_nas_filas, tamanho_da_fila = [],[]

MEDIA_DE_CHEGADA_PACIENTE = 5
MEDIA_DO_TEMPO_DE_ATENDIMENTO = 3.0
DESVIO_PADRAO_DO_TEMPO_DE_ATENDIMENTO = 0.5

def chegada_paciente(env, medicos):
    # ID para cada paciente
    paciente_id = 0

    while True:
       ## tempo de chegada do proximo paciente
       tempo_proximo_paciente = distribuicao_chegada_pacientes()
       # espera pelo próximo paciente
       yield env.timeout(tempo_proximo_paciente)

       # paciente chegou, marca o tempo e guarda o tempo de chegada
       tempo_de_chegada = env.now
       chegadas.append(tempo_de_chegada)
       paciente_id += 1
       print('%3d chegou no posto em %.2f' % (paciente_id, tempo_de_chegada))
       
       # executa o atendimento
       env.process(atendimento(env, paciente_id, tempo_de_chegada, medicos=medicos))

def salva_info_da_fila(env, balanca):
    horario_medicao = env.now
    tamanho_da_fila_agora = len(balanca.queue)
    horarios_nas_filas.append(horario_medicao)
    tamanho_da_fila.append(tamanho_da_fila_agora)

    return horario_medicao

def distribuicao_chegada_pacientes():
  tempo_proximo_paciente = expon.rvs(scale = MEDIA_DE_CHEGADA_PACIENTE, size = 1)
  return tempo_proximo_paciente

def calcula_tempo_no_sistema(env, horario_chegada):
  horario_saida = env.now
  saidas.append(horario_saida)
  tempo_total = horario_saida - horario_chegada
  in_system.append(tempo_total)



# pega o tempo de atendimento
def tempo_de_atendimento_paciente():
  return norm.rvs(loc = MEDIA_DO_TEMPO_DE_ATENDIMENTO, 
                  scale = DESVIO_PADRAO_DO_TEMPO_DE_ATENDIMENTO, 
                  size = 1)


def atendimento(env, paciente_id, horario_chegada, medicos):
    with medicos.request() as req:
        print('%3d entrou na fila em %.2f' % (paciente_id, env.now))
        horario_entrada_da_fila = salva_info_da_fila(env, medicos)
        yield req # espera o médico estar disponível

        print('%3d saiu da fila em %.2f' % (paciente_id, env.now))
        horario_saida_da_fila = salva_info_da_fila(env, medicos)

        # tempo que ficou na fila
        tempo_na_fila = horario_saida_da_fila - horario_entrada_da_fila
        in_queue.append(tempo_na_fila)

        # Execução de atendimento do paciente
        tempo_atendimento = tempo_de_atendimento_paciente()
        yield env.timeout(tempo_atendimento)
        print('%3d permaneceu por %.2f' % (paciente_id, tempo_atendimento))

        # tempo total da operacao de atendimento + fila
        calcula_tempo_no_sistema(env, horario_chegada)