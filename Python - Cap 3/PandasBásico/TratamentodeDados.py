#Tratamento de dados

import pandas as pd

dataset = pd.read_csv('./Datas/db.csv', sep= ';', index_col=0)
dataset2 = pd.read_csv('./Datas/db.csv', sep= ';', index_col=0)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#Verificar as informações dos dados
dataset.info()
#Mostra-se que "Quilometragem" possui menos valores non-null, podendo excluir alguns dados

#Verificando as "Quilometragem" se for nulo
print(dataset[dataset.Quilometragem.isna()])

#Podemos fazer um tratamento para que o codigo não descarte esses dados que tem Quilometragem NaN
#esse comando substituimos o valores NaN por 0
dataset.fillna(0, inplace= True)

#Verificando os valores
dataset.query('Zero_km == True')


#Porém caso queremos eleminar os dados NaN podemos usar o DropNaN
dataset2.dropna(subset= ['Quilometragem'], inplace= True)
