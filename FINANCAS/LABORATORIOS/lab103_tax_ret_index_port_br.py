""""
Neste laboratório, vamos trabalhar com alguns papéis consagrados no mercado, e analisá-los
conforntando-os com o índice BOVESPA:

        PETR3.SA -> PETROBRAS
        VALE3.SA -> VALE
        CMIG3.SA -> CMIG
        ^BVSP    -> ÍNDICE BOVESPA
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Nesta prática queremos avaliar os índices de mercado
# Nossa variável tickers será uma lista de índices

tickers = ['PETR3.SA', 'VALE3.SA', 'CMIG3.SA']

print(f'\nNossa variável tickers -> {tickers} - seu tipo é -> {type(tickers)}')

ind_data = pd.DataFrame()

print(f'\nNossa variável ind_data -> {ind_data} - seu tipo é -> {type(ind_data)}')

# Percorrendo nossa lista de índices e buscando dados no yahoo finance desde 1/1/1995
# t -> variável do índice -> percorrer a lista

for t in tickers:
    ind_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2005-01-01'
    )['Adj Close']

print(f'\nÉ importante que todos os tickets não contenham dados faltantes')
print(f'\nResumo do dataFrame:\n----------------------------------------------------------')
print(f'\n{ind_data.info()}')  # Sempre avaliem as informações referentes ao seu dataframe
print(f'\nInspecionando o cabeçalho do dataFrame:\n{ind_data.head()}')  # Confira na web
print(f'\nInspecionando a calda do dataFrame:\n{ind_data.tail()}')  # Confira na web

# Para efeito de análise precisamos normalizar estes dados
# Vamos normalizar para a base 100 e plotar o gráfico

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Vamos avaliar o efeito da não normalização dos índices

ind_data.plot(figsize=(15, 6))
plt.show()

# Vamos avaliar o retorno simples das ações analisadas

returns = (ind_data / ind_data.shift(1)) - 1
print(f'\nAnalisando só os dados mais recentes: \n{returns.tail()}')

# Cálculo do retorno médio anual das ações

anual_ind_returns = returns.mean() * 250
print(f'\nO retorno médio anual dos das ações:\n{anual_ind_returns}')

# Tornando mais amigável o retorno anual -> formatando a saída

anual_decimal = str(round(anual_ind_returns * 100, 5))
print(f'\nExibe o retorno médio anual das ações em valores percentuais:\n{anual_decimal}')

# Agora um passo muito importante, vamos pegar nosso conjunto de ações e comparar com o índice.
# O índice BOVESPA, por ser o que representa o mercado nacional foi o escolhido

tickers = ['PETR4.SA', 'VALE3.SA', 'CMIG3.SA', '^BVSP']
data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(
        t, data_source='yahoo', start='1995-1-1'
    )['Adj Close']

# -----------------------

ret = (data_2 / data_2.shift(1)) - 1
print(f'\nAnalisando só os dados mais recentes: \n{ret.tail()}')

# Cálculo do retorno médio anual das ações e índice BOVESPA

anual_ind_ret = ret.mean() * 250
print(f'\nO retorno médio anual dos das ações com o ^BVSP:\n{anual_ind_ret}')

# Tornando mais amigável o retorno anual -> formatando a saída

an_decimal = str(round(anual_ind_ret * 100, 5))
print(f'\nExibe o retorno médio anual das ações com o ^BVSP em valores percentuais:\n{an_decimal}')

# Inspecionando os dados mais recentes

print(f'\nDados mais recebtes:\n{data_2.tail()}')

# A seguir normalizamos para a Base 100 e plotamos o gráfico

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()
