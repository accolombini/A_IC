"""
Neste laboratório vamos trabalhar com a Covariância e a Correlação de Ativos utilizando Python

        -   A Covariância entre uma varíavel e ela própria é a na verdade a Variância dessa variável
            Assim ao longo da diagonal principal da matriz de Covariância teremos a Variância das
            variáveis sob análise
            O restante da matriz será preenchido com as Covariâncias entre elas.
        -   No caso desse lab, as variáveis serão os preços das duas ações sob análise, portanto,
            esperamos uma matriz de Covariância de 2 x 2

        Para este lab, trabalharemos com dois ativos - um americano e o outro alemão, sendo
        ambos do mesmo segmento

            - PG -> Procter & Gamble
            - BEI.DE -> Beiersdorf
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# import matplotlib.pyplot as plt


tickers = ['PG', 'BEI.DE']  # tickers é uma lista que contém nossos ativo
print(f'Conhecendo minha variável tickers\n{type(tickers)}\n Seu conteúdo é: {tickers}')
# <class 'list'>
# Seu conteúdo é: ['PG', 'BEI.DE']
sec_data = pd.DataFrame()

print(f'Conhecendo minha variável sec_data\n{type(sec_data)}\nSeu conteúdo é: {sec_data}')
# <class 'pandas.core.frame.DataFrame'>
# Seu conteúdo é: Empty DataFrame
# Columns: []
# Index: []

for t in tickers:
    sec_data[t] = wb.DataReader(
        t, data_source='yahoo', start='2000-01-01'
    )['Adj Close']

print(f'\nDados da carteira -> Será oportuno que todos os tickets tenham a mesma quantidade de informação')
print(f'\n{sec_data.info()}')

print(f'\nOlhando para os dados para conferência com o site do Yahoo')
print(f'\nOlhando os primeiros registros:\n{sec_data.head(10)}')
print(f'\nOlhando os últimos registros:\n{sec_data.tail(10)}')

# Estaremos analisando cada ativo individualmente, neste caso, é mais interessante usar
# o retorno logaritmico

print(f'\nCálculo do retorno logaritmico, mais interessante para este tipo de '
      f'análise.\n----------------------------------------------------------------------------\n')

sec_returns = np.log(sec_data / sec_data.shift(1))  # todos os dados e dividindo pelo dia anterior

print(f'\nO retorno logaritmico do ativo é: \n{sec_returns}')

# O método var() do numpy calcula a variância diretamente
# Cálculo da variãncia diária

PG_var = sec_returns['PG'].var()

print(f'\nA variância por dia da PG é: {PG_var: .5f}')

BEI_var = sec_returns['BEI.DE'].var()

print(f'\nA variância por dia da BEI.DE é: {BEI_var: .5f}')

# Cálculo da variãncia anual

PG_var = sec_returns['PG'].var() * 250

print(f'\nA variância anual da PG é: {PG_var: .5f}')

BEI_var = sec_returns['BEI.DE'].var() * 250

print(f'\nA variância anual da BEI.DE é: {BEI_var: .5f}')

# Com o método cov() do pandas iremos calcular a covariância dos pares de colunas
# Para todas as matrizes => preste atenção aos resultados na diagonal principal e no caso
# fique atento as outras colunas, nossa matriz é 2x2, portanto, observe também a diagonal secundária
# Como dica => na diagonal principal teremos a Variância e na diagonal secundária teremos a Covariância
# Para grandes matrizes => o restante da matriz é preenchida com a Covariância entre as colunas, no caso
# (ativos analisados)

# Matriz de Covariância Diária
cov_matrix = sec_returns.cov()
print(f'\nMatriz de Covariância diária:\n{cov_matrix}')

# Matriz de Covariância Anual
cov_matrix_a = sec_returns.cov() * 250
print(f'\nMatriz de Covariância anual:\n{cov_matrix_a}')

# Com o método corr() do pandas estaremos calculando a correlação de pares de colunas
# Atenção! Correlação entre preços de ativos e correlação de retorno de ativos possuem
# resultados diferentes
# Fique atento, você não deve analisar a matriz de correlação e ela não deve ser
# multiplicada por 250

corr_matrix = sec_returns.corr()
print(f'\nA matriz de Correlação dos ativos é:\n{corr_matrix}')
# Muito cuidado aqui, o resultado na diagonal secundária não é a correlação entre os preços das
# duas ações. A corr(preços) versus a corr(retornos) normalmente possuem valores diferentes
# Nunca se esqueça => um investidor esta interessado no retorno das ações e não nos preços das ações
# Assim, cabe ao analista a interpretação dos resultados, isto não é competência do Python, ok!!!
