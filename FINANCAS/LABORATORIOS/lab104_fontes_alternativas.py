""""
Neste laboratório, vamos trabalhar com fontes alternativas ao yahoo finance

        - quandl
"""

# Realizando os imports de: numpy, pandas_datareader, matplolib.pyplot

from pandas_datareader import data as wb
import quandl
import os
from datetime import datetime

mydata_01 = quandl.get('FRED/GDP')

print(f'Imprimindo mydata:\n{mydata_01.head()}\n{mydata_01.tail()}')

data = wb.get_data_fred('GS10')  # Requer índice qualificado
# Este exemplo mostra rendimentos de vencimento constante de 5
# anos em títulos do governo dos EUA

print(f'Imprimindo data:\n{data.head()}\n{data.tail()}')


# Para trabalhar com IEX precisamos de uma chave válida

# os.environ["IEX_API_KEY"] = "pk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Padrão de uma chave
# start = datetime(2015, 1, 1)
# end = datetime(2020, 1, 1)
# facebook = wb.DataReader('FB', 'iex', start, end)
