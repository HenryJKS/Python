import pandas as pd

#Seleção com DataFrames

dataset = pd.read_csv('./Datas/db.csv', sep= ';', index_col=0)

#Selecionando os 5 primeiros itens
dataset.head()

#Selecionando uma coluna

#O tipo que retorna é do tipo Series, o Dataframe é feito de vários Series
dataset['Valor']

#Porém podemos fazer o retorno do tipo Dataframe, adicionando somente mais um []
dataset[['Valor']]

#Selecionando Linhas [i:j]
dataset[0:3]

#Utilizando .loc para seleções (Seleciona um grupo de linhas e colunas segundo os rotulos)
#Retorna um Series
dataset.loc['Passat']

#Retornando um Dataframe, para selecionar mais de uma linha
dataset.loc[['Passat', 'DS5']]

#Retornando um Dataframe, porém somente com Colunas que eu quero
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

#Utilizando .iloc para seleções com indices numericos
#DataFrame em .iloc
dataset.iloc[[1, 2], [0, 2]]

#Series em .iloc
dataset.iloc[0:4, [0, -1, 2]]