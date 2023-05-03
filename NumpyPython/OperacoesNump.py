#Operações aritmeticas com Numpy

import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757., 2000.])
anos = np.array([2003, 1991, 1990, 2019, 2006, 2013])

#Criando um variavel 'idade = 2019' menos o array anos
idade = 2019 - anos
print(idade)

#Operações com 2 arrays
km_media = km / idade
print(km_media)

#Array com 2 dimensoes
dados = np.array([km, anos])
print(dados)

#Consultar um indice só em um array
print(dados[0][1])
