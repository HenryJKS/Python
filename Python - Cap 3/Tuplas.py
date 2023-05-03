#Tuplas são sequencias para armazenar colecões de itens
#Uma das características das Tuplas, é que elas são imutaveis, ou seja não podemos modificar elas
#A lista são mutáveis 

import pandas as pd

#Criando tuplas com 'tuple'
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4')])

#Criando tuplas somente com '()'
nome = ('A', 'B', 'C')

#Para seleção em Tuplas é a mesma coisa com Array e Listas
#Acessando uma tupla dentro de outra tupla, e selecionando somente o 'Gol'
nomes_carros[-1][1]