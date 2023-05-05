#Queries com Dataframe
import pandas as pd

dataset = pd.read_csv('./Datas/db.csv', sep= ';', index_col=0)


#Seleção com dataset mais simples
dataset.Motor

#Uma Query retorna somente o Motor de 'Motor Diesel'
#Retorna um Series
select = dataset.Motor == 'Motor Diesel'
select2 = dataset.Zero_km == True
#Chamando a Query
dataset[select]

#Uma Query com mais de 1 condição
dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]

#Utilizando Método Query
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))



