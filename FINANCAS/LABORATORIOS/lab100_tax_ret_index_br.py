"""

Neste laboratório, vamos trabalhar com alguns índices consagrados no mercado nacional
serão eles:

        - ^BVSP -> BOVESPA

Também vamos trabalhar com os seguintes papéis:

        - CMIG3 - CEMIG
        - SUZB3 - SUZANO PAPÉIS E CELULOSE

"""
# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Nesta prática queremos avaliar os índices de mercado
# Nossa variável tickers será uma lista de índices

tickers = ['^BVSP']

ind_data = pd.DataFrame()

# Percorrendo nossa lista de índices e buscando dados no yahoo finance desde 1/1/2010

for t in tickers:
    ind_data[t] = wb.DataReader(t, data_source='yahoo',
                                start='1995-01-01')['Adj Close']


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
print(f'\nAnalisando só os dados mais recentes; \n{returns.tail()}')

# Cálculo do retorno médio anual dos índices analisados

anual_ind_returns = returns.mean() * 250
print(f'\nO retorno médio anual dos índices é:\n{anual_ind_returns}')

# Tornando mais amigável o retorno anual -> formatando a saída

anual_decimal = str(round(anual_ind_returns * 100, 5))
print(f'\nExibe o retorno médio anual dos índices em valores percentuais:\n{anual_decimal}')

# Agora um passo muito importante, vamos pegar uma ação e comparar com o índice.
# Vamos inicialmente comparar a TAEE11 com o índice BOVESPA e IEE

tickers = ['CMIG3.SA', 'SUZB3.SA', '^BVSP']
data_2 = pd.DataFrame()


for t in tickers:
    data_2[t] = wb.DataReader(
        t, data_source='yahoo', start='2010-1-1'
    )['Adj Close']


# Inspecionando os dados mais recentes

print(f'\nDados mais recebtes:\n{data_2.tail()}')

# A seguir normalizamos para a Base 100 e plotamos o gráfico

(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()
