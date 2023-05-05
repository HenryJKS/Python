import pandas as pd

carros = ['Jetta Variant', 'Passat', 'Crossfox']
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

#Series são arrays unidimensionais capazes de armazenar qual tipo de dado
#Criando um series a partir de uma lista
pd.Series(carros)

#Dataframe são arrays bidimensionais (ROWS X COLUMNS), podem ser criado atraves de uma Array, Series, Dicionario, Lista

#Dataframe a patir de um dicionario
dataset = pd.DataFrame(dados)

#Dataframe a partir de um dado externo
#"sep" = separador que é usado em arquivo, "index_col" = qual indice será usado como principal
dataset2 = pd.read_csv('./Datas/db.csv', sep= ';', index_col= 0)

print(dataset2)