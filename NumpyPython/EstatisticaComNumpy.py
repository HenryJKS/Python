#Estatisticas com Numpy
import numpy as np

anos = np.loadtxt(fname = "./Datas/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "./Datas/carros-km.txt")
valor = np.loadtxt(fname = "./Datas/carros-valor.txt")


#Column_Stack, ele cria uma tupla (Linhas x Colunas)
dataset = np.column_stack((anos, km, valor))

#Verificar o shape 
print(dataset.shape)

#Mean, retorna a média dos elementos do array ao longo do eixo especificado
print(np.mean(dataset[:, 2], axis=0))

#Sum, retorna a soma dos elementos do array 
print(np.sum(dataset, axis=0))

