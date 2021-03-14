"""
Este laboratório é apenas para demonstrar como você pode importar uma arquivo no
formato .csv e efetuar seu trabalho normalmente no Python.
Este não é um laboratório no contexto do curso, apenas um extra para aqueles(as)
que queiram se aprofundar no conhecimento do Python.

Para esta prática você precisará ter instalado no seu ambiente virtual
os módulos: openpyxl e xlrd

        - pip install openpyxl
        - pip install xlrd

    Uma fonte alternativa para coleta de dados, no formato .csv é o:
    https://www.infomoney.com.br/cotacoes/iee/historico/


"""

import pandas as pd

# Lendo de um arquivo .csv no diretório corrente

mydata = pd.read_csv('índice de energia elétrica Dados Históricos.csv')

print(f'\n--------------------------------------------------------\n'
      f'Olhando para nosso índice em csv:\n{mydata.head()}\n{mydata.tail()}')

# Escrevendo num arquivo .csv no diretório corrente

mydata.to_excel('h_iee.xlsx')

# Testando leitura no nosso arquivo .xlsx

mydata_novo = pd.read_excel('h_iee.xlsx')

print(f'\n----------------------------------------------\n'
      f'Olhando para nosso índice agora em xlsx:'
      f'\n{mydata_novo.head()}\n{mydata_novo.tail()}')
