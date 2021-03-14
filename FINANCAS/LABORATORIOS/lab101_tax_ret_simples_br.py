"""
Neste laboratório vamos trabalhar com a taxa de retorno simples de um ativo.

    REQUISITOS:     - para este laboratório precisaremos de alguns módulos Python
                    - será preciso -> numpy
                    - será preciso -> pandas
                    - será preciso -> matplotlib
                    - onde buscar pelos módulos: https://pypi.org/
                    - usaremos para análise o site: https://finance.yahoo.com/
                    - PANDAS-DATAREADER:
                     https://readthedocs.org/projects/pandas-datareader/downloads/pdf
                     /latest/
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Nosso papel é avaliar a VALE3

# O que queremos -> baixar 25 anos de movimentação financeira da VALE3
VALE3 = wb.DataReader('VALE3.SA', data_source='yahoo',
                      start='2000-01-01')

# Visualizar se tivemos ou não sucesso, cuidado o ticket é importante
print(f'{VALE3.head(2)}')
print(f'{VALE3.tail(2)}')

# Retorno simples = papel_dia/papel_dia_anterior - 1

VALE3['simple_return'] = (VALE3['Adj Close'] / VALE3['Adj Close'].shift(1)) - 1
print(f'{VALE3["simple_return"].head(20)}')
print(f'{VALE3["simple_return"].tail(20)}')

# Vamos fazer uma análise gráfica desse período => retorno diário

VALE3['simple_return'].plot(figsize=(8, 5))  # Exibe a variação do rendimento diário do papel
plt.show()

# Faremos o cálculo da média diária

avg_return_d = VALE3['simple_return'].mean()
# print(avg_return_d)
print(f'A média diária calculada é -> {avg_return_d}')

# Faremos o cálculo da média anual -> 365 - 360 -> pregão -> 250, 251, 252

avg_return_a = VALE3['simple_return'].mean() * 250
print(f'A média anual calculada é -> {avg_return_a}')

print(f'A média anual em porcentagem -> {str(round(avg_return_a, 5) * 100) + "%"}')
