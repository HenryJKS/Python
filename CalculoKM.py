#Biblioteca numpy
import numpy as np

#loadtxt carregar todos dados de um arquivo externo 
#dtype você pode mudar o tipo dos dados que chega para variavel
km = np.loadtxt('./Datas/carros-km.txt')
anos = np.loadtxt('./Datas/carros-anos.txt', dtype= int)

#print(km)
#print(anos)

#Média de km de cada modelo de carro
km_media = km / (2022 - anos)

print(km_media)