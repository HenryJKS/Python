#Atributos e Métodos no numpy

import numpy as np

dados = np.array([[44410.,  5712., 37123.,0., 25757.], [ 2003.,  1991.,  1990.,  2019.,  2006.]])
contador = np.arange(10)



#Ver a tupla de um array (TUPLA = Linhas x Colunas)
print(dados.shape)

#Números de dimensoes
print(dados.ndim)

#Tipo de dados dentro de uma array
print(dados.dtype)

#Transformar Linhas em Conlunas
print(dados.T)

#Transformar uma array em uma lista
print(dados.tolist())

#Retorna um array que contém os mesmo dados com uma nova forma
contadorreshape = np.reshape(contador, (5, 2), order='C')
print(contadorreshape)

#Concatenando Arrays
km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]

info_carros = (km + anos)
#Posso usar um reshape nesse nova array concatenado
info_carros_reshape = np.reshape(info_carros, (5, 2), order='F')
print(info_carros_reshape)

#Alterar a forma e o tamanho do array

#Copiando dados de uma variavel com .copy() e passando para outra
dados_new = dados.copy()

#Criando uma nova linha com RESIZE
dados_new.resize(3, 5, refcheck=False)

#Preenchendo essa nova linha
dados_new[2] = dados_new[0] / (2019 - dados_new[1])

print(dados_new)


