#Iterando (Usando For e If) com Dataframes

import pandas as pd

dataset = pd.read_csv('./Datas/db.csv', sep= ';', index_col=0)

#A função iterrows() é usada para iterar sobre as linhas de um DataFrame do pandas na forma de par (índice, série)
#Essa função itera sobre as colunas do DataFrame e retorna uma tupla com o nome da coluna e o conteúdo em forma de série
#Por exemplo, se você tiver um DataFrame com as colunas “Nome” e “Idade”, a função iterrows() retornará uma tupla com o nome da coluna e o conteúdo em forma de série para cada linha do DataFrame

dataset.iterrows

#Iterando com iterrows
for index, row in dataset.iterrows():
    if(2019 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = round(row['Quilometragem'] / (2019 - row['Ano']),2)
    else:
        dataset.loc[index, 'Km_media'] = 0


