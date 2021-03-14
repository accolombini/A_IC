"""
Neste laboratório vamos trabalhar com a taxa de retorno simples de um ativo.

    REQUISITOS:     - para este laboratório precisaremos de alguns módulos Python
                    - será preciso -> numpy
                    - será preciso -> pandas
                    - será preciso -> matplotlib
                    - onde buscar pelos módulos: https://pypi.org/
                    - usaremos para análise o site: https://finance.yahoo.com/
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
from pandas_datareader import data as wb  # Nos permite ir ao yahoofinance e baixar os dados necessários
import matplotlib.pyplot as plt  # Nós plotamos os gráficos

# Nosso papel é avaliar a PG

# O que queremos -> baixar 25 anos de movimentação financeira da PG
PG = wb.DataReader('PG', data_source='yahoo', start='1995-01-01')

# Visualizar se tivemos ou não sucesso, cuidado o ticket é importante
print(f'{PG.head()}')
print(f'{PG.tail()}')

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(f'{PG["simple_return"].head(10)}')
print(f'{PG["simple_return"].tail(10)}')

# Vamos fazer uma análise gráfica desse período => retorno diário

PG['simple_return'].plot(figsize=(8, 5))  # Exibe a variação do rendimento diário do papel
plt.show()

# Faremos o cálculo da média diária

avg_return_d = PG['simple_return'].mean()
# print(avg_return_d)
print(f'\nA média diária calculada é -> {avg_return_d}')

# Faremos o cálculo da média anual -> 365 - 360 -> pregão -> 250, 251, 252

avg_return_a = PG['simple_return'].mean() * 250
print(f'\nA média anual calculada é -> {avg_return_a}')

print(f'\nA média anual em porcentagem -> {str(round(avg_return_a, 5) * 100) + "%"}')
