"""
Neste laboratório vamos continuar a partir do laboratório anterios

        -   Estamos interessados analisar o risco Sistemático (Diversificável) e o risco
            Idiossincrático (Não Diversificável), com isso queremos separar o Risco Diversificável
            do Risco não Diversificável de um portfólio de investimentos
        -   Continuaremos com os mesmos papéis PG e BEI.DE
        -   O período para análise será 2010-01-01 até hoje
        -   Vamos considerar também que nossa carteira é igualmente ponderada, 50% x 50%

"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# import matplotlib.pyplot as plt


tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2010-01-01'
    )['Adj Close']

print(f'\nDados da carteira -> Será oportuno se todos os tickets tenham a '
      f'mesma quantidade de informação')

print(f'\n{sec_data.info()}')

print(f'\nOlhando para os dados para conferência com o site do Yahoo')
print(f'\nOlhando os primeiros registros:\n{sec_data.head()}')
print(f'\nOlhando os últimos registros:\n{sec_data.tail()}')

# Estaremos analisando cada ativo individualmente, neste caso, é mais interessante usar
# o retorno logaritmico

print(f'\nCálculo do retorno logaritmico, mais interessante para este tipo de '
      f'análise.\n----------------------------------------------------------------------------\n')

sec_returns = np.log(sec_data / sec_data.shift(1))

print(f'\nO retorno logaritmico do ativo é: \n{sec_returns}')

# Vamos trabalhar com uma carteira balanceada => 50% para cada ativo
# Para isso, vamos salvar os pesos numa matriz numpy -> observe a seguir:

weights = np.array([0.5, 0.5])

print(f'\nOlhando para os pesos:\n{weights[0]} ou 50%\n{weights[1]} ou 50%')

# Cálculo da variância do portfólio -> O código a seguir mostra um pouco do poder do Python
# Neste código estamos pegando a transposta de uma matriz e multiplicando por outra, observe.
# Fique atento, estamos realizando dois produtos de matrizes. Note também que esse cálculo
# foi elevado a 0.5, necessário para encontrar a volatilidade

pfolio_var = (np.dot(weights.T, np.dot(
    sec_returns.cov() * 250, weights
))) ** 0.5

print(f'\n---------------------------------lab08 início---------------------------------------\n')

# O Risco diversificável anual = variância do portfólio - variância anual ponderada

# A seguir vamos criar uma estrutura para o cálculo anual da variância de cada empresa

PG_var_a = sec_returns[['PG']].var() * 250  # Cálculo da variância anual da PG

print(f'\nO valor de PG_var_a é:\n{PG_var_a}')

BEI_var_a = sec_returns[['BEI.DE']].var() * 250   # Cálculo da variância anual da BEI.DE

print(f'\nO valor de BEI_var_a é:\n{BEI_var_a}')

# A seguir calcularemos o risco diversificável, sendo sua expressão dada por:

# risco diversificável = variância do portfólio - variância anual ponderada

# Embora correta, devemos esperar um resultado incorreto, observe a seguir:

dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)

# print(f'\nO valor de dr é:\n{dr}')  # BEI.DE   NaN, PG       NaN

# Esperavamos um número e recebemos como retorno NaN. Este problema remete a um cuidado que
# devemos ter ao trabalhar com objetos Numpy

# Há duas formas para resolver esse problema, farei uma para cada ativo -> acompanhe

print(f'\nCorrigindo o problema para a PG, método 1:\n{float(PG_var_a): .6f}')

PG_var_a = sec_returns['PG'].var() * 250  # Uso [] para indicar que trabalharemos com dados apenas da PG

print(f'\nCorrigindo o problema para a PG, método 2:\n{PG_var_a: .6f}')

# Agora vamos corrigir o problema para a BEI.DE, observe que bastava termos trabalhado
# um colchete na expressão acima

BEI_var_a = sec_returns['BEI.DE'].var() * 250  # Uso [] para indicar que trabalharemos com dados apenas da BEI.DE

print(f'\nCorrigindo o problema para a BEI.DE, método 2:\n{BEI_var_a: .6f}')

# A seguir vamos calcular o risco não diversificável

dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)

print(f'\nConhecendo o valor de dr:\n{dr}')

print(f'\nO risco não diversificável (arredondando dr) é:\n{str(round((dr * 100), 3)) + "%"}')

# Cálculo do Risco não sistemático -> diferença entre pfolio_var e dr
# Aqui note que podemos calcular de duas formas diferentes. Se subtrairmos o Risco Não Sistemático
# de Toda Variância ou se somarmos as variâncias anuais ponderadas teremos o mesmo resultado

n_dr_1 = pfolio_var - dr

print(f'\nO valor do Risco não Sistemático forma 1 é:\n{n_dr_1}')

n_dr_2 = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a)

print(f'\nO valor do Risco não Sistemático forma 2 é:\n{n_dr_2}')
