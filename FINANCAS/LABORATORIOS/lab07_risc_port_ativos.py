"""
Neste laboratório vamos trabalhar com a Covariância e a Correlação de Ativos

        -   Estamos interessados em saber qual o Risco por trás de uma carteira de Ativos
        -   Continuaremos com os mesmos papéis PG e BEI.DE
        -   O período para análise será 2000-01-01 até hoje
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
        t, data_source='yahoo', start='2000-01-01'
    )['Adj Close']

print(f'\nDados da carteira -> Será oportuno se todos os tickets tenham a mesma quantidade de informação')
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

# Cálculo da variância do portfólio -> O código a seguir mostra um pouco do poder do Python
# Neste código estamos pegando a transposta de uma matriz e multiplicando por outra, observe.
# Fique atento, estamos realizando dois produtos de matrizes. Note também que esse cálculo
# foi elevado a 0.5, necessário para encontrar a volatilidade

pfolio_vol = (np.dot(weights.T, np.dot(
    sec_returns.cov() * 250, weights
))) ** 0.5

print(f'\nA volatilidade do Portfólio: {pfolio_vol: .8f}')
print(f'\nA volatilidade do Portfólio formatada: {str(round(pfolio_vol * 100, 5)) + " %"}')
