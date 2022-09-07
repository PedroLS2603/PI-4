import matplotlib.pyplot as plt
import numpy as np
import util as u
import grafico as g

mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
# Gráfico 1 - Total de produtos Vendidos por mês - Linha
# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras
# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)
# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto
graficoCreme = g.Grafico('Creme facial', mes, creme_facial)
graficoLimpeza = g.Grafico('Limpeza facial', mes, limpeza_facial)
graficoPasta = g.Grafico('Pasta dentária', mes, pasta_dentaria)
graficoSabonete = g.Grafico('Sabonete', mes, sabonete)
graficoShampoo = g.Grafico('Shampoo', mes, shampoo)
graficoHidratante = g.Grafico('Hidratante', mes, hidratante)


u.total_vendas_por_mes(mes, creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante)
u.vendas_de_produtos_por_mes(graficoCreme, graficoLimpeza, graficoPasta, graficoSabonete, graficoShampoo, graficoHidratante)
u.comparativo_por_mes(graficoCreme, graficoLimpeza)
u.hist_faixa_qtd_por_mes(sabonete)
u.perc_quantidade_por_ano(creme_facial, limpeza_facial, pasta_dentaria, sabonete, shampoo, hidratante)
