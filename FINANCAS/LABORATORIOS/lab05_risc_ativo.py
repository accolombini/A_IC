"""
Neste laboratório, vamos avaliar o risco por trás de um ativo
"""

# Fazendo os imports

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2010-01-01'
    )['Adj Close']

print(f'\nDados da carteira. É importante que todos os papéis tenham a mesma '
      f'quantidade de informação')
print(f'\n{sec_data.info()}')
print(f'\nFazendo uma inspeção nos dados -> compare com os dados do site')
print(f'\n{sec_data.head()}')
print(f'\n{sec_data.tail()}')

# Vamos olhar para cada ativo individualmente, assim, o retorno logaritmico
# é mais interessante

print(f'\nCálculo do retoro logaritmico para cada ativo individualmente')

sec_returns = np.log(sec_data / sec_data.shift(1))
print(f'\n{sec_returns}')

# Agora vamos calcular a média e o desvio padrão das Ações
# O desvio padrão pode ser chamado de risco da Ação/ativo
# Ao maior desvio padrão, atribui-se uma maior volatilidade ao ativo

# Vamos primeiramente calcular o Risco das ações da PG
print(f'\n------------------------------ SEPARADOR ----------------------------------')
print(f'\nA media diaria das ações da PG é: {sec_returns["PG"].mean()}')
print(f'A media anual das ações da PG é: {sec_returns["PG"].mean() * 250}')
print(f'O desvio padrão diario das ações da PG é: {sec_returns["PG"].std()}')
print(f'O desvio padrão das ações da PG é: {sec_returns["PG"].std() * 250 ** 0.5}')

# Calculando agora para as ações da BEI.DE

print(f'\nA media diaria das ações da BEI.DE é: {sec_returns["BEI.DE"].mean()}')
print(f'A media anual das ações da BEI.DE é: {sec_returns["BEI.DE"].mean() * 250}')
print(f'O desvio padrão diario das ações da BEI.DE é: {sec_returns["BEI.DE"].std()}')
print(f'O desvio padrão das ações da BEI.DE é: '
      f'{sec_returns["BEI.DE"].std() * 250 ** 0.5}')

print(f'\nVamos melhorar a visulaização colcando a média e o desvio '
      f'padrão dos ativos um abaixo do outro')
print(f'\nA media anual das ações da PG é: {sec_returns["PG"].mean() * 250}')
print(f'A media anual das ações da BEI.DE é: {sec_returns["BEI.DE"].mean() * 250}')

# O mesmo resultado acima, utilizando uma forma mais elgante, mais PAYTHÔNICA

print(f'\nA média anual dos ativos -> PG BEI.DE:')
print(f'{sec_returns[["PG", "BEI.DE"]].mean() * 250}')

print(f'\nO desvio padrão anual dos ativos -> PG BEI.DE:')
print(f'{sec_returns[["PG", "BEI.DE"]].std() * 250 ** 0.5}')
