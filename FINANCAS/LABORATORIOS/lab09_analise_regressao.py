"""
Neste laboratório vamos trabalhar com Análise de Regressão

        -   Ela quantifica a relação entre uma variável chamada de variável dependente
            e uma ou mais varíavel chamada de variável(eis) explicativas (variáveis
            independentes)
        -   É útil quando queremos prever uma variável dependente no futuro com a ajuda de
            dados históricos
        -   A equação para uma regressão simples é a equação de uma reta, sendo escrita
            da seguinte forma: y = α + β χ
        -   Vamos trabalhar com a Regressão dos Mínimos Múltiplos Quadrados, também
            conhecido como OLS
        -   Você poderá ser solicitado a instalar dois novos módulos:
            1- pip install statsmodels
            2- pip install scipy

"""

import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

# Nesta base de dados temos: Preço da Casa, Tamanho do Imóvel, Estado onde se Localizam
# Número de Quartos e Ano de construção

data = pd.read_excel('C:/Users/accol/OneDrive/UNIVERSIDADES/UFF/AULAS/AEAD_2020_1'
                     '/TEE00135_AN_INV/LAB_TEE00135/Housing.xlsx')

print(f'\nConhecendo os dados históricos Tamanho x Preço de imóveis:\n{data}')

# Restringindo data a dois atributos -> Preço da Casa e Tamanho da Casa
# Nosso objetivo será regredir o tamanho de uma casa a seu preço, para isso trabalharemos
# com apenas dois atributos "House Price" e "House Size (sq.ft.)"

print(f'\nVerificando nossa tabela a ser usada na regressão linear Simples:'
      f'\n{data[["House Price", "House Size (sq.ft.)"]]}')

# Regressão Simples em Python -> Univariável

X = data['House Size (sq.ft.)']  # X será nossa variável independente (variável previsora)
Y = data['House Price']  # Y será nossa variável dependente (o que queremos prever)

print(f'\nOlhando para nossa variável independente ou previsora -> X:\n{X}')
print(f'\nOlhando para nossa variável dependente -> Y:\n{Y}')

# Usando matplotlib faremos uma observação gráfica do nosso problema
# O objetivo aqui é mostrar algum cuidado que devemos ter, que se não
# forem observados nos levarão a conclusões equivocadas -> obeserve o gráfico

plt.scatter(X, Y)
plt.show()

# Percebeu o problema, pois é precisamos reorganizar os eixos para uma
# visualização mais precisa do nosso gráfico => observe

plt.scatter(X, Y)
plt.axis([0, 2_500, 0, 1_500_000])
plt.show()

# Melhorando nosso gráfico, vamos nomear nossos Eixos

plt.scatter(X, Y)
plt.axis([0, 2_500, 0, 1_500_000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')
plt.show()

# Agora faremos uma regressão em Python -> Calculando Alfa (α), Beta (β) e R quadrado
# y = α + βχ + erro

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

print(f'\nO valor de slope é:\n{slope}')
print(f'\nO valor de intercept é:\n{intercept}')
print(f'\nO valor de r_value é:\n{r_value}')
print(f'\nO valor de r_value quadrado é:\n{r_value ** 2}')
print(f'\nO valor de p_value é:\n{p_value}')
print(f'\nO valor de std_err é:\n{std_err}')

# Podemos assim escrever nossa equação de regressão:
# Y = 260806.2360560964 + 401.91628631922595*X +/- 65.24299510636492
