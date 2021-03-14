""""
Neste laboratório, vamos trabalhar com alguns índices consagrados no mercado, serão eles:

        - ^GSPC -> S & P 500
        - ^IXIC -> Nasdaq
        - ^GDAXI -> DAX Alemanha
        - ^BSVP -> BOVESPA
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Nesta prática queremos avaliar os índices de mercado
# Nossa variável tickers será uma lista de índices

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^RUT']

print(f'\nNossa variável tickers -> {tickers} - seu tipo é -> {type(tickers)}')

ind_data = pd.DataFrame()

print(f'\nNossa variável ind_data -> {ind_data} - seu tipo é -> {type(ind_data)}')

# Percorrendo nossa lista de índices e buscando dados no yahoo finance desde 1/1/1995
# t -> variável do índice -> percorrer a lista

for t in tickers:
    ind_data[t] = wb.DataReader(
        t, data_source='yahoo', start='1995-01-01'
    )['Adj Close']

print(f'\nÉ importante que todos os tickets tenham a mesma quantidade de informação')
print(f'\nResumo do dataFrame:\n{ind_data.info()}')
print(f'\nInspecionando o cabeçalho do dataFrame:\n{ind_data.head()}')
print(f'\nInspecionando a calda do dataFrame:\n{ind_data.tail()}')

# Para efeito de análise precisamos normalizar estes dados
# Vamos normalizar para a base 100 e plotar o gráfico

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Vamos avaliar o efeito da não normalização dos índices

ind_data.plot(figsize=(15, 6))
plt.show()

# Vamos avaliar o retorno simples dos índices analisados -> como fizemos para as ações

returns = (ind_data / ind_data.shift(1)) - 1
print(f'\nAnalisando só os dados mais recentes: \n{returns.tail()}')

# Cálculo do retorno médio anual dos índices analisados

anual_ind_returns = returns.mean() * 250
print(f'\nO retorno médio anual dos índices é:\n{anual_ind_returns}')

# Tornando mais amigável o retorno anual -> formatando a saída

anual_decimal = str(round(anual_ind_returns * 100, 5))
print(f'\nExibe o retorno médio anual dos índices em valores percentuais:\n{anual_decimal}')

# Agora um passo muito importante, vamos pegar uma ação e comparar com o índice.
# Vamos inicialmente comparar a PG com o índice S & P 500
# Depois disso vamos incluir o índice DJI

tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.DataReader(
        t, data_source='yahoo', start='1995-1-1'
    )['Adj Close']

# Inspecionando os dados mais recentes

print(f'\nDados mais recebtes:\n{data_2.tail()}')

# A seguir normalizamos para a Base 100 e plotamos o gráfico

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()
