"""" 
Neste laboratório, continuaremos trabalhando com a taxa de retorno de simples
de um ativo, neste caso, usaremos a taxa logarítmica de retorno:

        - o que buscamos: log(Pt / (Pt_1)
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Nosso papel é avaliar a PG - em termos de retorno logarítmico

# O que queremos -> baixar 25 anos de movimentação financeira da PG
PG = wb.DataReader('PG', data_source='yahoo', start='1995-01-01')

# Visualizar se tivemos ou não sucesso, cuidado o ticket é importante
print(f'{PG.head(2)}')
print(f'{PG.tail(2)}')

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1

print(f'{PG["simple_return"].head(2)}')
print(f'{PG["simple_return"].tail(2)}')

# Cálculo do retorno logaritmico

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(f'{PG["log_return"]}')

# Vamos agora plotar o gráfico do retorno logarítmico

PG['log_return'].plot(figsize=(8, 5))
plt.show()

# Calculamos a média diária do retorno logarítmico

log_return_d = PG['log_return'].mean()
print(f'\nMédia diária{(len("Saída formatada") - len("Média diária")) * " "} '
      f'-> {log_return_d}')

# Como podemos observar esse não é um bom número, vamos melhorar calculando a média anual.
# Para isso devemos lembrar sempre que estamos falando de ano -> pregão => portanto,
# trabalharemos com 250 dias

log_return_a = PG['log_return'].mean() * 250
print(f'Média anual{(len("Saída formatada") - len("Média anual")) * " "} '
      f'-> {log_return_a}')

# Vamos melhorar um pouco esta saída

print(f'Saída formatada -> {str(round(log_return_a, 6) * 100) + "%"}')
