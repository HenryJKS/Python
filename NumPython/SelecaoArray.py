#Seleção em arrays Numpy

import numpy as np


km = np.array([44410., 5712., 37123., 0., 25757., 2000.])
anos = np.array([2003, 1991, 1990, 2019, 2006, 2013])

contador = np.arange(0, 10)
dados = np.array([km, anos])
print(dados)

#Selecionando um numero em uma variavel
item = 6
index = item - 1
print(contador[index])

#Fatiamento, para pegar um seleção de valores, com passos 2 (pular 2 casas)
print(contador[1:8:2])

#Pegar somente numeros pares
print(contador[0::2])

#Selecionando somente os indexes 1, 2, 3 das 2 dimensões
print(dados[:, 1:3])

#Fazer km_media somentes desse veículos selecionado
print(dados[:, 1:3][0] / (2019 - dados[:, 1:3][1]))

#Array com boolean, visualizar somente numeros maiores que 5
print(contador[contador > 5])

#Calcular a km_media dos veiculos com fabricação depois de 2000
#print(dados[:, dados[1] > 2000][0] / (2019 - dados[:, dados[1] > 2000][1]) ) 
calc1 = (dados[:, dados[1] > 2000][0])
calc2 = (dados[:, dados[1] > 2000][1])

print(calc1)
print(calc2)

km_media = calc1 / (2019 - calc2)

print(km_media)
