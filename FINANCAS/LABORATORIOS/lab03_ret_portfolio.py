"""
Neste laboratório vamos extender os conceitos de retorno sobre o investimento, considerando um
portfólio de ações.
        NOTA:   o ponto aqui é encontrar o ótimo para sua carteira se tornar equilibrada e
                com retorno máximo
                Nosso portfólio será composto por:  PG   -> Procter Gamble
                                                    MSFT -> Microsoft
                                                    F    -> Ford
                                                    GE   -> General Eletric
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Criando as variáveis tickers e mydata
tickers = ['PG', 'MSFT', 'F', 'GE']  # <class 'list'>
# print(f'O tipo de tickers é -> {type(tickers)}')
mydata = pd.DataFrame()  # -> PG MSFT F GE | valores que extrair
# print(f'O tipo de tickers é -> {type(mydata)}')  # <class 'pandas.core.frame.DataFrame'>

# Buscando as informações no yahoo para a composição do DataFrame
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

# Visualizando os dados extrair do yahoo finance

print(f'\n----------------------Início dos Resultados---------------------------')
print(f'Resumo do DataFrame\n-------------------------------------------------------')
# print(f'{mydata.info()}\n')  # .info() é um método que retorna todas as probliedades do objeto -> mydata
print(f'Informações do DataFrame HEAD\n{mydata.head()}')
print(f'Informações do DataFrame TAIL\n{mydata.tail()}')

# Vamos gerar um gráfico de linhas para avaliar o comportamento destes papéis
# Para normalizar o gráfico vamos normalizar os preços da ações para base 100
# A normalização será feita usando Pl / P0 * 100 => preço no dia 3/1/1995 => fixo =>> iloc[0]

# O método iloc[0] nos devolve o preço dos papéis no primeiro instante analisado -> 1995 => 3/1/1995

print(f'\nPara conferir o retorno de iloc confira com HEAD\n{mydata.iloc[0]}')

# Para normalizar, vamos então dividir todo conteúdo de mydata por maydata.iloc[0] e
#  multiplicar por 100

(mydata / mydata.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Para poder comparar vamos imprimir o mesmo gráfico sem a normalização, fins didáticos apenas

# mydata.plot(figsize=(15, 6))
# plt.show()

# Nota sobre Python -> loc e iloc levam ao mesmo resultado, mas devem ser expressos
# da forma com segue -> observe os resultados:

print(f'\n--------------------------------OBS PYTHON-------------------------------')
print(f'Com loc temos o resultado\n{mydata.loc["1995-01-03"]}')
print(f'\nCom iloc o resultado é\n{mydata.iloc[0]}')

# Cálculo do retorno de simples desta carteira de ativos vamos criar uma nova tabela
# Os cálculos são os mesmos já vistos, só que agora aplicados a uma matriz numpy

returns = (mydata / mydata.shift(1)) - 1  # ret = ph / po - 1
print(f'\n-------------------- Olhando para o retorno simples --------------------')
print(f'{returns.head()}')
print(f'{returns.tail()}')

# Da nossa teoria, lembra, precisamos atribuir pesos aos nossos ativos, inicialmente,
# vou considerar pesos iguais. Vamos usar o método numpy dot() que nos permite calcular
# produtos vetoriais ou de matrizes de forma "mágica"

weights = np.array([0.25, 0.25, 0.25, 0.25])
print(f'\n------------------- Retorno levando em conta os pesos --------------')
print(f'{np.dot(returns, weights)}')

# O retorno não é muito interessenta visulamente, observe que temos uma lista gigantesca
# de dados, que você pode perceber pela presença dos 3 prontos .... Precisamos
# melhorar isso

# Novamente vamos calcular a taxa de retorno anual da carteira, isso
# multiplicaremos por 250 a média dos retornos

annaul_returns = returns.mean() * 250
print(f'\nRetorno médio anual da carteira de ações')
print(f'{annaul_returns}')

# Aplicaremos os pesos no retorno médio anual, para avaliar o rendimento
# da nossa carteira

print(f'\nRetorno médio da carteira considerando os pesos\n'
      f'{np.dot(annaul_returns, weights)}')

pfolio_1 = str(round((np.dot(annaul_returns, weights)) * 100, 5)) + " %"
print(f'\nO portifólio 1 resulta num ganho de:\n{pfolio_1}')

# A ideia agora é que você possa variar os pesos de seus ativos para
# encontrar a melhor carteira. Não se impolgue, lembre-se que há o equilibiro
# Risco x Retorno que deve ser levado em consideração. Vamos usar os pesos
# definidos na nossa aula teórica

weights_2 = np.array([0.4, 0.4, 0.15, 0.05])

print(f'\n------------------- Retorno levando em conta outros pesos --------------')
print(f'{np.dot(returns, weights_2)}')

# Cálculo do portifólio 2

pfolio_2 = str(round((np.dot(annaul_returns, weights_2)) * 100, 5)) + " %"
print(f'\nO portifólio 2 resulta num ganho de:\n{pfolio_2}')
