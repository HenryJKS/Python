#Introducao do Pandas

import pandas as pd

#Comando par visualizar todas linhas possíveis
pd.set_option('display.max_rows', 10)

#Comando para visualizar todas colunas possíveis
pd.set_option('display.max_columns', 1000)

#Importando dados em uma fonte de dados .CSV 
dataset = pd.read_csv('./Datas/db.csv', sep=';')

#Ver variavel de cada coluna
dataset.dtypes

#Aplicar funções matematica em massa em variaveis
dataset[['Quilometragem', 'Valor']].describe

#Informações da variavel que recebe os dados
print(dataset.info())